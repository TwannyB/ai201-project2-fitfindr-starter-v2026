"""
The FitFindr planning loop.

This is the file that makes FitFindr an agent rather than a script. It decides
which tool to run next based on what the last one returned.

If your loop calls all three tools no matter what comes back, you have a list
of function calls. A loop looks at the last result before it picks the next
step. **That branch is the graded part of this unit.**

Build and test your three tools in `tools.py` first. Then come here.

    python agent.py          runs both example paths below
"""

import re

import config
import trace
from tools import search_listings, suggest_outfit, create_fit_card
from generate import ModelUnavailable
import mcp_client


# ── session state ─────────────────────────────────────────────────────────────

def new_session(query: str, wardrobe: dict | None) -> dict:
    """
    A fresh session for one user interaction.

    The session is the single source of truth for a run. Every tool result goes
    in here, and the next tool reads it back out.

    You could pass values straight from one call to the next. It would work,
    and you would not be able to test it — you can't print a variable you have
    already overwritten. Going through the session is what makes the state
    visible, and unit 4 has you write a criterion about exactly that.

    Add fields if you need them.
    """
    return {
        "query": query,              # what the user typed
        "parsed": {},                # description / size / max_price you pulled out of it
        "searched": False,           # True once search_listings has run, even if it found nothing
        "search_results": [],        # everything search_listings returned
        "selected_item": None,       # the one you chose — goes into suggest_outfit
        "wardrobe": wardrobe,        # the user's wardrobe; None until get_wardrobe runs
        "wardrobe_checked": False,   # True once the empty / missing-category check has run
        "missing_categories": [],    # tops/bottoms/shoes the wardrobe can't supply
        "wardrobe_note": None,       # shown to the user when the wardrobe is empty or has gaps
        "outfit_suggestion": None,   # what suggest_outfit returned
        "fit_card": None,            # what create_fit_card returned
        "error": None,               # set when the run ended early
    }


# ── query parsing ─────────────────────────────────────────────────────────────

# "under $30", "below 30", "less than $29.99", "up to $50", or a bare "$30".
_PRICE_RE = re.compile(
    r"\b(?:under|below|less than|max(?:imum)?|up to)\s+\$?\s*(\d+(?:\.\d+)?)"
    r"|\$\s*(\d+(?:\.\d+)?)",
    re.IGNORECASE,
)

# "size M", "in size 8", "size W30 L30", "size medium", "size one size".
# Longer alternatives come first so "xl" isn't read as "x" and "xxs" not as "s".
_SIZE_RE = re.compile(
    r"\b(?:in\s+)?size\s+("
    r"one\s+size|extra[\s-]+small|extra[\s-]+large|x-small|x-large"
    r"|small|medium|large"
    r"|w\d+(?:\s+l\d+)?|(?:us\s*)?\d+(?:\.\d+)?"
    r"|xxs|xxl|xs|xl|s|m|l"
    r")\b",
    re.IGNORECASE,
)

_SIZE_WORDS = {
    "small": "S",
    "medium": "M",
    "large": "L",
    "extra small": "XS",
    "x-small": "XS",
    "extra large": "XL",
    "x-large": "XL",
    "one size": "One Size",
}

_FILLER_RE = re.compile(
    r"\b(?:i'?m\s+)?(?:looking\s+for|searching\s+for|i\s+want|i\s+need"
    r"|find\s+me|show\s+me)\b",
    re.IGNORECASE,
)


def _parse_query(query: str) -> dict:
    """
    Pull a description, a size, and a max_price out of a plain-language query.

    Regex, not the model: the same query always parses the same way, and it
    costs no calls. Whatever isn't a price or a size becomes the description.
    """
    max_price = None
    price_match = _PRICE_RE.search(query)
    if price_match:
        max_price = float(price_match.group(1) or price_match.group(2))
        query = query[: price_match.start()] + " " + query[price_match.end():]

    size = None
    size_match = _SIZE_RE.search(query)
    if size_match:
        raw = re.sub(r"[\s-]+", " ", size_match.group(1).lower())
        size = _SIZE_WORDS.get(raw) or _SIZE_WORDS.get(raw.replace(" ", "-")) or raw.upper()
        query = query[: size_match.start()] + " " + query[size_match.end():]

    description = _FILLER_RE.sub(" ", query)
    description = re.sub(r"[,.!?;:]", " ", description)
    description = " ".join(description.split())

    return {"description": description, "size": size, "max_price": max_price}


def _no_results_message(parsed: dict) -> str:
    """Say what the user could change, based on what was actually searched for."""
    description = parsed["description"]
    size = parsed["size"]
    max_price = parsed["max_price"]

    if not description:
        return (
            "I couldn't tell what you're looking for. Describe the item, e.g. "
            "'vintage graphic tee under $30, size M'."
        )

    searched = f'No listings matched "{description}"'
    if size:
        searched += f" in size {size}"
    if max_price is not None:
        searched += f" under ${max_price:g}"

    suggestions = []
    if max_price is not None:
        suggestions.append(f"raising or removing the ${max_price:g} price limit")
    if size:
        suggestions.append("dropping the size")
    suggestions.append(
        "using fewer or broader words (just the item type, like \"jacket\" or \"jeans\")"
    )

    if len(suggestions) == 1:
        advice = suggestions[0]
    else:
        advice = ", ".join(suggestions[:-1]) + ", or " + suggestions[-1]
    return f"{searched}. Try {advice}."


# An outfit needs a top, bottoms and shoes. Outerwear and accessories are extras,
# so not owning them isn't a gap.
_CORE_CATEGORIES = ["tops", "bottoms", "shoes"]


def _wardrobe_gaps(wardrobe: dict, selected_item: dict) -> list[str]:
    """
    Core categories the outfit can't fill: not in the wardrobe, and not the
    selected item's own category (buying shoes covers the shoes).
    """
    owned = {item.get("category") for item in wardrobe.get("items") or []}
    return [
        c for c in _CORE_CATEGORIES
        if c not in owned and c != selected_item.get("category")
    ]


# ── planning loop ─────────────────────────────────────────────────────────────

def run_agent(query: str, wardrobe: dict | None = None) -> dict:
    """
    Run the loop once and return the finished session.

    Args:
        query:    what the user asked for, in plain language
                  (e.g. "vintage graphic tee under $30, size M").
        wardrobe: None (the default) to read the user's saved wardrobe with
                  get_wardrobe over MCP, after a listing is chosen. Or pass a
                  wardrobe dict to use that instead and skip the fetch — evals
                  pass get_example_wardrobe() / get_empty_wardrobe() so runs
                  stay comparable.

    Returns:
        The session dict. **Check session["error"] first** — if it isn't None,
        the run ended early and the later fields will still be None.
        Otherwise check session["wardrobe_note"]: set when the wardrobe is
        empty or missing tops, bottoms or shoes. The run still finishes then.

    ─────────────────────────────────────────────────────────────────────────
    TODO — build this, following the branch rule you wrote in Milestone 2.

      1. Start a session with new_session().

      2. Count the times round the loop, and call trace.check_iterations(count)
         on each one before you go again. It raises when the count passes
         MAX_ITERATIONS in config.py — see trace.py.

      3. Parse the query into a description, a size, and a max_price. Regex,
         string splitting, or asking the model are all fine — say which you
         chose in your README. Put the result in session["parsed"].

      4. Call search_listings() with what you parsed.
         Put the results in session["search_results"].

         ⚠️ THIS IS THE BRANCH. If nothing came back:
              - put a message in session["error"] saying what the user could
                change — "No results" is not that message
              - return the session
              - do NOT call suggest_outfit with nothing

      5. Choose an item — the first result is fine. Put it in
         session["selected_item"].

      6. Call suggest_outfit() with the selected item and the wardrobe.
         Put the result in session["outfit_suggestion"].

      7. Call create_fit_card() with the outfit and the item.
         Put the result in session["fit_card"].

      8. Return the session.

    ─────────────────────────────────────────────────────────────────────────
    IN UNIT 4 you come back and add two things:

      • Trace calls. One per step. `trace.step("search_listings", inputs=...,
        returned=...)` — see trace.py. Your README needs the output.

      • A handler for ModelUnavailable, so a bad key produces a message rather
        than a stack trace. The import is already at the top of this file.
    """
    session = new_session(query, wardrobe)

    count = 0

    # Each pass looks at what the session holds so far and picks the one next
    # step. The run ends when the fit card is written, or early at the branch.
    try:
        while True:
            count += 1
            trace.check_iterations(count)

            if not session["parsed"]:
                session["parsed"] = _parse_query(query)

            elif not session["searched"]:
                parsed = session["parsed"]
                session["search_results"] = mcp_client.call_tool(
                    "search_listings",
                    {
                        "description": parsed["description"],
                        "size": parsed["size"],
                        "max_price": parsed["max_price"]
                    }
                    )
                #ADD STEP TRACE HERE
                trace.step("search_listings", inputs={"description": parsed["description"], "size": parsed["size"], "max_price": parsed["max_price"]}, returned=session["search_results"])
                session["searched"] = True

            elif not session["search_results"]:
                # The branch: nothing to style, so stop before suggest_outfit.
                session["error"] = _no_results_message(session["parsed"])
                return session

            elif session["selected_item"] is None:
                session["selected_item"] = session["search_results"][0]

            elif session["wardrobe"] is None:
                # No wardrobe was passed in, so read the saved one over MCP.
                # Only the MCP call is inside the try: it's the only thing
                # here that can raise MCPError.
                try:
                    session["wardrobe"] = mcp_client.call_tool("get_wardrobe", {})
                except mcp_client.MCPError:
                    # Can't continue: styling with no wardrobe would hide a
                    # broken file. str(exc) is a generic MCP message (see
                    # step 5), so say what to do instead.
                    session["error"] = (
                        "Couldn't read your saved wardrobe. Check that "
                        "data/wardrobe.json is valid JSON, or delete it to reset "
                        "to the demo wardrobe."
                    )
                    trace.step("get_wardrobe", inputs={}, returned=None,
                               note="branch: MCP call failed, stopping")
                    return session
                trace.step("get_wardrobe", inputs={}, returned=session["wardrobe"])

            elif not session["wardrobe_checked"]:
                # Runs whether the wardrobe came from get_wardrobe or was passed
                # in (evals, --empty-wardrobe), so both get the same checks.
                # Neither case stops the run: suggest_outfit still has something
                # to give.
                items = session["wardrobe"].get("items") or []
                if not items:
                    session["wardrobe_note"] = (
                        "Your wardrobe is empty, so these are general styling "
                        "ideas. Add your clothes with: python app.py wardrobe add"
                    )
                    branch = "branch: empty wardrobe, continuing with general advice"
                else:
                    gaps = _wardrobe_gaps(session["wardrobe"], session["selected_item"])
                    session["missing_categories"] = gaps
                    if gaps:
                        session["wardrobe_note"] = (
                            f"Your wardrobe has no {', '.join(gaps)}, so the outfit "
                            "may be incomplete. Add some with: python app.py wardrobe add"
                        )
                        branch = f"branch: missing {', '.join(gaps)}, continuing"
                    else:
                        branch = "wardrobe covers tops, bottoms and shoes"
                trace.step("check_wardrobe",
                           inputs={"items": len(items),
                                   "selected_category": session["selected_item"].get("category")},
                           returned=session["missing_categories"], note=branch)
                session["wardrobe_checked"] = True

            elif session["outfit_suggestion"] is None:
                session["outfit_suggestion"] = suggest_outfit(
                    session["selected_item"], session["wardrobe"], session["missing_categories"]
                )
                #ADD STEP TRACE HERE
                trace.step("suggest_outfit", inputs={"selected_item": session["selected_item"], "wardrobe": session["wardrobe"], "missing_categories": session["missing_categories"]}, returned=session["outfit_suggestion"])

            elif session["fit_card"] is None:
                #ADD STEP TRACE HERE
                session["fit_card"] = create_fit_card(
                    session["outfit_suggestion"], session["selected_item"]
                )
                trace.step("create_fit_card", inputs={"outfit_suggestion": session["outfit_suggestion"], "selected_item": session["selected_item"]}, returned=session["fit_card"])

            else:
                return session
        
    except ModelUnavailable as exc:
        session["error"] = str(exc)
        return session


# ── running it directly ───────────────────────────────────────────────────────

def _show(session: dict) -> None:
    if session["error"]:
        print(f"  stopped: {session['error']}")
        print(f"  fit_card is {session['fit_card']!r} — it should still be None here")
        return

    item = session["selected_item"] or {}
    print(f"  found:    {item.get('title')} — ${item.get('price')} on {item.get('platform')}")
    print(f"  outfit:   {session['outfit_suggestion']}")
    print(f"  fit card: {session['fit_card']}")
    if session["wardrobe_note"]:
        print(f"  note:     {session['wardrobe_note']}")


if __name__ == "__main__":
    from utils.data_loader import get_example_wardrobe

    print("=== A query the data can match (saved wardrobe, via get_wardrobe) ===")
    _show(run_agent(query="looking for a vintage graphic tee under $30"))

    print("\n=== A query it can't ===")
    _show(run_agent(
        query="designer ballgown size XXS under $5",
        wardrobe=get_example_wardrobe(),
    ))

    print(
        "\nThe second one should stop before the fit card. If both paths look "
        "the same,\nthe branch isn't doing anything yet."
    )

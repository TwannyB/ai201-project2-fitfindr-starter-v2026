"""
The three FitFindr tools.

Each one is a standalone function you can call and test on its own, before any
of them are wired into the loop. Build and test them one at a time — three
untested tools joined by a loop is one problem that looks like six, because you
can't tell which layer is lying to you.

    search_listings(description, size, max_price)  → list[dict]
    suggest_outfit(new_item, wardrobe)             → str
    create_fit_card(outfit, new_item)              → str
    get_wardrobe(category=None)                    → dict  (capstone)
    check_grounding(outfit, wardrobe)              → dict  (capstone; a check, not a tool)

All three are stubs right now. They run and they do nothing — that's the
starting position and it's deliberate.

⚠️ Before you write any of them, fill in the **Tool Inventory** section of your
README (Milestone 2). Four lines per tool: what it does, each input with its
type, exactly what it returns, and what it returns when it has nothing to give.
That last line is what your loop branches on. "Returns a list" earns nothing —
the description has to say what is *in* the list.
"""

import re

import config  # noqa: F401 — you'll use this in search_listings
from generate import generate
from utils.data_loader import load_listings
from utils.wardrobe_store import CATEGORIES, load_wardrobe


# ── shared helpers ────────────────────────────────────────────────────────────

_STOPWORDS = {
    "a", "an", "the", "and", "or", "for", "with", "in", "of", "to", "on", "my",
    "me", "i", "im", "looking", "want", "need", "some", "something", "size",
    "under", "below", "less", "than", "like", "that", "is", "it",
}


def _stem(word: str) -> str:
    """Strip a trailing plural 's' so "jeans" matches "jean" and "tops" matches "top"."""
    return word[:-1] if len(word) > 3 and word.endswith("s") else word


def _words(text: str) -> set[str]:
    """Lowercase keyword set for `text`, minus stopwords, plurals stemmed."""
    found = re.findall(r"[a-z0-9]+", (text or "").lower())
    return {_stem(w) for w in found if w not in _STOPWORDS}


def _is_one_size(size: str) -> bool:
    return size.strip().upper().startswith("ONE SIZE")


def _size_tokens(size: str) -> set[str]:
    """
    Break a size string into whole tokens.

    "S/M" → {S, M}, "US 8.5" → {8.5}, "W30 L30" → {W30, L30},
    "XL (oversized)" → {XL}. Parenthetical notes and a leading "US" are dropped.
    """
    cleaned = re.sub(r"\(.*?\)", " ", size.upper())
    return {t for t in re.split(r"[/\s]+", cleaned) if t and t != "US"}


def _size_matches(listing_size: str, wanted: str) -> bool:
    """
    True when every token of the wanted size is a whole token of the listing's
    size. "One Size" listings only match a request for one size.
    """
    if _is_one_size(wanted):
        return _is_one_size(listing_size)
    if _is_one_size(listing_size):
        return False
    wanted_tokens = _size_tokens(wanted)
    return bool(wanted_tokens) and wanted_tokens <= _size_tokens(listing_size)


def _describe_item(item: dict) -> str:
    """Format a listing dict as prompt text. Brand is only included when present."""
    lines = [
        f"Title: {item.get('title')}",
        f"Category: {item.get('category')}",
        f"Colors: {', '.join(item.get('colors') or [])}",
        f"Style tags: {', '.join(item.get('style_tags') or [])}",
        f"Size: {item.get('size')}",
        f"Condition: {item.get('condition')}",
        f"Price: ${item.get('price')}",
        f"Platform: {item.get('platform')}",
    ]
    if item.get("brand"):
        lines.append(f"Brand: {item['brand']}")
    if item.get("description"):
        lines.append(f"Description: {item['description']}")
    return "\n".join(lines)


# A wardrobe ID with its label punctuation: "w_003: ", "(w_003)", "w_003 ".
# Used to keep IDs out of the fit card.
_WARDROBE_ID_RE = re.compile(r"\(?\bw_\d{3}\b\)?:?\s*")


def _describe_wardrobe_piece(piece: dict) -> str:
    """
    One prompt line per saved piece, starting "w_003: White ribbed tank top" —
    the same "id: name" the outfit format asks the model to write back, so it
    copies rather than translates.
    """
    line = (
        f"{piece.get('id')}: {piece.get('name')} ({piece.get('category')}; "
        f"colors: {', '.join(piece.get('colors') or [])}; "
        f"style: {', '.join(piece.get('style_tags') or [])})"
    )
    if piece.get("notes"):
        line += f" — {piece['notes']}"
    return line


# ── Tool 1: search_listings ───────────────────────────────────────────────────

def search_listings(
    description: str,
    size: str | None = None,
    max_price: float | None = None,
) -> list[dict]:
    """
    Search the listings data for items matching a description, and optionally a
    size and a price ceiling.

    This is the tool that doesn't call the model, which makes it the easiest one
    to test and the one to move onto MCP in unit 4.

    Args:
        description: keywords describing what the user wants
                     (e.g. "vintage graphic tee").
        size:        a size string to filter by, or None to skip size filtering.
                     Match case-insensitively — "M" should match "S/M".

                     ⚠️ Read the sizes in the data before you reach for a plain
                     substring test. `"s" in "us 9"` is True, and so is
                     `"l" in "xl"`. A filter that returns shoes when someone
                     asked for a small top reads like a broken search, and it
                     will quietly cost you in unit 4 when you test criterion 1.
                     What counts as a size match is part of your spec — decide
                     it and write it into your Tool Inventory.
        max_price:   maximum price, inclusive, or None to skip price filtering.

    Returns:
        A list of matching listing dicts, best match first.
        **Returns an empty list when nothing matches — an empty list, not None,
        and not an exception.** Your loop branches on this.

    Each listing dict has these fields:
        id, title, description, category, style_tags (list), size,
        condition, price (float), colors (list), brand (str or None), platform

    Note that `brand` is None for most listings. That is deliberate and
    realistic — thrift listings often have no brand. If something you write
    assumes a brand is always there, you will find out in unit 4.

    TODO:
        1. Load every listing with load_listings().
        2. Filter by max_price and by size, when each is provided.
        3. Score what's left by keyword overlap with `description`.
        4. Drop anything scoring zero.
        5. Sort by score, highest first, and return the listing dicts —
           at most config.SEARCH_RESULT_LIMIT of them.

    Test it from a terminal before you move on:
        python -c "from tools import search_listings; print(search_listings('graphic tee', max_price=30))"
    """
    listings = load_listings()

    if max_price is not None:
        listings = [l for l in listings if l["price"] <= max_price]

    if size:
        listings = [l for l in listings if _size_matches(l["size"], size)]

    query_words = _words(description)
    if not query_words:
        return []

    # Title and style tags say what the item *is*, so they count most.
    weighted_fields = [
        (lambda l: _words(" ".join(l["style_tags"])), 3),
        (lambda l: _words(l["title"]), 3),
        (lambda l: _words(l["category"]), 2),
        (lambda l: _words(l["brand"] or ""), 2),
        (lambda l: _words(" ".join(l["colors"])), 1),
        (lambda l: _words(l["description"]), 1),
    ]

    scored = []
    for listing in listings:
        score = sum(
            weight * len(query_words & field(listing))
            for field, weight in weighted_fields
        )
        if score > 0:
            scored.append((score, listing))

    scored.sort(key=lambda pair: pair[0], reverse=True)
    return [listing for _, listing in scored[: config.SEARCH_RESULT_LIMIT]]


# ── Tool 2: suggest_outfit ────────────────────────────────────────────────────

def suggest_outfit(
    new_item: dict,
    wardrobe: dict,
    missing_categories: list[str] | None = None,
    feedback: str | None = None,
) -> str:
    """
    Given a thrifted item and the user's wardrobe, suggest one or two outfits.

    This one calls the model, through `generate()`. You don't need to think
    about rate limits — the adapter handles pacing for you.

    Args:
        new_item: a listing dict — the item the user is considering.
        wardrobe: a wardrobe dict with an 'items' key holding a list of items.
                  **It may be empty.** Handle that.
        missing_categories: core categories (tops, bottoms, shoes) the
                  wardrobe can't supply, from agent._wardrobe_gaps. The prompt
                  tells the model to leave those slots out rather than invent
                  them. None or [] when nothing is missing.
        feedback: the problems check_grounding found in a previous answer,
                  one per line. Set only on the agent's retry; the prompt then
                  names those mistakes so the model can fix them.

    Returns:
        A non-empty string with outfit suggestions.
        With saved items, it is grounded and line-per-piece, so the grounding
        check (step 8) can read it:

            Outfit 1: <short name>
            - NEW: <listing title>
            - w_003: White ribbed tank top
            Vibe: <one sentence>

        plus a final "Missing: shoes" line when missing_categories is set.
        With an empty wardrobe, it returns general styling advice with common
        pieces and no IDs, rather than raising or returning "".

    TODO:
        1. Check whether wardrobe['items'] is empty.
        2. If it is, ask the model for general styling ideas for this item.
        3. If it isn't, format the wardrobe items into the prompt and ask for
           specific combinations naming pieces the user already owns.
        4. Return the model's response.

    Test it from a terminal before you move on:
        python -c "from tools import suggest_outfit; from utils.data_loader import get_example_wardrobe, load_listings; print(suggest_outfit(load_listings()[0], get_example_wardrobe()))"
    """
    items = (wardrobe or {}).get("items") or []
    system = (
        "You are a thrift-savvy stylist. Give concrete, wearable outfit ideas "
        "in plain text. Be brief: no more than about 120 words."
    )

    if not items:
        prompt = (
            "Someone is considering this thrifted item:\n\n"
            f"{_describe_item(new_item)}\n\n"
            "They haven't shared their wardrobe. Suggest one or two outfits "
            "built around this item using common, easy-to-find pieces "
            "(e.g. 'straight-leg jeans', 'white sneakers'), and say what vibe "
            "each outfit gives."
        )
    else:
        system = (
            "You are a thrift-savvy stylist. You build outfits only from pieces "
            "the user actually owns, plus the one new item. You never suggest "
            "buying or adding anything else. Follow the output format exactly. "
            "Be brief: no more than about 170 words."
        )
        wardrobe_text = "\n".join(_describe_wardrobe_piece(p) for p in items)

        if missing_categories:
            missing = ", ".join(missing_categories)
            missing_rule = (
                f"- Their wardrobe has no {missing}. Leave that slot out of the "
                "outfits instead of inventing a piece for it, and end your answer "
                f"with this line: Missing: {missing}\n"
            )
        else:
            missing_rule = ""

        prompt = (
            "Someone is considering this thrifted item:\n\n"
            f"{_describe_item(new_item)}\n\n"
            "Here is everything they own, one piece per line as id: name:\n"
            f"{wardrobe_text}\n\n"
            "Suggest one or two outfits, each pairing the new item with 2 to 4 "
            "pieces from that list.\n\n"
            "Rules:\n"
            "- Use only pieces from the list. The new item is the only piece "
            "that isn't from the wardrobe.\n"
            "- Write each wardrobe piece on its own line as its id and name, "
            "copied exactly from the list.\n"
            "- Don't suggest adding anything else (no extra shoes, jewelry or "
            "layers), not even in the Vibe line.\n"
            "- Don't add details about a piece that aren't in the list.\n"
            f"{missing_rule}"
            "\n"
            "Format (the <...> parts are placeholders; repeat the block for "
            "Outfit 2):\n\n"
            "Outfit 1: <short name>\n"
            "- NEW: <the new item's title>\n"
            "- <id>: <name exactly as listed>\n"
            "- <id>: <name exactly as listed>\n"
            "Vibe: <one sentence about the look, naming no other pieces>\n"
        )
        if feedback:
            # A retry after a failed grounding check. Naming the exact mistakes
            # works better than repeating the rules, and it also changes the
            # prompt, so the cache can't hand back the same bad answer.
            prompt += (
                "\nYour previous answer broke the rules:\n"
                f"{feedback}\n"
                "Fix this: use only ids and names copied exactly from the list.\n"
            )

    response = generate(prompt, system=system)
    if not response.strip():
        return (
            f"Couldn't come up with an outfit for {new_item.get('title')} right "
            "now. Try again, or pair it with neutral basics you already own."
        )
    return response


# ── Grounding check (capstone) ────────────────────────────────────────────────
#
# Not a tool the agent chooses to call, and not on MCP: it's a deterministic
# check on suggest_outfit's output that the loop always runs. No model call.

# A piece line from suggest_outfit's format: "- NEW: <title>" or "- w_003: <name>".
# Bullets may come back as -, * or •, and the label may be wrapped in **bold**.
_PIECE_LINE_RE = re.compile(r"^[-*•]\s*\**\s*(NEW|w_\d{3})\s*\**\s*:\s*\**\s*(.*?)\s*\**\s*$",
                            re.IGNORECASE)
_ANY_ID_RE = re.compile(r"\bw_\d{3}\b")


def _name_words(text: str) -> set[str]:
    return set(re.findall(r"[a-z0-9]+", (text or "").lower()))


def check_grounding(outfit: str, wardrobe: dict) -> dict:
    """
    Check that every piece in a suggest_outfit answer is in the saved wardrobe.

    Reads the line-per-piece format and flags three kinds of problem:

      • unknown_ids — an id that isn't in the wardrobe (on a piece line or
                      anywhere else in the text, e.g. the Vibe line).
      • mismatched  — a real id whose name has words the saved name doesn't.
                      Shortening is fine ("Black denim jacket" for "Vintage
                      black denim jacket"); adding is not ("Oversized black
                      denim jacket" — an invented detail).
      • unlisted    — a piece line with no id at all, e.g. "- Gold hoops".

    Plus one format problem: a non-empty wardrobe and no cited pieces, which
    means the answer can't be checked.

    Known gap: an unowned piece mentioned only in prose (a Vibe line saying
    "add some hoops") has no line and no id, so this can't see it.

    Args:
        outfit:   the string suggest_outfit returned.
        wardrobe: the wardrobe dict it was given.

    Returns:
        {"grounded": True | False | None,  # None = not checked (see skipped)
         "skipped": str | None,
         "cited_ids": [...], "unknown_ids": [...], "mismatched": [...],
         "unlisted": [...], "problems": [human-readable strings]}
        With an empty wardrobe, suggest_outfit gives general advice by design,
        so the check is skipped: grounded is None.
    """
    result = {
        "grounded": None, "skipped": None, "cited_ids": [], "unknown_ids": [],
        "mismatched": [], "unlisted": [], "problems": [],
    }
    items = (wardrobe or {}).get("items") or []
    if not items:
        result["skipped"] = "empty wardrobe: general advice isn't meant to be grounded"
        return result

    saved = {item["id"]: item["name"] for item in items}

    for raw in (outfit or "").splitlines():
        line = raw.strip()
        if not line or line[0] not in "-*•":
            continue  # Outfit / Vibe / Missing lines aren't pieces
        if line.startswith("**") and not _PIECE_LINE_RE.match(line):
            continue  # a bold header like "**Outfit 1**", not a bullet
        match = _PIECE_LINE_RE.match(line)
        if not match:
            result["unlisted"].append(line)
            continue
        label, name = match.group(1), match.group(2)
        if label.upper() == "NEW":
            continue
        piece_id = label.lower()
        if piece_id not in saved:
            continue  # counted below with every other id in the text
        if piece_id not in result["cited_ids"]:
            result["cited_ids"].append(piece_id)
        if not _name_words(name) <= _name_words(saved[piece_id]):
            result["mismatched"].append(
                {"id": piece_id, "said": name, "saved": saved[piece_id]}
            )

    for found in _ANY_ID_RE.findall((outfit or "").lower()):
        if found not in saved and found not in result["unknown_ids"]:
            result["unknown_ids"].append(found)

    for piece_id in result["unknown_ids"]:
        result["problems"].append(f"{piece_id} isn't in their wardrobe.")
    for m in result["mismatched"]:
        result["problems"].append(
            f'{m["id"]} was called "{m["said"]}", but it is "{m["saved"]}".'
        )
    for line in result["unlisted"]:
        result["problems"].append(f'"{line}" has no wardrobe id.')
    if not result["cited_ids"] and not result["problems"]:
        result["problems"].append(
            "No wardrobe pieces were listed in the '- <id>: <name>' format."
        )

    result["grounded"] = not result["problems"]
    return result


# ── Tool 3: create_fit_card ───────────────────────────────────────────────────

def create_fit_card(outfit: str, new_item: dict) -> str:
    """
    Write a short caption someone would actually post about the find.

    This calls the model too.

    Args:
        outfit:   the outfit suggestion string from suggest_outfit().
        new_item: the listing dict for the item.

    Returns:
        A two-to-four sentence caption.
        If `outfit` is empty or whitespace, return a descriptive message rather
        than raising.

    The caption should read like a real post rather than a product description,
    mention the item and its price and platform once each, and be specific about
    the vibe.

    It should also come out **differently for different inputs**. If you run
    this three times on the same item and get three word-for-word identical
    strings, it's one of two things, and both are near the top of `config.py`:

        • CACHE_ENABLED — the adapter handed back an answer it already had
        • TEMPERATURE   — at 0.0 the model gives the same words every time

    TODO:
        1. Guard against an empty or whitespace-only `outfit`.
        2. Build a prompt with the item details and the outfit.
        3. Call generate() and return the response.

    Test it from a terminal before you move on:
        python -c "from tools import create_fit_card; from utils.data_loader import load_listings; print(create_fit_card('jeans and white sneakers', load_listings()[0]))"
    """
    if not outfit or not outfit.strip():
        return (
            "Couldn't write a fit card: there's no outfit suggestion to "
            "caption. Run suggest_outfit first and pass its result in."
        )

    # The outfit names wardrobe pieces as "w_003: White ribbed tank top" for the
    # grounding check. Nobody posts an ID, so strip them in code rather than
    # asking the model not to. Strings are immutable: re.sub returns a new one
    # and the caller's `outfit` is untouched.
    outfit_for_caption = _WARDROBE_ID_RE.sub("", outfit)

    system = (
        "You write short social media captions for thrifted outfits. They "
        "sound like a real person posting their find, not a product listing. "
        "Describe the user's wardrobe pieces only with words that appear in the outfit text, and don't add fit, size, material or color details about them. "
        "Describe the thrifted item itself using its listing details."
    )
    prompt = (
        "Write a caption for this thrift find and the outfit built around it.\n\n"
        f"The item:\n{_describe_item(new_item)}\n\n"
        f"The outfit:\n{outfit_for_caption}\n\n"
        "Rules:\n"
        "- Two to four sentences.\n"
        "- Mention the item, its price, and the platform it's from, once each.\n"
        "- Be specific about the vibe, using real details of the item and "
        "outfit (colors, style, the pieces it's paired with).\n"
        "- Don't invent details that contradict the item or outfit above.\n"
        "- Return only the caption."
    )

    response = generate(prompt, system=system)
    if not response.strip():
        return (
            f"Couldn't write a fit card for {new_item.get('title')} right now. "
            "Try again in a moment."
        )
    return response


# ── Tool 4 (stretch): find_similar ────────────────────────────────────────────

def find_similar(item: dict) -> list[dict]:
    """
    Find other listings with a similar aesthetic to a given item.

    Like search_listings, this one doesn't call the model — it compares
    listing fields directly, so it's cheap to run and easy to test.

    Args:
        item: a listing dict — the item to find look-alikes for. It needs
              style_tags, category, and colors; id is used to leave the item
              itself out of the results.

    Returns:
        A list of listing dicts, most similar first, at most
        config.SEARCH_RESULT_LIMIT of them. Never includes the input item.
        Similarity is ranked by shared style tags first, then same category,
        then shared colors.
        **Returns an empty list when nothing shares anything with the item —
        an empty list, not None, and not an exception.**

    Each listing dict has the same fields as search_listings returns:
        id, title, description, category, style_tags (list), size,
        condition, price (float), colors (list), brand (str or None), platform

    Test it from a terminal:
        python -c "from tools import find_similar; from utils.data_loader import load_listings; print(find_similar(load_listings()[0]))"
    """
    tags = {t.lower() for t in item.get("style_tags") or []}
    colors = {c.lower() for c in item.get("colors") or []}
    category = (item.get("category") or "").lower()

    scored = []
    for listing in load_listings():
        if listing["id"] == item.get("id"):
            continue
        score = (
            3 * len(tags & {t.lower() for t in listing["style_tags"]})
            + 2 * (listing["category"].lower() == category)
            + 1 * len(colors & {c.lower() for c in listing["colors"]})
        )
        if score > 0:
            scored.append((score, listing))

    scored.sort(key=lambda pair: pair[0], reverse=True)
    return [listing for _, listing in scored[: config.SEARCH_RESULT_LIMIT]]


# ── Tool 5 (capstone): get_wardrobe ───────────────────────────────────────────

def get_wardrobe(category: str | None = None) -> dict:
    """
    Read the user's saved wardrobe from data/wardrobe.json.

    Like search_listings, this doesn't call the model.

    Args:
        category: one of tops, bottoms, outerwear, shoes, accessories to get
                only that category, or None (or "") for everything.
                Case and surrounding spaces don't matter.

    Returns:
        A wardrobe dict {"items": [...]} in the same shape suggest_outfit
        takes. Each item has: id (e.g. "w_003"), name, category,
        colors (list), style_tags (list), notes (str or None).
        Items keep their saved order. Storage fields like next_id and
        user_id are left out.
        **Returns {"items": []} when nothing is saved, or nothing is saved in
        that category — never None, and not an exception.**

    Raises:
        ValueError: if `category` isn't one of the five categories, so a typo
                    isn't mistaken for "you own nothing in that category".
                    Also if data/wardrobe.json is corrupted (from load_wardrobe).

    Test it from a terminal:
        python -c "from tools import get_wardrobe; print(get_wardrobe('shoes'))"
    """
    items = load_wardrobe().get("items") or []

    wanted = (category or "").strip().lower()
    if wanted:
        if wanted not in CATEGORIES:
            raise ValueError(
                f"Unknown category {category!r}. Use one of: {', '.join(CATEGORIES)}."
            )
        items = [item for item in items if item.get("category") == wanted]

    return {"items": items}

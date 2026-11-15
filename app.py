#!/usr/bin/env python3
"""
FitFindr — command line.

    python app.py ask 'vintage graphic tee under $30, size M'
    python app.py ask                     keep asking until you quit
    python app.py ask --empty-wardrobe    run as a user with nothing saved
    python app.py listings                browse the data  (Milestone 1)
    python app.py fields                  what fields a listing has
    python app.py examples                queries worth trying, including a dud
    python app.py wardrobe list           show your saved wardrobe
    python app.py wardrobe add            add an item (prompts for each field)
    python app.py wardrobe edit w_003     change an item; Enter keeps a value
    python app.py wardrobe remove w_003   delete an item (asks first)

Add --trace to any `ask` to print the loop step by step.

⚠️ Quote your query with SINGLE quotes. In PowerShell, "under $30" in double
quotes silently becomes "under " — PowerShell reads $30 as a variable and
substitutes nothing, so you search with no price ceiling and get no error
telling you why. Single quotes are literal in PowerShell, bash and zsh alike.
"""

import argparse
import sys

import config

# Every query here except the last one has something real to find in
# data/listings.json. If you add your own, check it against the data first — a
# query that finds nothing because the item doesn't exist looks exactly like a
# search tool that's broken.
EXAMPLE_QUERIES = [
    "vintage graphic tee under $30",
    "90s track jacket in size M",
    "silk slip dress in midi length under $40",
    "platform sneakers size 8",
    "denim jacket under $50",
    "designer ballgown size XXS under $5",   # matches nothing, on purpose
]


def cmd_fields(args):
    """Milestone 1 — you can't filter on a field that isn't there."""
    from utils.data_loader import load_listings, get_example_wardrobe

    listing = load_listings()[0]
    print("A listing has these fields:\n")
    for key, value in listing.items():
        shown = str(value)
        if len(shown) > 58:
            shown = shown[:58] + "…"
        print(f"  {key:<14} {type(value).__name__:<6} {shown}")

    item = get_example_wardrobe()["items"][0]
    print("\nA wardrobe item has these fields:\n")
    for key, value in item.items():
        shown = str(value)
        if len(shown) > 58:
            shown = shown[:58] + "…"
        print(f"  {key:<14} {type(value).__name__:<6} {shown}")

    print(
        "\nThese are what search_listings can filter on. Read a few whole "
        "listings\nwith `python app.py listings` before you write it."
    )


def cmd_listings(args):
    """Milestone 1 — read the data before you write tools against it."""
    from utils.data_loader import load_listings

    listings = load_listings()

    if args.full:
        import json
        for listing in listings[: args.n]:
            print(json.dumps(listing, indent=2))
            print()
        return

    print(f"{len(listings)} listings.\n")
    print(f"{'id':<6}{'price':>8}  {'size':<22}{'platform':<11}title")
    print("-" * 92)
    for listing in listings[: args.n]:
        print(
            f"{str(listing['id']):<6}"
            f"{listing['price']:>8.2f}  "
            f"{str(listing['size']):<22}"
            f"{listing['platform']:<11}"
            f"{listing['title'][:38]}"
        )
    if len(listings) > args.n:
        print(f"\n… {len(listings) - args.n} more. Use -n {len(listings)} to see them all.")
    print("\nRead five or six all the way through: python app.py listings --full -n 6")


def cmd_examples(args):
    print("Queries worth trying:\n")
    for query in EXAMPLE_QUERIES[:-1]:
        print(f"  python app.py ask '{query}'")
    print(f"\nAnd one the data cannot match — this is the empty-search branch:\n")
    print(f"  python app.py ask '{EXAMPLE_QUERIES[-1]}'")
    print(
        "\nSingle quotes on purpose. In PowerShell a query in \"double quotes\"\n"
        "loses the $30 — it gets read as a variable — and you search with no\n"
        "price ceiling, with nothing to tell you it happened."
    )


def _ask_one(query, wardrobe, use_trace):
    from run_log import logged_run
    import trace as trace_module

    if use_trace:
        trace_module.start_trace()

    # Same agent run, plus a record in logs/runs.jsonl (no echo: the CLI
    # prints the outfit, not JSON).
    session = logged_run(
        query, wardrobe, source="cli",
        wardrobe_source="saved" if wardrobe is None else "empty",
    )

    print()
    if session["error"]:
        print(f"  {session['error']}")
    else:
        item = session["selected_item"] or {}
        print(f"  Found:    {item.get('title')} — ${item.get('price')} on {item.get('platform')}")
        print()
        print(f"  Outfit:   {session['outfit_suggestion']}")
        print()
        print(f"  Fit card: {session['fit_card']}")
        if session.get("wardrobe_note"):
            print()
            print(f"  Note:     {session['wardrobe_note']}")
    print()

    if use_trace:
        text = trace_module.get_trace()
        if not text:
            print(
                "  (--trace printed nothing. You haven't added trace.step() calls to\n"
                "   run_agent() yet — that's unit 4, Milestone 2.)\n"
            )
    return session


def cmd_ask(args):
    from utils.data_loader import get_empty_wardrobe
    import generate

    # None means "use the saved wardrobe": run_agent fetches it with get_wardrobe.
    wardrobe = get_empty_wardrobe() if args.empty_wardrobe else None
    if args.empty_wardrobe:
        print("(running with an empty wardrobe)")

    try:
        if args.query:
            _ask_one(args.query, wardrobe, args.trace)
        else:
            print("Ask for something, or press Enter on an empty line to quit.\n")
            while True:
                try:
                    query = input("> ").strip()
                except (EOFError, KeyboardInterrupt):
                    print()
                    break
                if not query:
                    break
                _ask_one(query, wardrobe, args.trace)
    finally:
        print(generate.usage())


def build_parser():
    parser = argparse.ArgumentParser(
        prog="app.py",
        description="FitFindr",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_fields = sub.add_parser("fields", help="what fields the data has")
    p_fields.set_defaults(func=cmd_fields)

    p_list = sub.add_parser("listings", help="browse the listings data")
    p_list.add_argument("-n", type=int, default=15, help="how many to show")
    p_list.add_argument("--full", action="store_true", help="print whole records")
    p_list.set_defaults(func=cmd_listings)

    p_ex = sub.add_parser("examples", help="queries worth trying")
    p_ex.set_defaults(func=cmd_examples)

    p_ask = sub.add_parser("ask", help="run the agent")
    p_ask.add_argument("query", nargs="?")
    p_ask.add_argument("--trace", action="store_true", help="print the loop step by step")
    p_ask.add_argument(
        "--empty-wardrobe",
        action="store_true",
        help="run as a user with nothing saved — one of unit 4's failure modes",
    )
    p_ask.set_defaults(func=cmd_ask)

    p_w = sub.add_parser("wardrobe", help="view and edit your saved wardrobe")
    wsub = p_w.add_subparsers(dest="action", required=True)

    wsub.add_parser("list", help="show saved items").set_defaults(func=cmd_wardrobe_list)
    wsub.add_parser("add", help="add an item").set_defaults(func=cmd_wardrobe_add)
    p_ed = wsub.add_parser("edit", help="edit an item by id")
    p_ed.add_argument("item_id")
    p_ed.set_defaults(func=cmd_wardrobe_edit)
    p_rm = wsub.add_parser("remove", help="remove an item by id")
    p_rm.add_argument("item_id")
    p_rm.set_defaults(func=cmd_wardrobe_remove)

    return parser

CATEGORIES = "tops, bottoms, outerwear, shoes, accessories"


def _split_list(text):
    """'Red, navy ,' -> ['Red', 'navy']. Cleanup (lowercasing, dedupe) is the store's job."""
    return [part.strip() for part in text.split(",") if part.strip()]


def _print_errors(errors):
    print("Not saved:")
    for error in errors:
        print(f"  - {error}")


def _show_item(item):
    print(f"  {item['id']}  {item['name']}")
    print(f"        category:   {item['category']}")
    print(f"        colors:     {', '.join(item['colors'])}")
    print(f"        style tags: {', '.join(item['style_tags']) or '-'}")
    print(f"        notes:      {item.get('notes') or '-'}")


def cmd_wardrobe_list(args):
    from utils.wardrobe_store import load_wardrobe

    items = load_wardrobe()["items"]
    if not items:
        print("Your wardrobe is empty. Add something with: python app.py wardrobe add")
        return

    print(f"{'id':<7}{'category':<13}{'colors':<22}name")
    print("-" * 80)
    for item in items:
        colors = ", ".join(item["colors"])
        if len(colors) > 20:
            colors = colors[:19] + "…"
        print(f"{item['id']:<7}{item['category']:<13}{colors:<22}{item['name'][:40]}")
    print(f"\n{len(items)} item(s).")


def cmd_wardrobe_add(args):
    from utils.wardrobe_store import add_item

    print("Enter the details of the item to add to your wardrobe.")
    fields = {
        "name": input("Name: ").strip(),
        "category": input(f"Category ({CATEGORIES}): ").strip(),
        "colors": _split_list(input("Colors (comma-separated): ")),
        "style_tags": _split_list(input("Style tags (comma-separated, optional): ")),
        "notes": input("Notes (optional): ").strip() or None,
    }

    item, errors = add_item(fields)
    if errors:
        _print_errors(errors)
        return
    print("Added:")
    _show_item(item)


def cmd_wardrobe_edit(args):
    from utils.wardrobe_store import get_item, update_item

    item = get_item(args.item_id)
    if item is None:
        print(f"No item with ID {args.item_id}. See: python app.py wardrobe list")
        return

    print(f"Editing {item['id']}. Press Enter to keep the current value; type - to clear an optional field.")
    changes = {}

    name = input(f"Name [{item['name']}]: ").strip()
    if name:
        changes["name"] = name

    category = input(f"Category ({CATEGORIES}) [{item['category']}]: ").strip()
    if category:
        changes["category"] = category

    colors = input(f"Colors [{', '.join(item['colors'])}]: ").strip()
    if colors:
        changes["colors"] = _split_list(colors)

    tags = input(f"Style tags [{', '.join(item['style_tags'])}]: ").strip()
    if tags == "-":
        changes["style_tags"] = []
    elif tags:
        changes["style_tags"] = _split_list(tags)

    notes = input(f"Notes [{item.get('notes') or ''}]: ").strip()
    if notes == "-":
        changes["notes"] = None
    elif notes:
        changes["notes"] = notes

    if not changes:
        print("Nothing changed.")
        return

    updated, errors = update_item(item["id"], changes)
    if errors:
        _print_errors(errors)
        return
    print("Saved:")
    _show_item(updated)


def cmd_wardrobe_remove(args):
    from utils.wardrobe_store import get_item, remove_item

    item = get_item(args.item_id)
    if item is None:
        print(f"No item with ID {args.item_id}. See: python app.py wardrobe list")
        return

    _show_item(item)
    if input("Remove this item? (y/n): ").strip().lower() != "y":
        print("Cancelled.")
        return

    removed = remove_item(item["id"])
    if removed is None:  # deleted by something else in the meantime
        print(f"No item with ID {args.item_id}.")
    else:
        print(f"Removed {removed['id']} ({removed['name']}).")


def main():
    args = build_parser().parse_args()
    try:
        args.func(args)
    except KeyboardInterrupt:
        print("\nStopped.")
        sys.exit(130)
    except Exception as exc:  # noqa: BLE001 — students read this, not a traceback
        print(f"\n{type(exc).__name__}: {exc}\n", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

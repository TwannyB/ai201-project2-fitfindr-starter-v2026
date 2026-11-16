#!/usr/bin/env python3
"""
Run the capstone criteria and write down what happened. ← CAPSTONE, STEP 9

    python run_capstone_eval.py                    all five criteria, 3 runs each
    python run_capstone_eval.py --criteria 1,4,5   only these (no model calls)
    python run_capstone_eval.py --label before     names the results file

It carries out the procedures in criteria.md → "Capstone criteria" exactly as
a stranger would: real `python app.py ...` commands, each in its own process,
with typed input piped in. For every trial it records the command, the input,
the output, the exit code, and the wardrobe file before and after, and writes
it all to results/run_<date>_capstone[_label].md.

⚠️ Like run_eval.py, it does NOT decide whether a trial passed. The PASS/FAIL
cells are blank. It does record plain facts that make grading quicker (which
IDs a removal took away, whether the file changed), but whether those facts
meet the criterion is your call.

Your real data/wardrobe.json is backed up before anything runs and restored at
the end, even if the run fails or you press Ctrl-C.

Criteria 2 and 3 call the model: 30 `ask` runs, about 60 model calls. Caching
is off for them (five tries have to be five real answers), and the harness
waits at least ASK_SPACING seconds between asks, because each command is a
new process and generate.py's per-minute pacing only counts calls within one
process. Expect 10-15 minutes for a full run; criteria 1, 4 and 5 alone take
about a minute.
"""

import argparse
import datetime as dt
import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).parent
APP = ROOT / "app.py"
WARDROBE = ROOT / "data" / "wardrobe.json"
BACKUP = ROOT / "data" / "wardrobe.json.eval-backup"
RUN_LOG = ROOT / "logs" / "runs.jsonl"
RESULTS = ROOT / "results"

# Two model calls per ask; 9 s apart keeps a run of asks near 13 calls a
# minute, under the free tier's 15.
ASK_SPACING = 9.0
CORRUPT_JSON = '{"items": [broken'

ENV = {**os.environ, "AI201_CACHE": "0", "PYTHONIOENCODING": "utf-8"}

_last_ask = 0.0


# ── running commands ──────────────────────────────────────────────────────────

def cli(*args: str, stdin: str = "") -> dict:
    """Run `python app.py <args>` in a new process, the way a user would."""
    command = [sys.executable, str(APP), *args]
    started = time.perf_counter()
    proc = subprocess.run(command, input=stdin, capture_output=True, text=True,
                          encoding="utf-8", errors="replace", env=ENV, cwd=ROOT,
                          timeout=300)
    output = (proc.stdout + proc.stderr).strip()
    return {
        "command": "python app.py " + " ".join(_quote(a) for a in args),
        "stdin": stdin,
        "exit_code": proc.returncode,
        "output": output,
        "seconds": round(time.perf_counter() - started, 1),
        "traceback": "Traceback (most recent call last)" in output,
    }


def ask(*args: str) -> dict:
    """An `ask`, spaced out so separate processes stay under the rate limit."""
    global _last_ask
    wait = ASK_SPACING - (time.perf_counter() - _last_ask)
    if wait > 0:
        time.sleep(wait)
    lines_before = _log_line_count()
    result = cli("ask", *args)
    _last_ask = time.perf_counter()
    result["run_record"] = _new_log_record(lines_before)
    return result


def _quote(arg: str) -> str:
    return f"'{arg}'" if " " in arg else arg


def _log_line_count() -> int:
    if not RUN_LOG.exists():
        return 0
    with open(RUN_LOG, encoding="utf-8") as f:
        return sum(1 for _ in f)


def _new_log_record(lines_before: int):
    """The run record the CLI wrote for this ask (run_log.py), if any."""
    if not RUN_LOG.exists():
        return None
    with open(RUN_LOG, encoding="utf-8") as f:
        new = f.readlines()[lines_before:]
    return json.loads(new[-1]) if new else None


# ── the wardrobe file ─────────────────────────────────────────────────────────

def read_wardrobe():
    if not WARDROBE.exists():
        return None
    try:
        return json.loads(WARDROBE.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return "(not valid JSON)"


def fresh_demo_wardrobe() -> dict:
    """Criteria: 'delete data/wardrobe.json; the next command recreates it'."""
    if WARDROBE.exists():
        WARDROBE.unlink()
    return cli("wardrobe", "list")


def ids(wardrobe) -> list:
    return [item["id"] for item in (wardrobe or {}).get("items", [])] if isinstance(wardrobe, dict) else []


def item_by_id(wardrobe, item_id):
    for item in (wardrobe or {}).get("items", []) if isinstance(wardrobe, dict) else []:
        if item["id"] == item_id:
            return item
    return None


def add_stdin(name, category, colors, style_tags="", notes="") -> str:
    """The five prompts of `wardrobe add`, in order."""
    return "\n".join([name, category, colors, style_tags, notes]) + "\n"


# ── criterion 1: add, remove, persist ─────────────────────────────────────────

# Varied on purpose: capitals, repeats and surrounding spaces, so the stored
# values show the cleanup. Names stay under 40 characters.
C1_ITEMS = [
    ("Navy Linen Shirt", "Tops", "Navy, navy, White", "Minimal, summer", "Runs large"),
    ("  Olive Cargo Shorts ", "bottoms", " Olive ,olive", "utility", ""),
    ("Red Canvas High-Tops", "SHOES", "red, White, red", "Sneakers, Casual, casual", " Laces fray a bit "),
    ("Grey Wool Beanie", "accessories", "grey", "", ""),
    ("Tan Trench Coat", " outerwear ", "Tan, beige", "classic, Classic", "Belted"),
]


def criterion_1(run: int) -> list:
    trials = []
    setup = fresh_demo_wardrobe()
    demo_items = (read_wardrobe() or {}).get("items", [])

    for n, (name, category, colors, tags, notes) in enumerate(C1_ITEMS, 1):
        before = read_wardrobe()
        added = cli("wardrobe", "add", stdin=add_stdin(name, category, colors, tags, notes))
        after = read_wardrobe()
        new_ids = [i for i in ids(after) if i not in ids(before)]
        listed = cli("wardrobe", "list")  # a separate process
        trials.append({
            "label": f"add {n}",
            "facts": {
                "next_id before": (before or {}).get("next_id"),
                "IDs added": new_ids,
                "stored item (wardrobe.json)": item_by_id(after, new_ids[0]) if new_ids else None,
                "shown by `wardrobe list` (separate process)": _list_line(listed["output"], new_ids),
            },
            "steps": [("add", added), ("list", listed)],
        })

    for n in range(1, len(C1_ITEMS) + 1):
        before = read_wardrobe()
        target = ids(before)[-1]
        removed = cli("wardrobe", "remove", target, stdin="y\n")
        after = read_wardrobe()
        listed = cli("wardrobe", "list")
        others_before = [i for i in before["items"] if i["id"] != target]
        trials.append({
            "label": f"remove {n}",
            "facts": {
                "targeted (last listed) ID": target,
                "IDs that disappeared": [i for i in ids(before) if i not in ids(after)],
                "every other item unchanged in wardrobe.json": others_before == after["items"],
                "target still in `wardrobe list`": target in listed["output"],
            },
            "steps": [("remove", removed), ("list", listed)],
        })

    final = read_wardrobe()
    trials.append({
        "label": "after all removals",
        "facts": {
            "items equal the original demo items": final["items"] == demo_items,
            "IDs now": ids(final),
            "next_id now": final.get("next_id"),
        },
        "steps": [],
        "not_a_trial": True,
    })
    return [{"label": "fresh demo wardrobe", "steps": [("setup", setup)], "facts": {}, "not_a_trial": True}] + trials


def _list_line(output: str, wanted: list) -> list:
    return [line.strip() for line in output.splitlines() if any(w in line for w in wanted)]


# ── criterion 2: grounded outfits without shoes ───────────────────────────────

C2_QUERIES = ["denim jacket under $50"] * 3 + ["vintage levis jeans"] * 2


def criterion_2(run: int) -> list:
    steps = [("setup", fresh_demo_wardrobe()),
             ("remove w_007", cli("wardrobe", "remove", "w_007", stdin="y\n")),
             ("remove w_008", cli("wardrobe", "remove", "w_008", stdin="y\n"))]
    loaded = read_wardrobe()
    trials = [{"label": "setup: demo without shoes", "steps": steps, "not_a_trial": True,
               "facts": {"wardrobe IDs loaded": ids(loaded)}}]
    for n, query in enumerate(C2_QUERIES, 1):
        result = ask(query)
        record = result["run_record"] or {}
        trials.append({
            "label": f"trial {n}",
            "facts": {
                "query": query,
                "status / error": f"{record.get('status')} / {record.get('error')}",
                "grounding check verdict (code's, not yours)": record.get("grounded"),
                "grounding retries": record.get("grounding_retries"),
                "IDs cited": record.get("cited_ids"),
                "cited IDs not in the loaded wardrobe": [i for i in (record.get("cited_ids") or []) if i not in ids(loaded)],
                "final outfit (piece lines to grade)": record.get("outfit"),
            },
            "steps": [("ask", result)],
        })
    return trials


# ── criterion 3: empty wardrobe ───────────────────────────────────────────────

def criterion_3(run: int) -> list:
    trials = []
    for n in range(1, 6):
        result = ask("denim jacket under $50", "--empty-wardrobe")
        record = result["run_record"] or {}
        out = result["output"]
        trials.append({
            "label": f"trial {n}",
            "facts": {
                "empty-wardrobe note shown": "Your wardrobe is empty, so these are general styling ideas." in out,
                "`w_` IDs in the output": "w_0" in out,
                "fit card produced": bool(record.get("fit_card")),
                "traceback": result["traceback"],
                "exit code": result["exit_code"],
            },
            "steps": [("ask", result)],
        })
    return trials


# ── criterion 4: corrupt wardrobe file ────────────────────────────────────────

C4_MESSAGE = ("Couldn't read your saved wardrobe. Check that data/wardrobe.json is "
              "valid JSON, or delete it to reset to the demo wardrobe.")


def criterion_4(run: int) -> list:
    trials = []
    for n in range(1, 6):
        fresh_demo_wardrobe()
        good = WARDROBE.read_text(encoding="utf-8")
        WARDROBE.write_text(CORRUPT_JSON, encoding="utf-8")
        try:
            result = cli("ask", "denim jacket under $50")
        finally:
            WARDROBE.write_text(good, encoding="utf-8")  # the criterion's "restore"
        trials.append({
            "label": f"trial {n}",
            "facts": {
                "exact message shown": C4_MESSAGE in result["output"],
                "exit code": result["exit_code"],
                "traceback": result["traceback"],
                "general styling advice given instead (treated as empty)":
                    "general styling ideas" in result["output"],
            },
            "steps": [("ask with corrupt file", result)],
        })
    return trials


# ── criterion 5: validation and normalization ─────────────────────────────────

C5_CASES = [
    ("A", "repeated colors and style tags, capitals and spaces",
     add_stdin("Striped Tee", "tops", "  Red, red , NAVY, navy ", " Casual, casual,  STRIPED ", "")),
    ("B", "whitespace-only name", add_stdin("   ", "tops", "red")),
    ("C", "whitespace-only category", add_stdin("Plain Tee", "   ", "red")),
    ("D", "whitespace-only colors", add_stdin("Plain Tee", "tops", "  ,  ")),
    ("E", "invalid category 'furniture'", add_stdin("Plain Tee", "furniture", "red")),
    ("F", "style tags and notes left blank", add_stdin("Plain Hat", "accessories", "black", "", "")),
]


def criterion_5(run: int) -> list:
    trials = [{"label": "fresh demo wardrobe", "steps": [("setup", fresh_demo_wardrobe())],
               "facts": {}, "not_a_trial": True}]
    for case, what, stdin in C5_CASES:
        before = read_wardrobe()
        added = cli("wardrobe", "add", stdin=stdin)
        after = read_wardrobe()
        new_ids = [i for i in ids(after) if i not in ids(before)]
        trials.append({
            "label": f"case {case}",
            "facts": {
                "input": what,
                "`Not saved:` shown": "Not saved:" in added["output"],
                "`Added:` shown": "Added:" in added["output"],
                "wardrobe.json unchanged": before == after,
                "stored item": item_by_id(after, new_ids[0]) if new_ids else None,
            },
            "steps": [("add", added)],
        })
    return trials


CRITERIA = {
    1: ("Adding, removing, and persisting wardrobe items", "30/30 operations", criterion_1),
    2: ("Grounded outfit suggestions", "15/15 trials", criterion_2),
    3: ("Empty wardrobe behavior", "15/15 trials", criterion_3),
    4: ("Corrupt wardrobe file handling", "15/15 trials", criterion_4),
    5: ("Validation and normalization when adding items", "18/18 cases", criterion_5),
}


# ── report ────────────────────────────────────────────────────────────────────

def write_report(results: dict, args) -> Path:
    RESULTS.mkdir(exist_ok=True)
    stamp = dt.datetime.now().strftime("%Y-%m-%d_%H%M")
    path = RESULTS / f"run_{stamp}_capstone{'_' + args.label if args.label else ''}.md"
    runs = args.runs

    lines = [
        f"# Capstone run log{' — ' + args.label if args.label else ''}", "",
        "- Produced by: `run_capstone_eval.py`, following criteria.md → \"Capstone criteria\"",
        "- Each step is a real `python app.py …` command in its own process",
        f"- Runs per criterion: {runs} · caching off · {ASK_SPACING:g} s between asks",
        f"- When: {dt.datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
        "The PASS/FAIL cells are blank on purpose: grade each trial against the",
        "criterion's wording using the evidence underneath, then count.",
        "",
    ]

    for number, per_run in results.items():
        title, target, _ = CRITERIA[number]
        graded = [t["label"] for t in per_run[0] if not t.get("not_a_trial")]
        lines += [f"## Capstone criterion {number}: {title}", "", f"**Target:** {target}", "",
                  "| Trial | " + " | ".join(f"Run {r}" for r in range(1, runs + 1)) + " |",
                  "|---|" + "---|" * runs]
        lines += [f"| {label} | " + " | ".join(" " for _ in range(runs)) + " |" for label in graded]
        lines += ["", f"**Verdict:** ___ / {len(graded) * runs}", ""]

        for r, trials in enumerate(per_run, 1):
            lines += [f"### Criterion {number}, run {r}", ""]
            for t in trials:
                lines += [f"**{t['label']}**", ""]
                for key, value in t["facts"].items():
                    if isinstance(value, (dict, list)) or (isinstance(value, str) and "\n" in value):
                        shown = value if isinstance(value, str) else json.dumps(value, ensure_ascii=False)
                        lines += [f"- {key}:", "", "```", shown, "```", ""]
                    else:
                        lines.append(f"- {key}: `{value}`")
                for name, step in t["steps"]:
                    lines += ["", "<details><summary>"
                              f"{name}: <code>{step['command']}</code> → exit {step['exit_code']}, {step['seconds']} s"
                              "</summary>", ""]
                    if step["stdin"]:
                        lines += ["Typed input:", "", "```", step["stdin"].rstrip("\n"), "```", ""]
                    lines += ["Output:", "", "```", step["output"] or "(none)", "```", "", "</details>"]
                lines.append("")

    path.write_text("\n".join(lines), encoding="utf-8")
    return path


# ── main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Run the capstone criteria.")
    parser.add_argument("--runs", type=int, default=3, help="runs per criterion (default 3)")
    parser.add_argument("--criteria", default="1,2,3,4,5", help="e.g. 1,4,5")
    parser.add_argument("--label", default="", help="a name for this run, e.g. 'before'")
    args = parser.parse_args()
    chosen = [int(c) for c in args.criteria.split(",") if c.strip()]

    had_wardrobe = WARDROBE.exists()
    if had_wardrobe:
        shutil.copy2(WARDROBE, BACKUP)
        print(f"Backed up your wardrobe to {BACKUP.relative_to(ROOT)}")

    results = {}
    try:
        for number in chosen:
            title, _, run_one = CRITERIA[number]
            results[number] = []
            for r in range(1, args.runs + 1):
                print(f"Criterion {number} ({title}), run {r}/{args.runs}...", flush=True)
                results[number].append(run_one(r))
    except KeyboardInterrupt:
        print("\nStopped. Writing what finished so far.")
    finally:
        if had_wardrobe:
            shutil.copy2(BACKUP, WARDROBE)
            BACKUP.unlink()
            print("Restored your wardrobe.")
        elif WARDROBE.exists():
            WARDROBE.unlink()

    complete = {n: runs for n, runs in results.items() if len(runs) == args.runs}
    if complete:
        path = write_report(complete, args)
        print(f"\nWrote {path.relative_to(ROOT)}")
        print("Grade it against criteria.md, then commit it.")


if __name__ == "__main__":
    main()

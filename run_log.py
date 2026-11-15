"""
Structured run records. ← CAPSTONE, MILESTONE 3

Every agent run, from the CLI or over HTTP, writes one JSON object per line to
logs/runs.jsonl. Rejected requests and crashes write one too: a failure that
only shows up as a missing line is one you'll never find.

    from run_log import logged_run, log_record
    session = logged_run(query, wardrobe, source="http", wardrobe_source="saved")

The file is plain JSON Lines, so you can read it back with anything:

    python -c "import json; [print(json.loads(l)['status'], json.loads(l)['duration_ms']) for l in open('logs/runs.jsonl')]"

Where the records go:
  • always to logs/runs.jsonl
  • also to stdout when echo=True (serve.py does this). On Render the disk is
    wiped on every restart, so the file doesn't last there; stdout does, in
    the dashboard's Logs tab. The CLI doesn't echo, so it doesn't print JSON
    over your outfit.

Fields in every record:
  ts               UTC time the run started, ISO 8601
  run_id           short random ID, to match a stdout line to a file line
  source           "cli" or "http"
  status           ok | stopped | crashed | rejected
                     ok       the run finished with a fit card
                     stopped  run_agent ended early on purpose (no listings,
                              wardrobe unreadable, outfit not grounded…)
                     crashed  an exception escaped run_agent
                     rejected the request was refused before the agent ran
  query            what the user asked
  duration_ms      wall-clock time of the run
  error            session["error"], the exception, or why it was rejected

Fields when the agent ran:
  wardrobe_source  saved | request | empty
  wardrobe_items   how many pieces the agent styled from
  selected_item    id and title of the listing it chose
  missing_categories, wardrobe_note
  grounded, cited_ids, grounding_problems, grounding_retries
  outfit, fit_card the text the user saw
  model_calls, cache_hits, prompt_tokens, output_tokens
                   what this run spent, from generate.py's counters — the
                   cost measurement for Milestone 3 comes from these
"""

import datetime as dt
import json
import sys
import threading
import time
import uuid
from pathlib import Path

import config
import generate

LOG_DIR = config.ROOT / "logs"
LOG_FILE = LOG_DIR / "runs.jsonl"

_write_lock = threading.Lock()


def log_record(record: dict, echo: bool = False) -> dict:
    """
    Append one record to logs/runs.jsonl (and stdout when echo is True).

    Logging must never break a run, so a failed write is reported on stderr
    and swallowed.
    """
    line = json.dumps(record, ensure_ascii=False, default=str)
    with _write_lock:
        try:
            LOG_DIR.mkdir(exist_ok=True)
            with open(LOG_FILE, "a", encoding="utf-8") as f:
                f.write(line + "\n")
        except OSError as exc:
            print(f"[run_log] couldn't write {LOG_FILE}: {exc}", file=sys.stderr, flush=True)
        if echo:
            print(line, flush=True)
    return record


def new_record(source: str, query: str) -> dict:
    """The fields every record has, before anything has happened."""
    return {
        "ts": dt.datetime.now(dt.timezone.utc).isoformat(timespec="milliseconds"),
        "run_id": uuid.uuid4().hex[:8],
        "source": source,
        "status": None,
        "query": query,
        "duration_ms": 0,
        "error": None,
    }


def logged_run(query: str, wardrobe: dict | None, source: str,
               wardrobe_source: str, echo: bool = False) -> dict:
    """
    Run the agent once, time it, and log what happened.

    Returns the session, exactly as run_agent returned it. If run_agent raises,
    the crash is logged and the exception re-raised, so callers handle it the
    way they did before logging existed.
    """
    from agent import run_agent

    record = new_record(source, query)
    record["wardrobe_source"] = wardrobe_source

    calls_before = generate.call_count()
    hits_before = generate._cache_hits
    tokens_before = generate.token_counts()
    started = time.perf_counter()

    try:
        session = run_agent(query, wardrobe)
    except Exception as exc:
        record["status"] = "crashed"
        record["error"] = f"{type(exc).__name__}: {exc}"
        raise
    else:
        record["status"] = "stopped" if session.get("error") else "ok"
        record["error"] = session.get("error")
        _add_session_fields(record, session)
        return session
    finally:
        record["duration_ms"] = round((time.perf_counter() - started) * 1000)
        tokens_after = generate.token_counts()
        record["model_calls"] = generate.call_count() - calls_before
        record["cache_hits"] = generate._cache_hits - hits_before
        record["prompt_tokens"] = tokens_after["prompt"] - tokens_before["prompt"]
        record["output_tokens"] = tokens_after["output"] - tokens_before["output"]
        log_record(record, echo=echo)


def _add_session_fields(record: dict, session: dict) -> None:
    item = session.get("selected_item") or {}
    grounding = session.get("grounding") or {}
    record.update({
        "wardrobe_items": len((session.get("wardrobe") or {}).get("items") or []),
        "selected_item": {"id": item.get("id"), "title": item.get("title")} if item else None,
        "missing_categories": session.get("missing_categories"),
        "wardrobe_note": session.get("wardrobe_note"),
        "grounded": grounding.get("grounded"),
        "cited_ids": grounding.get("cited_ids"),
        "grounding_problems": grounding.get("problems"),
        "grounding_retries": session.get("grounding_retries"),
        "outfit": session.get("outfit_suggestion"),
        "fit_card": session.get("fit_card"),
    })

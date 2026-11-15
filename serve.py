#!/usr/bin/env python3
"""
FitFindr over HTTP. ← UNIT 9

    python serve.py                       run it on your machine
    gunicorn serve:app                    run it the way a host runs it

Everything else in this repo exits after one command. A host has nothing to
keep running, so a command line cannot be deployed. This file is the smallest
thing that can: it starts a web server, waits, and hands each request to the
same `run_agent()` your CLI calls. **No new agent logic lives here.** If your
loop works from `python app.py ask`, it works from here; if it doesn't, fix it
there, not in this file.

Two routes:

    POST /ask       {"query": "vintage graphic tee under $30",
                     "wardrobe": {...}}     ← wardrobe is optional
    GET  /health    is it awake?

`/ask` returns the session dict from `run_agent()` as JSON, unchanged — the
same keys you print from the command line, including `error`. Read
`session["error"]` first, exactly as you do everywhere else.

It runs **one request at a time**, and one route is deliberately slower than a
web server has to be. The reason is worth reading before you deploy: see the
note above `_one_at_a_time` below — it also decides which gunicorn worker you
can use.

Instrumented (capstone, Milestone 3): every /ask, including rejected and
crashed ones, writes a timed JSON record to logs/runs.jsonl and stdout. The
record format lives in run_log.py.
"""

import os
import sys
import threading

# config first, and before anything that talks to the model: it loads your .env
# and fixes the Windows console encoding for every module that imports it.
import config  # noqa: F401

from flask import Flask, jsonify, request

from run_log import log_record, logged_run, new_record
from utils.wardrobe_store import validate_wardrobe


app = Flask(__name__)


# ── one request at a time ─────────────────────────────────────────────────────
# Here's why this exists.
#
# A web server will happily run two requests at once. Two things in this repo
# assume otherwise:
#
#   • If you moved a tool onto MCP in unit 4, `mcp_client.call_tool` starts
#     `mcp_server.py` as a separate process over stdio, one per call. Two
#     overlapping requests means two extra Python interpreters, and the free
#     tier you're deploying to has 512 MB for all of it. That is the reason
#     that would still be here even if everything else were perfect.
#   • `generate.py`'s pacing window and its call counter are plain module
#     globals — deliberately, because that file is teaching pacing and quota,
#     not locking. Two threads sharing them means the per-minute limiter is
#     counting something that isn't true.
#
# What the lock covers is exactly the agent run: the part that spawns
# processes and calls the model. Reading the request, rejecting a bad one, and
# turning the answer into JSON all happen outside it — so a request with a
# malformed body comes straight back with a 400 instead of queueing behind
# somebody else's agent.
#
# Serialising the runs costs you nothing here — this is one user asking one
# question — and it keeps the deployed behaviour identical to the CLI's. When
# that stops being an acceptable trade, the fix is a real queue, not a bigger
# lock.
#
# The same constraint decides your start command, and this is the part that
# bites in deployment rather than on your machine. `mcp_client.call_tool`
# wraps `asyncio.run()`, and `asyncio.run()` refuses to start when an event
# loop is already running. An async worker always has one running. So under
# `gunicorn -k gevent` (or `-k eventlet`, or `serve:app` wrapped for an ASGI
# server like uvicorn) EVERY MCP call fails with "asyncio.run() cannot be
# called from a running event loop" — not some of them under load, all of
# them, every time, in a place your laptop never showed you.
#
#     gunicorn serve:app              ← right: the DEFAULT sync worker
#     gunicorn -k gevent serve:app    ← breaks every MCP call you make

_one_at_a_time = threading.Lock()


@app.get("/health")
def health():
    """Is the server awake? A host pings something like this to find out."""
    return jsonify({"status": "ok"})


@app.post("/ask")
def ask():
    """
    Run the agent on one query.

    In:   {"query": "...", "wardrobe": {...}}   wardrobe optional — leave it
                                                out and you get the saved
                                                wardrobe the CLI uses. On
                                                Render that's the demo
                                                wardrobe, reseeded each boot.
                                                Send your own to style from
                                                it; nothing is stored.
    Out:  the session dict from run_agent(), as JSON.
          400 {"error": ..., "problems": [...]} for a bad query or wardrobe.

    Every request leaves a record in logs/runs.jsonl and on stdout, including
    rejected and crashed ones. See run_log.py for the fields.
    """
    payload = request.get_json(silent=True)
    if not isinstance(payload, dict):
        payload = {}
    query = payload.get("query")
    query = query.strip() if isinstance(query, str) else ""
    if not query:
        # 400 rather than a stack trace: the caller can act on this one.
        return _reject("", "Send JSON with a 'query' field, e.g. "
                           '{"query": "vintage graphic tee under $30"}')

    if payload.get("wardrobe") is None:
        wardrobe, wardrobe_source = None, "saved"  # run_agent fetches it with get_wardrobe
    else:
        # A wardrobe from the request gets the same checks as one typed into
        # the CLI. Unchecked, an item with no id or name crashed the grounding
        # check and came back as a 500, and the caller couldn't tell why.
        wardrobe, problems = validate_wardrobe(payload["wardrobe"])
        if problems:
            return _reject(query, "The wardrobe you sent isn't valid.", problems)
        wardrobe_source = "request"

    # A queued request should look like a queued request. Without this the
    # second caller just sits there, and "slow" and "waiting its turn" are
    # indistinguishable from the outside — which is how people conclude the
    # deployment is broken when it is behaving exactly as designed.
    #
    # This is NOT the logging you add in the follow-along. It prints nothing
    # on the normal path, carries no timing and counts nothing; it says only
    # that this request had to wait. `locked()` can be a moment out of date,
    # so the note is occasionally missed — which costs nothing, because
    # nothing depends on it.
    if _one_at_a_time.locked():
        print(
            "  [serve] another request is still running. This one is waiting "
            "its turn — serve.py handles one at a time, on purpose.",
            file=sys.stderr,
            flush=True,
        )

    failure = None
    session = None
    with _one_at_a_time:
        try:
            # logged_run times the run and writes its record, crash or not.
            session = logged_run(query, wardrobe, source="http",
                                 wardrobe_source=wardrobe_source, echo=True)
        except Exception as exc:  # noqa: BLE001 — a 500 with a sentence beats a hang
            failure = f"{type(exc).__name__}: {exc}"

    # Outside the lock: building a response is not work the next caller should
    # be waiting on.
    if failure is not None:
        return jsonify({"error": failure}), 500

    return jsonify(session)


def _reject(query: str, message: str, problems: list[str] | None = None):
    """A 400 the caller can act on, and a log record so it isn't invisible."""
    record = new_record("http", query)
    record["status"] = "rejected"
    record["error"] = message + (" " + " ".join(problems) if problems else "")
    log_record(record, echo=True)
    body = {"error": message}
    if problems:
        body["problems"] = problems
    return jsonify(body), 400


if __name__ == "__main__":
    # PORT and 0.0.0.0 are not decoration. A host tells you which port to
    # listen on through PORT, and it reaches your process from outside the
    # container — bind 127.0.0.1 and nothing but the container itself can
    # connect, which looks exactly like a broken app from the browser.
    port = int(os.getenv("PORT", "5000"))

    # Never on by default. Flask's debugger executes code typed into a browser,
    # and a deployed app with it on is a stranger's shell. Set AI201_DEBUG=1 in
    # your own terminal when you want the reloader.
    debug = os.getenv("AI201_DEBUG", "0") == "1"

    # 127.0.0.1, not localhost: on Windows, localhost tries IPv6 first, which
    # this server doesn't listen on, and each request waits ~2 s to fall back.
    url = f"http://127.0.0.1:{port}"
    print(f"\nFitFindr is listening on {url}")
    print("It runs one request at a time — a second one waits for the first.")
    print("Ask it something from a second terminal (single quotes, as always):\n")
    print("  Windows PowerShell:")
    print(
        f"    Invoke-RestMethod -Method Post -Uri {url}/ask "
        "-ContentType 'application/json' "
        "-Body '{\"query\": \"vintage graphic tee under $30\"}'\n"
    )
    print("  macOS / Linux:")
    print(
        f"    curl -X POST {url}/ask \\\n"
        f"      -H 'Content-Type: application/json' \\\n"
        f"      -d '{{\"query\": \"vintage graphic tee under $30\"}}'\n"
    )
    print("More requests, and how to read a 400, are in RUNNING.md.")
    print("Ctrl-C to stop.\n")

    app.run(host="0.0.0.0", port=port, debug=debug)

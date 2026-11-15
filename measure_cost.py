#!/usr/bin/env python3
"""
Measure what one agent run costs. ← CAPSTONE, MILESTONE 3

Two steps, because the token counts live in the server's run records, not in
the /ask response:

  1. Send the runs:
         python measure_cost.py send
     Wakes the service, then sends 10 queries one at a time, plus one bad
     request for a failure record. Prints each run's HTTP status, round-trip
     time and grounding, and the UTC time it was sent so you can find its line
     in Render's Logs tab.

  2. Copy those 11 JSON lines from Render's Logs tab into a text file (any
     extra text on a line, like a timestamp prefix, is fine), then:
         python measure_cost.py summarize render_logs.txt
     Prints each run and the averages of model_calls, prompt_tokens,
     output_tokens and duration_ms over the successful runs. Add
     --price-in and --price-out (US$ per 1M tokens, from the model's pricing
     page) to turn the measured tokens into a dollar figure.

Why these 10 queries: each one selects a DIFFERENT listing (checked against
search_listings). The response cache is keyed by prompt, so two queries that
picked the same listing would build the same outfit prompt and the second would
come back from the cache with 0 tokens, dragging the average down. The
summary reports cache_hits so you can see that it didn't happen.

Standard library only, so it runs from any terminal with Python 3.
"""

import argparse
import datetime as dt
import json
import sys
import time
import urllib.error
import urllib.request

DEFAULT_URL = "https://fitfindr-ppek.onrender.com"

QUERIES = [
    "vintage levi's jeans",
    "y2k baby tee",
    "graphic hoodie",
    "leather jacket",
    "cargo pants",
    "band tee",
    "corduroy pants",
    "knit cardigan",
    "denim shorts",
    "flannel shirt",
]

# An invalid wardrobe: a bad id and a category that doesn't exist. Expect 400.
BAD_REQUEST = {
    "query": "denim jacket",
    "wardrobe": {"items": [{"id": "shirt1", "name": "Cap", "category": "hats",
                            "colors": ["black"], "style_tags": []}]},
}


def _request(method: str, url: str, body: dict | None = None, timeout: int = 150):
    """Returns (status, parsed JSON or text, seconds). Never raises on 4xx/5xx."""
    data = json.dumps(body).encode("utf-8") if body is not None else None
    req = urllib.request.Request(url, data=data, method=method,
                                 headers={"Content-Type": "application/json"})
    started = time.perf_counter()
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            status, raw = resp.status, resp.read()
    except urllib.error.HTTPError as exc:
        status, raw = exc.code, exc.read()
    seconds = time.perf_counter() - started
    text = raw.decode("utf-8", errors="replace")
    try:
        return status, json.loads(text), seconds
    except json.JSONDecodeError:
        return status, text, seconds


def _now() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%H:%M:%S")


def cmd_send(args):
    base = args.url.rstrip("/")

    print(f"Waking {base} (the free tier sleeps; this can take a minute)...")
    status, body, seconds = _request("GET", f"{base}/health")
    print(f"  /health: HTTP {status} in {seconds:.1f}s — not counted as a run\n")
    if status != 200:
        sys.exit(f"The service didn't answer /health with 200: {body}")

    print(f"{'#':>2}  {'sent (UTC)':<10} {'HTTP':<4} {'secs':>6}  {'result':<8} {'grounded':<8} query → selected item")
    times = []
    for n, query in enumerate(QUERIES, 1):
        sent = _now()
        status, body, seconds = _request("POST", f"{base}/ask", {"query": query})
        if isinstance(body, dict) and status == 200:
            result = "stopped" if body.get("error") else "ok"
            grounded = (body.get("grounding") or {}).get("grounded")
            item = (body.get("selected_item") or {}).get("title", "-")
            if result == "ok":
                times.append(seconds)
        else:
            result, grounded, item = "failed", "-", str(body)[:60]
        print(f"{n:>2}  {sent:<10} {status:<4} {seconds:>6.1f}  {result:<8} {str(grounded):<8} {query} → {item}")

    sent = _now()
    status, body, seconds = _request("POST", f"{base}/ask", BAD_REQUEST)
    problems = body.get("problems") if isinstance(body, dict) else body
    print(f" F  {sent:<10} {status:<4} {seconds:>6.1f}  {'rejected' if status == 400 else '??':<8} {'-':<8} bad wardrobe → {problems}")

    if times:
        print(f"\nRound-trip time, {len(times)} successful runs: average {sum(times) / len(times):.1f}s, "
              f"min {min(times):.1f}s, max {max(times):.1f}s (includes network; "
              "duration_ms in the logs is the server's own time).")
    print("\nNext: copy these runs' JSON lines from Render's Logs tab into a file, then\n"
          "  python measure_cost.py summarize <that file>")


def cmd_summarize(args):
    records = []
    with open(args.file, encoding="utf-8") as f:
        for line in f:
            start = line.find("{")
            if start == -1:
                continue
            try:
                record = json.loads(line[start:])
            except json.JSONDecodeError:
                continue
            if isinstance(record, dict) and "run_id" in record and "status" in record:
                records.append(record)

    if not records:
        sys.exit(f"No run records found in {args.file}. Each should be a JSON line with run_id and status.")

    print(f"{'run_id':<9} {'status':<9} {'ms':>7} {'calls':>5} {'cache':>5} {'in':>6} {'out':>5}  query")
    for r in records:
        print(f"{r['run_id']:<9} {r['status']:<9} {r.get('duration_ms', 0):>7} "
              f"{r.get('model_calls', '-')!s:>5} {r.get('cache_hits', '-')!s:>5} "
              f"{r.get('prompt_tokens', '-')!s:>6} {r.get('output_tokens', '-')!s:>5}  {r.get('query')}")

    ok = [r for r in records if r["status"] == "ok"]
    failed = [r for r in records if r["status"] != "ok"]
    counts = [f"{len(ok)} ok"] + [
        f"{sum(1 for r in failed if r['status'] == s)} {s}"
        for s in sorted({r["status"] for r in failed})
    ]
    print(f"\n{len(records)} records: {', '.join(counts)}")
    if not ok:
        sys.exit("No successful runs to average.")

    cached = sum(r.get("cache_hits") or 0 for r in ok)
    if cached:
        print(f"⚠️  {cached} model call(s) came from the cache and cost 0 tokens; "
              "the averages below are lower than a fresh run's.")

    def avg(field):
        return sum(r.get(field) or 0 for r in ok) / len(ok)

    calls, p_in, p_out, ms = avg("model_calls"), avg("prompt_tokens"), avg("output_tokens"), avg("duration_ms")
    print(f"\nAverage over {len(ok)} successful runs:")
    print(f"  model calls    {calls:.1f}")
    print(f"  prompt tokens  {p_in:.0f}")
    print(f"  output tokens  {p_out:.0f}")
    print(f"  total tokens   {p_in + p_out:.0f}")
    print(f"  server time    {ms / 1000:.1f} s  (min {min(r['duration_ms'] for r in ok) / 1000:.1f}, "
          f"max {max(r['duration_ms'] for r in ok) / 1000:.1f})")

    if args.price_in is not None and args.price_out is not None:
        dollars = p_in / 1e6 * args.price_in + p_out / 1e6 * args.price_out
        print(f"\n  cost per run   ${dollars:.6f}  = {p_in:.0f} × ${args.price_in}/1M + {p_out:.0f} × ${args.price_out}/1M")
        print(f"  per 1,000 runs ${dollars * 1000:.4f}")


def main():
    parser = argparse.ArgumentParser(description="Measure the cost of one FitFindr run.")
    sub = parser.add_subparsers(dest="command", required=True)

    p_send = sub.add_parser("send", help="send 10 runs and 1 bad request")
    p_send.add_argument("--url", default=DEFAULT_URL, help=f"service URL (default {DEFAULT_URL})")
    p_send.set_defaults(func=cmd_send)

    p_sum = sub.add_parser("summarize", help="average the run records copied from the logs")
    p_sum.add_argument("file", help="text file with the JSON log lines")
    p_sum.add_argument("--price-in", type=float, help="US$ per 1M prompt tokens")
    p_sum.add_argument("--price-out", type=float, help="US$ per 1M output tokens")
    p_sum.set_defaults(func=cmd_summarize)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()

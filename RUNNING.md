# Running FitFindr

**Just want to see it work?** It's live at **https://fitfindr-ppek.onrender.com**
— jump to [Try the hosted version](#try-the-hosted-version). To run it
yourself, follow the Quick start. Everything after that is reference.

---

## Quick start

You need Python 3.11, 3.12 or 3.13 (**not** 3.14), Git, and a Gemini API key
from [aistudio.google.com](https://aistudio.google.com) (free).

**1. Get the code and install** — from the folder you want it in:

```powershell
# Windows (PowerShell)
git clone https://github.com/TwannyB/ai201-project2-fitfindr-starter-v2026.git fitfindr
cd fitfindr
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
copy .env.example .env      # then open .env and paste your key after GEMINI_API_KEY=
```

```bash
# macOS / Linux
git clone https://github.com/TwannyB/ai201-project2-fitfindr-starter-v2026.git fitfindr
cd fitfindr
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env        # then open .env and paste your key after GEMINI_API_KEY=
```

**2. Check the setup.** `python test.py` checks your Python version, packages,
API key, and makes one real model call. Continue when it passes.

**3. Ask it something** — **single quotes**, always (see the warning under
[Your first five minutes](#your-first-five-minutes)):

```
python app.py ask 'vintage graphic tee under $30'
```

You get a listing, one or two outfits made from your saved wardrobe (each
piece cited by ID, like `- w_003: White ribbed tank top`), and a caption. Your
wardrobe lives in `data/wardrobe.json`. If that file doesn't exist yet (a fresh
clone), this run creates it from a demo wardrobe, `w_001`–`w_010`; if it does,
the outfits use whatever you've saved. Then edit it:

```
python app.py wardrobe list
python app.py wardrobe add          # prompts for each field
```

**4. Run it as a server** (optional) — `python serve.py`, then send requests
from a **second** terminal: the same commands as
[Try the hosted version](#try-the-hosted-version), with
`https://fitfindr-ppek.onrender.com` replaced by `http://127.0.0.1:5000`.
Use `127.0.0.1` rather than `localhost` on Windows: `localhost` tries IPv6
first, which the server doesn't listen on, and every request waits ~2 s before
falling back.

**5. Read what it recorded.** Every run, including failed ones, adds a line to
`logs/runs.jsonl`. From the project folder, in either shell:

```
python -c "import json; [print(r['ts'], r['status'], r['duration_ms'], r.get('model_calls'), r['query']) for r in map(json.loads, open('logs/runs.jsonl', encoding='utf-8'))]"
```

> Activate the virtual environment every time you open a new terminal: you
> should see `(.venv)` at the start of the prompt. The log command above only
> works from the project folder, where `logs/` is.

---

## Your first five minutes

Look at the data first, so the results make sense:

```bash
python app.py fields                    # what a listing and a wardrobe item hold
python app.py listings --full -n 6      # read six listings all the way through
python app.py examples                  # queries worth trying
python app.py ask 'vintage graphic tee under $30'
```

> **Quote your queries with single quotes**, on every operating system. In
> PowerShell, `"vintage graphic tee under $30"` in double quotes silently
> becomes `vintage graphic tee under ` — PowerShell reads `$30` as a variable
> and substitutes nothing. You get results with no price ceiling and no error
> saying so. Single quotes are literal in PowerShell, bash and zsh alike.

That last one runs the whole loop: search, read your saved wardrobe, suggest
outfits built only from pieces you own (checked by code before you see them),
and write a caption. Add `--trace` to watch each step and why it was taken.

---

## Every command

| Command | What it does |
|---|---|
| `python test.py` | Checks your environment. Run it whenever something feels off |
| `python app.py fields` | The fields a listing and a wardrobe item have |
| `python app.py listings` | Browse the data. `--full` for whole records, `-n` for how many |
| `python app.py examples` | Queries worth trying, including one that matches nothing |
| `python app.py ask '...'` | Run the agent on one query — **single quotes** |
| `python app.py ask` | Keep asking until you press Enter on an empty line |
| `python app.py wardrobe list` | Show your saved wardrobe (`data/wardrobe.json`) |
| `python app.py wardrobe add` | Add an item; prompts for each field, cleans it up, and refuses bad input with a reason |
| `python app.py wardrobe edit w_003` | Change an item; Enter keeps the current value |
| `python app.py wardrobe remove w_003` | Delete an item (asks first). IDs are never reused |
| `python serve.py` | Serves the agent over HTTP on `http://127.0.0.1:5000` |
| `python run_capstone_eval.py` | Runs the five wardrobe criteria (`criteria.md`) and writes `results/run_<time>_capstone_<label>.md`. Options: `--criteria 1,4,5` (**comma-separated**), `--runs 3`, `--label before`. It backs up `data/wardrobe.json` and restores it at the end. Criteria 2 and 3 make real model calls |
| `python run_eval.py --label before` | The earlier (unit 4) eval: every scenario five times |
| `python measure_cost.py send` | Sends ten `/ask` requests to the deployed app (or `--url http://127.0.0.1:5000`) to measure cost |
| `python measure_cost.py summarize <file>` | Averages tokens and time from saved run records. Add `--price-in` / `--price-out` (US$ per 1M tokens) for a dollar figure |
| `python agent.py` | Runs both example paths — one that matches, one that can't |
| `python mcp_server.py` / `python mcp_client.py` | Start the MCP server / ask it what tools it offers |

Useful flags on `ask`:

| Flag | What it does |
|---|---|
| `--trace` | Print each step of the loop: what went in, what came out, and why |
| `--empty-wardrobe` | Run as if nothing were saved (your file isn't touched). You get general styling advice and a note saying the wardrobe is empty |

---

## Running it as a server

Everything above exits when the command finishes. `serve.py` stays up: the
same `run_agent()`, behind two HTTP routes.

On your machine:

```bash
python serve.py
curl -X POST http://127.0.0.1:5000/ask \
  -H 'Content-Type: application/json' \
  -d '{"query": "vintage graphic tee under $30"}'
```

That's bash. On Windows, use the PowerShell requests in
[Try the hosted version](#try-the-hosted-version) with the URL swapped for
`http://127.0.0.1:5000`.

On a host, the start command is (it's already in `render.yaml`):

```bash
gunicorn serve:app --timeout 120 --threads 4
```

| Thing | What it means |
|---|---|
| `PORT` | The host tells your app which port to listen on by setting this. Both `serve.py` and `gunicorn` read it, and `serve.py` falls back to `5000` on your machine. Don't hard-code a port |
| `POST /ask` | `{"query": "...", "wardrobe": {...}}` — wardrobe optional. Returns the session dict, `error` and all |
| `GET /health` | Says `ok` if the app is awake |
| It answers one request at a time | On purpose. A second request waits for the first to finish, and prints `[serve] another request is still running` while it waits. An MCP tool call starts a whole second Python process, and the free tier's 512 MB has no room for two of those at once — and `generate.py`'s rate-limit counting assumes one caller. The reasoning is written out in `serve.py` |
| A sync worker, not async | Not `-k gevent`, not `-k eventlet`, not wrapped for uvicorn. `mcp_client.call_tool` uses `asyncio.run()`, which won't start inside a running event loop, so an async worker breaks **every** MCP call — and only once you've deployed it |
| The first request is slow | The free tier puts your app to sleep after about fifteen minutes of nothing. The next request wakes it up and waits for it — around a minute. Not a bug, and worth knowing before you demo it |

Every request, including rejected and crashed ones, leaves a timed record: see
[Run records](#run-records).

---

## Deployed on Render

**URL:** https://fitfindr-ppek.onrender.com

### How it got there

The settings are in `render.yaml` (a Render Blueprint), so the dashboard only
needs your repo and your API key:

1. Push to GitHub. Render deploys from the repo, not from your machine.
2. On [dashboard.render.com](https://dashboard.render.com): **New → Blueprint**,
   connect the GitHub repo, and pick the `main` branch. Render finds
   `render.yaml` and shows one web service, `fitfindr`, on the free plan.
3. It asks for **`GEMINI_API_KEY`** (marked `sync: false`, so it's never in the
   repo). Paste the same key that's in your `.env`.
4. **Apply.** The first build takes a few minutes. Render only marks the
   deploy **Live** after `/health` answers, so "Live" in the Events tab means
   the check already passed. To check it yourself, see
   [Try the hosted version](#try-the-hosted-version).

Every push to `main` redeploys automatically.



### What `render.yaml` sets, and why

| Setting | Why |
|---|---|
| `pip install -r requirements.txt` | Same pinned packages as local |
| `gunicorn serve:app --timeout 120 --threads 4` | **Not async** (an async worker breaks every MCP call — see the table above). The timeout is raised from gunicorn's 30 s because one `/ask` makes 2–3 model calls and starts the MCP server twice: 5–19 s locally, slower on the free CPU, longer with a grounding retry or a rate-limit wait. `--threads 4` keeps one process (512 MB) but lets `/health` answer while an `/ask` runs: with one thread, Render's 5-second health check queued behind back-to-back `/ask` requests, timed out, and Render restarted the instance. Agent runs still go one at a time through `serve.py`'s lock |
| `healthCheckPath: /health` | Render pings it before sending traffic and after each deploy |
| `PYTHON_VERSION = 3.13` | `requirements.txt` supports 3.11–3.13, not 3.14. If the build log says the version isn't found, set the full version (e.g. `3.13.5`) |
| `GEMINI_API_KEY` | The only secret. Set in the dashboard, never committed |

### Try the hosted version

> **The first request can take about a minute.** The free tier sleeps after
> 15 minutes idle and the next request wakes it, then the agent's own model
> calls take 5–20 s more. The PowerShell examples set `-TimeoutSec 120` and the
> bash ones `--max-time 120` so a cold start isn't mistaken for a failure.
>
> **Keep the JSON in single quotes**, in both shells. Inside double quotes,
> PowerShell reads `$30` as a variable and silently drops it, so the query
> loses its price limit with no error.

Windows readers: use the **PowerShell** blocks. In Windows PowerShell, `curl`
is a different command, and even `curl.exe` breaks these JSON bodies (PowerShell
5.1 strips the inner quotes when passing them to a program).

**1. Is it awake?** Expect `status: ok`.

```powershell
Invoke-RestMethod https://fitfindr-ppek.onrender.com/health -TimeoutSec 120
```

```bash
curl --max-time 120 https://fitfindr-ppek.onrender.com/health
```

**2. Ask it something, with the demo wardrobe** (what `data/wardrobe.json`
reseeds to on Render). Expect `error` empty, outfits with `- w_NNN:` lines, and
a caption with no IDs in it.

```powershell
$r = Invoke-RestMethod -Method Post -Uri https://fitfindr-ppek.onrender.com/ask -ContentType 'application/json' -TimeoutSec 120 -Body '{"query": "vintage graphic tee under $30"}'
$r.outfit_suggestion
$r.fit_card
$r.grounding.cited_ids
```

```bash
curl --max-time 120 -X POST https://fitfindr-ppek.onrender.com/ask \
  -H 'Content-Type: application/json' \
  -d '{"query": "vintage graphic tee under $30"}'
```

PowerShell prints lists nested inside the response as `System.Object[]`.
That's display only; print the field (`$r.grounding.cited_ids`) or the whole
thing with `$r | ConvertTo-Json -Depth 6`.

**3. With your own wardrobe**, sent with the request. Nothing is stored; it's
checked with the same rules as `app.py wardrobe add`: IDs like `w_001`, one of
tops/bottoms/outerwear/shoes/accessories, at least one color, at most 50 items.
Expect outfits using only these three pieces.

```powershell
$body = @'
{"query": "denim jacket under $50", "wardrobe": {"items": [
  {"id": "w_001", "name": "Cream cable-knit sweater", "category": "tops", "colors": ["cream"], "style_tags": ["cozy"]},
  {"id": "w_002", "name": "Black straight-leg trousers", "category": "bottoms", "colors": ["black"], "style_tags": []},
  {"id": "w_003", "name": "Brown suede loafers", "category": "shoes", "colors": ["brown"], "style_tags": []}]}}
'@
$r = Invoke-RestMethod -Method Post -Uri https://fitfindr-ppek.onrender.com/ask -ContentType 'application/json' -TimeoutSec 120 -Body $body
$r.outfit_suggestion
```

The closing `'@` must be at the very start of its line.

```bash
curl --max-time 120 -X POST https://fitfindr-ppek.onrender.com/ask \
  -H 'Content-Type: application/json' \
  -d '{"query": "denim jacket under $50", "wardrobe": {"items": [
        {"id": "w_001", "name": "Cream cable-knit sweater", "category": "tops", "colors": ["cream"], "style_tags": ["cozy"]},
        {"id": "w_002", "name": "Black straight-leg trousers", "category": "bottoms", "colors": ["black"], "style_tags": []},
        {"id": "w_003", "name": "Brown suede loafers", "category": "shoes", "colors": ["brown"], "style_tags": []}]}}'
```

**4. A wardrobe it should reject.** An invalid wardrobe comes back as `400`
with a `problems` list naming each mistake, and never reaches the agent. This
one has a bad ID and a category that doesn't exist:

```powershell
try {
  Invoke-RestMethod -Method Post -Uri https://fitfindr-ppek.onrender.com/ask -ContentType 'application/json' -TimeoutSec 120 -Body '{"query": "denim jacket", "wardrobe": {"items": [{"id": "shirt1", "name": "Cap", "category": "hats", "colors": ["black"], "style_tags": []}]}}'
} catch {
  # Windows PowerShell throws on a 400. Depending on the server, the body is
  # already in ErrorDetails (the local Flask server) or still in the response
  # stream (Render); this prints it either way.
  if ($_.ErrorDetails.Message) { $_.ErrorDetails.Message }
  else {
    $stream = $_.Exception.Response.GetResponseStream()
    if ($stream.CanSeek) { $stream.Position = 0 }
    (New-Object System.IO.StreamReader($stream)).ReadToEnd()
  }
}
```

```bash
curl --max-time 120 -X POST https://fitfindr-ppek.onrender.com/ask \
  -H 'Content-Type: application/json' \
  -d '{"query": "denim jacket", "wardrobe": {"items": [{"id": "shirt1", "name": "Cap", "category": "hats", "colors": ["black"], "style_tags": []}]}}'
```

Expect:

```
{"error":"The wardrobe you sent isn't valid.","problems":["Item 1: Item field \"id\" must look like w_001 (got 'shirt1').","Item 1: Item field \"category\" must be one of: tops, bottoms, outerwear, shoes, accessories."]}
```

Each of requests 2–4 leaves one JSON line in Render's **Logs** tab (`status`
`ok`, `ok`, `rejected`). `/health` isn't logged.

### What's different from running it locally

| | Local | Render (free) |
|---|---|---|
| Saved wardrobe | `data/wardrobe.json`, edited with `app.py wardrobe …`, survives restarts | **Demo wardrobe only.** The free tier's disk is wiped on every deploy, restart and sleep, so the file reseeds from the example each boot, and there are no routes to edit it. Persistence is a local feature |
| Your own wardrobe | Edit the saved one | Send it in the `/ask` body (above) |
| Run records | `logs/runs.jsonl` | The **Logs** tab: each run prints the same JSON line to stdout. The file is wiped with the disk |
| First request | Instant | ~1 minute after 15 min idle — the free tier sleeps |

### Run records

Every run writes one JSON line to `logs/runs.jsonl`: from `python app.py ask`,
from `/ask`, and also rejected requests (`status: "rejected"`) and crashes
(`status: "crashed"`). `serve.py` also prints each line to stdout, which is how
they reach Render's Logs tab. The fields are documented at the top of
`run_log.py`; the ones you'll use most:

`ts`, `run_id`, `source` (cli/http), `status` (ok/stopped/crashed/rejected),
`query`, `duration_ms`, `error`, `wardrobe_source` (saved/request/empty),
`grounded`, `grounding_retries`, `model_calls`, `prompt_tokens`, `output_tokens`.

Read them back, from the project folder, in either shell:

```
python -c "import json; [print(r['ts'], r['status'], r['duration_ms'], r.get('model_calls'), r['query']) for r in map(json.loads, open('logs/runs.jsonl', encoding='utf-8'))]"
```

`logs/` is in `.gitignore`: the records are runtime output. Copy the entries
you need into the README.

---

## Where everything lives

| File | What it does |
|---|---|
| `config.py` | Every setting worth changing — **TEMPERATURE and the cache are at the top** |
| `agent.py` | The planning loop: search, read the wardrobe, check it, suggest outfits, check grounding (one retry), write the fit card |
| `tools.py` | The tools: `search_listings`, `suggest_outfit`, `check_grounding`, `create_fit_card` |
| `utils/wardrobe_store.py` | **The saved wardrobe:** load, validate and clean items, add/edit/remove, ID counter, safe saving |
| `mcp_server.py` / `mcp_client.py` | `search_listings` and `get_wardrobe` served over MCP, and how the agent calls them |
| `generate.py` | The only thing that calls the model. Handles pacing, caching and quota |
| `trace.py` | What `--trace` prints, and the loop's stop condition |
| `app.py` | The command line, including `wardrobe list/add/edit/remove` |
| `serve.py` | The same agent over HTTP; `/ask` accepts a wardrobe in the request |
| `run_log.py` | One JSON record per run, to `logs/runs.jsonl` (and stdout for HTTP) |
| `criteria.md` | Acceptance criteria: the original project's, then the five capstone (wardrobe) criteria |
| `run_capstone_eval.py` | Tests the capstone criteria |
| `scenarios.py` / `run_eval.py` | The original project's test |
| `measure_cost.py` | Measures tokens and time per run |
| `render.yaml` | Render deployment settings |
| `data/` | 40 listings, the wardrobe schema, and your saved `wardrobe.json` (not committed; delete it to reset to the 10-item demo wardrobe) |
| `utils/data_loader.py` | Loading listings and the demo wardrobe |
| `results/` | Eval run logs, graded |

---

## The two settings people go looking for

Both are at the top of `config.py`.

If your fit cards come out **word-for-word identical** every time, it is one of:

- **`CACHE_ENABLED`** — while you build, identical prompts reuse the answer
  already received. That's deliberate; it makes debugging free. `run_eval.py`
  turns it off automatically.
- **`TEMPERATURE`** — at `0.0` the model gives you the same words every time.
  It ships at `0.9`.

---

## About rate limits

One run makes 2 model calls (3 with a grounding retry), and `generate.py`
keeps to 15 calls a minute, so a few runs back to back can cross the per-minute limit.

`generate.py` handles it:

- **It paces itself** and says when it's waiting. **A pause is the starter
  doing its job, not a bug.**
- **It reuses answers** to prompts already sent, while you build.
- **It stops** if a session makes an unreasonable number of calls, rather than
  draining your day's allowance. For an agent, that usually means a loop isn't
  ending — look for that before raising the number.
- **It counts your calls** and prints the total when you exit.

`config.MAX_ITERATIONS` (12) is the loop's own stop condition. A normal run
never hits it; don't lower it, because the grounding retry needs the room.

---

## When something goes wrong

| What you see | What it means |
|---|---|
| `No GEMINI_API_KEY found` | No `.env`, or the key wasn't pasted in. On Windows check it didn't save as `.env.txt` |
| A message saying the model couldn't be reached | Usually a bad key in `.env` |
| `Couldn't read your saved wardrobe` | `data/wardrobe.json` isn't valid JSON (e.g. hand-edited). Fix it, or delete it to reset to the demo wardrobe |
| `Couldn't build an outfit from only your saved pieces` | The model cited something you don't own twice in a row, so the run stopped rather than show it. Run it again, or add more pieces |
| `Missing: shoes` (or tops/bottoms) under an outfit | Your wardrobe has nothing in that category, so the outfit says what to add instead of inventing it |
| `Not saved:` with a list after `wardrobe add` | The item was refused (blank name, no color, unknown category). Nothing was written; add it again |
| `[rate limit] ... Waiting 34s` | Working as intended. Leave it |
| `[serve] another request is still running` | Also working as intended. `serve.py` answers one request at a time; yours is queued behind one that's mid-run |
| `QuotaGuard: This session has made 300 requests` | A loop isn't ending. Find it before raising the budget |
| `The loop ran 13 times, past MAX_ITERATIONS (12)` | Same thing, caught earlier |
| `The server doesn't offer a tool called '...'` | Nothing registered in `mcp_server.py` yet, or the name doesn't match |
| MCP returns a string where you expected a list | You're not going through `mcp_client.call_tool`, which unwraps it |
| Fit cards identical every run | `CACHE_ENABLED` or `TEMPERATURE`. See above |
| `IncompleteFieldDefinitionWarning: Field 'lifespan'` | Harmless noise from the MCP library's dependencies. Not your code, not an error. Ignore it |
| A price ceiling you typed is being ignored | You used double quotes in PowerShell. `$30` vanished. Use single quotes |
| `UnicodeEncodeError: 'charmap' codec can't encode` | Shouldn't happen — `config.py` sets the console to UTF-8. If you see it, you're running a file that doesn't import `config` |

Still stuck? Send me the full error, the command you ran, and what you expected.

# Running FitFindr

Everything about how the starter works and how to use it.

---

## Before your first class

Setup happens **before class**. The [environment setup page](../pages/ide_setup)
has the per-operating-system commands and the exact versions.

**Same API key you set up in unit 1.** Nothing new to sign up for. There is one
new package — the MCP SDK, for unit 4 — and it installs with everything else.

From inside this repo after you've forked and cloned it:

**macOS / Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env          # then paste your key into .env
python test.py
```

**Windows (PowerShell)**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
copy .env.example .env         # then paste your key into .env
python test.py
```

**You're ready when `python test.py` passes.**

If it doesn't and you've made one honest attempt at the error, post the
**whole** output in the help channel.

> Activate the virtual environment every time you open a new terminal. You
> should see `(.venv)` at the start of your prompt.

---

## Your first five minutes

Start with the data. Your tools will only be as good as your understanding of
what they're reading, and ten minutes here saves an hour of confused debugging.

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

That last one runs the loop. All three tools are stubs, so it will tell you the
loop isn't built yet. **That's the correct starting position** — it runs, and it
does nothing.

---

## Every command

| Command | What it does |
|---|---|
| `python test.py` | Checks your environment. Run it whenever something feels off |
| `python app.py fields` | The fields a listing and a wardrobe item have — **Milestone 1** |
| `python app.py listings` | Browse the data. `--full` for whole records, `-n` for how many |
| `python app.py examples` | Queries worth trying, including one that matches nothing |
| `python app.py ask '...'` | Run the agent on one query — **single quotes** |
| `python app.py ask` | Keep asking until you press Enter on an empty line |
| `python agent.py` | Runs both example paths — one that matches, one that can't |
| `python mcp_server.py` | Starts your MCP server — **unit 4** |
| `python mcp_client.py` | Asks the server what it offers — **unit 4** |
| `python run_eval.py --label before` | Runs every scenario five times and writes the run log — **unit 4** |
| `python serve.py` | Serves the agent over HTTP instead of exiting — **unit 9** |
| `python app.py wardrobe list` | Show your saved wardrobe (`data/wardrobe.json`) — **capstone** |
| `python app.py wardrobe add` | Add an item; prompts for each field and validates it |
| `python app.py wardrobe edit w_003` | Change an item; Enter keeps the current value |
| `python app.py wardrobe remove w_003` | Delete an item (asks first). IDs are never reused |

Useful flags on `ask`:

| Flag | What it does |
|---|---|
| `--trace` | Print the loop step by step, once you've added the trace calls |
| `--empty-wardrobe` | Run as a user with nothing saved — one of unit 4's failure modes |

---

## Which command goes with which milestone

### Unit 3 — the build

| Milestone | What you're doing | Where |
|---|---|---|
| 1 | Read the data, run the starter | `app.py fields`, `app.py listings --full`, `app.py ask` |
| 2 | Spec your three tools | README, **Tool Inventory** |
| 3 | Write your acceptance criteria | `criteria.md` |
| 4 | Build the three tools | `tools.py`, tested one at a time from a terminal |
| 5 | Wire the loop and the state | `agent.py::run_agent` |
| 6 | Write it up | README |

### Unit 4 — the test

| Milestone | What you're doing | Where |
|---|---|---|
| 1 | Move one tool onto MCP | `mcp_server.py`, then `mcp_client.call_tool` in `run_agent` |
| 2 | Break it on purpose, then trace it | `trace.py`, `app.py ask --trace` |
| 3 | Run your test | `scenarios.py`, then `run_eval.py --label before` |
| 4 | Call each criterion, diagnose the misses | README |
| 5 | Fix one thing and re-run | `run_eval.py --label after` |
| 6 | Say what's still broken | README |

---

## Running it somewhere else — **unit 9**

Everything above exits when the command finishes. A host has nothing to keep
running, so before you can deploy this you need something that stays up.
`serve.py` is that: the same `run_agent()`, behind two HTTP routes.

On your machine:

```bash
python serve.py
curl -X POST http://localhost:5000/ask \
  -H 'Content-Type: application/json' \
  -d '{"query": "vintage graphic tee under $30"}'
```

On a host, the start command is:

```bash
gunicorn serve:app
```

| Thing | What it means |
|---|---|
| `PORT` | The host tells your app which port to listen on by setting this. Both `serve.py` and `gunicorn` read it, and `serve.py` falls back to `5000` on your machine. Don't hard-code a port |
| `POST /ask` | `{"query": "...", "wardrobe": {...}}` — wardrobe optional. Returns the session dict, `error` and all |
| `GET /health` | Says `ok` if the app is awake |
| It answers one request at a time | On purpose. A second request waits for the first to finish, and prints `[serve] another request is still running` while it waits. An MCP tool call starts a whole second Python process, and the free tier's 512 MB has no room for two of those at once — and `generate.py`'s rate-limit counting assumes one caller. The reasoning is written out in `serve.py` |
| `gunicorn serve:app`, exactly | Not `-k gevent`, not `-k eventlet`, not wrapped for uvicorn. `mcp_client.call_tool` uses `asyncio.run()`, which won't start inside a running event loop, so an async worker breaks **every** MCP call — and only once you've deployed it |
| The first request is slow | The free tier puts your app to sleep after about fifteen minutes of nothing. The next request wakes it up and waits for it — around a minute. Not a bug, and worth knowing before you demo it |

`serve.py` ships with **no logging and no timing in it**, on purpose. You add
that yourself in the follow-along, before you deploy — instrumenting first is
the point of the session.

---

## Deployed on Render — **capstone**

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
4. **Apply.** The first build takes a few minutes. When the log says the
   service is live, check it:

```bash
curl https://fitfindr-ppek.onrender.com/health
```

Every push to `main` redeploys automatically.

### What `render.yaml` sets, and why

| Setting | Why |
|---|---|
| `pip install -r requirements.txt` | Same pinned packages as local |
| `gunicorn serve:app --timeout 120` | The default **sync** worker (an async one breaks every MCP call — see the table above). The timeout is raised from gunicorn's 30 s because one `/ask` makes 2–3 model calls and starts the MCP server twice: 5–19 s locally, slower on the free CPU, longer with a grounding retry or a rate-limit wait |
| `healthCheckPath: /health` | Render pings it before sending traffic and after each deploy |
| `PYTHON_VERSION = 3.13` | `requirements.txt` supports 3.11–3.13, not 3.14. If the build log says the version isn't found, set the full version (e.g. `3.13.5`) |
| `GEMINI_API_KEY` | The only secret. Set in the dashboard, never committed |

### Asking it something

With the **demo wardrobe** (what `data/wardrobe.json` reseeds to):

```bash
curl -X POST https://fitfindr-ppek.onrender.com/ask \
  -H 'Content-Type: application/json' \
  -d '{"query": "vintage graphic tee under $30"}'
```

With **your own wardrobe**, sent with the request. Nothing is stored; it's
checked with the same rules as `app.py wardrobe add` (IDs like `w_001`, one of
five categories, at least one color, at most 50 items):

```bash
curl -X POST https://fitfindr-ppek.onrender.com/ask \
  -H 'Content-Type: application/json' \
  -d '{"query": "denim jacket under $50", "wardrobe": {"items": [
        {"id": "w_001", "name": "Cream cable-knit sweater", "category": "tops", "colors": ["cream"], "style_tags": ["cozy"]},
        {"id": "w_002", "name": "Black straight-leg trousers", "category": "bottoms", "colors": ["black"], "style_tags": []},
        {"id": "w_003", "name": "Brown suede loafers", "category": "shoes", "colors": ["brown"], "style_tags": []}]}}'
```

An invalid wardrobe comes back as `400` with a `problems` list naming each
item's mistakes, instead of reaching the agent.

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

Read them back:

```bash
python -c "import json; [print(r['ts'], r['status'], r['duration_ms'], r.get('model_calls')) for r in map(json.loads, open('logs/runs.jsonl', encoding='utf-8'))]"
```

`logs/` is in `.gitignore`: the records are runtime output. Copy the entries
you need into the README.

---

## Where everything lives

| File | What it does |
|---|---|
| `config.py` | Every setting worth changing — **TEMPERATURE and the cache are at the top** |
| `tools.py` | Your three tools. **Stubs — you build these** |
| `agent.py` | The planning loop and the session. **Stub — you build this** |
| `generate.py` | The only thing that calls out to a service. Handles pacing and quota |
| `trace.py` | The trace helper, and the loop's stop condition |
| `app.py` | The command line |
| `serve.py` | The same agent over HTTP, for deploying — **unit 9** |
| `mcp_server.py` | Your MCP server — **unit 4, you register the tool** |
| `mcp_client.py` | Calling an MCP tool from your agent. Given to you |
| `scenarios.py` | What your test runs. **You fill this in** |
| `run_eval.py` | Runs the scenarios repeatedly and writes the run log |
| `criteria.md` | Your five acceptance criteria. **You fill this in** |
| `data/` | 40 listings and the wardrobe schema |
| `utils/data_loader.py` | Loading the data. Use this rather than reading the files yourself |
| `results/` | Run logs. **Commit these** — they're your evidence |

---

## The two settings people go looking for

Both are at the top of `config.py`, and the brief points at them by name.

If your fit cards come out **word-for-word identical** every time, it is one of:

- **`CACHE_ENABLED`** — while you build, identical prompts reuse the answer
  already received. That's deliberate; it makes debugging free. `run_eval.py`
  turns it off automatically.
- **`TEMPERATURE`** — at `0.0` the model gives you the same words every time.
  It ships at `0.9`.

---

## About rate limits

**This is the heaviest pair in the course for call volume.** Two of your three
tools call the model, so one agent run is several requests, and a few runs back
to back while debugging can cross the per-minute limit.

`generate.py` handles it:

- **It paces itself** and says when it's waiting. **A pause is the starter
  doing its job, not a bug.**
- **It reuses answers** to prompts already sent, while you build.
- **It stops** if a session makes an unreasonable number of calls, rather than
  draining your day's allowance. For an agent, that usually means a loop isn't
  ending — look for that before raising the number.
- **It counts your calls** and prints the total when you exit.

`config.MAX_ITERATIONS` is the loop's own stop condition. Your loop this unit
is short enough that you may never hit it. Keep it — a missing stop condition
is the most common architectural failure in production agents.

---

## When something goes wrong

| What you see | What it means |
|---|---|
| `The planning loop isn't built yet` | Correct, at the start. That's the TODO in `agent.py` |
| `No GEMINI_API_KEY found` | No `.env`, or the key wasn't pasted in. On Windows check it didn't save as `.env.txt` |
| A message saying the model couldn't be reached | Usually a bad key. This is also **exactly what unit 4 Milestone 2 asks you to trigger on purpose** |
| `[rate limit] ... Waiting 34s` | Working as intended. Leave it |
| `[serve] another request is still running` | Also working as intended. `serve.py` answers one request at a time; yours is queued behind one that's mid-run |
| `QuotaGuard: This session has made 300 requests` | A loop isn't ending. Find it before raising the budget |
| `The loop ran 11 times, past MAX_ITERATIONS` | Same thing, caught earlier |
| `The server doesn't offer a tool called '...'` | Nothing registered in `mcp_server.py` yet, or the name doesn't match |
| MCP returns a string where you expected a list | You're not going through `mcp_client.call_tool`, which unwraps it |
| Fit cards identical every run | `CACHE_ENABLED` or `TEMPERATURE`. See above |
| `--trace` prints nothing | You haven't added `trace.step()` calls yet — unit 4, Milestone 2 |
| `IncompleteFieldDefinitionWarning: Field 'lifespan'` | Harmless noise from the MCP library's dependencies. Not your code, not an error. Ignore it |
| A price ceiling you typed is being ignored | You used double quotes in PowerShell. `$30` vanished. Use single quotes |
| `UnicodeEncodeError: 'charmap' codec can't encode` | Shouldn't happen — `config.py` sets the console to UTF-8. If you see it, you're running a file that doesn't import `config` |

Still stuck after one honest attempt? Post in the help channel with the full
error, what you ran, and what you expected.

---

## A note on committing

At least four new commits in unit 3, at least four more in unit 4. Your commit
history is what shows your criteria existed before your results did.

**Do not delete and recreate this repository.** You submit the same URL both
units.

`results/` is deliberately **not** in `.gitignore`.

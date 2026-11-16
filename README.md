# FitFindr

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first** — setup, every
> command, and what to do when something breaks.
>
> Once `python test.py` passes:
>
> ```bash
> python app.py listings --full -n 6      # read the data (Milestone 1)
> python app.py fields                    # what you can filter on
> python app.py ask 'vintage graphic tee under $30'
> ```
>
> All three tools are stubs, so that last command will do nothing useful yet.
> That's the starting position.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     HOW TO USE THIS FILE

     This is your submission. Fill each section in as you finish the milestone
     it belongs to — don't leave it all to the end.

     Unit 3 asks for the first five sections. Unit 4 adds the five below them.
     Leave the unit 4 sections alone until then; they're here so you know
     what's coming.

     Everything is pasted as TEXT. No screenshots, no images, no video links.
     A typed block of output gets full credit; a picture of the same output
     gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 3 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- Three or four sentences: what a user asks for, and what they get back. -->



---

## Tool Inventory

<!-- Four lines per tool. This is worth 2 points and it's the single most
     common place students lose them.

     "Returns a list" earns NOTHING. The description has to say what is IN
     the list.

     The empty case isn't optional either — it's the thing your loop branches
     on, and if you don't decide it here you'll discover it as a crash in
     Milestone 5. -->

### `search_listings`

- **What it does:** It searches the listings file and returns items that match the query given by the user. As for size matching, sizes match on whole tokens such that M matches S/M but L doesn't match XL. "One Size" listings only match when no size is given or when the user specifies "One Size". 
- **Inputs:** `description` (string), `size` (string or None), and `max_price` (float or None)<!-- name and type each: `max_price` (float), not "a price" -->
- **Returns:** It returns a list of clothing items, where each item is a listing dict that has an id, title, description, category, style_tags, size, condition, price, colors, brand, and platform. The list is contains at most 10 items ordered from the best match first(highest score) to items that have a lower match value. 
- **When it has nothing:**  It returns an empty list.

### `suggest_outfit`

- **What it does:** It takes in a new clothing item and a group of other clothing items the user already has, and returns groupings of clothing items as outfit ideas.
- **Inputs:** `new_item` (dict), `wardrobe` (dict), and `missing_categories` (list of strings or None, the core categories the wardrobe can't supply; defaults to None)
- **Returns:** It returns a string with one or two outfits. Each outfit has an `Outfit N:` name line, a `- NEW: <listing title>` line, one `- w_NNN: <name>` line per saved piece (only pieces from the wardrobe, cited by ID), and a `Vibe:` line. When `missing_categories` isn't empty, it leaves those slots out and ends with a `Missing: <categories>` line.
- **When it has nothing:** It returns general styling advice. This happens when the wardrobe list is empty.

### `create_fit_card`

- **What it does:** It takes in an outfit and a new outfit item and returns a caption someone would post.
- **Inputs:** `outfit` (string), `new_item` (dict)
- **Returns:** It returns a 2-4 sentence string that someone would post as a caption with the outfit and new item. It mentions the clothing type, color, a style tag, material, or the combination of pieces.
- **When it has nothing:** It returns an error string explaining that a caption wasn't successfully created.This happens when outfit is empty or only whitespace, and a message is returned without calling the model.

### ADDITIONAL/Stretch Feature `find_similar`

- **What it does:** It takes in an item and returns listings for similar clothing items that match the aesthetic, or style tags.
- **Inputs:** `item` (dict)
- **Returns:** It returns a list of dicts where each dict is a listing dict that has an id, title, description, category, style_tags, size, condition, price, colors, brand, and platform. The list is ranked by shared style tags, then the same category and shared colors.
- **When it has nothing:** It returns an empty list.

### Capstone `get_wardrobe`

- **What it does:** It reads the user's saved wardrobe from `data/wardrobe.json`, either all of it or only one category. It doesn't call the model.
- **Inputs:** `category` (string or None): one of tops, bottoms, outerwear, shoes, accessories, case-insensitive. None or "" means every category.
- **Returns:** It returns a wardrobe dict `{"items": [...]}`, the same shape `suggest_outfit` takes. Each item has an id (`w_NNN`), name, category, colors, style_tags, and notes (string or None), in saved order. Storage fields (`next_id`, `user_id`) are left out.
- **When it has nothing:** It returns `{"items": []}` when nothing is saved, or nothing is saved in that category. An unknown category raises `ValueError` instead, so a typo isn't mistaken for an empty category.

---

## Planning Loop

<!-- Your branch rule, stated as a rule — the condition AND both paths — plus
     the file and function that holds it.

     Like this:
       "If search_listings returns an empty list, put a message in the session
        and stop. Otherwise take the first result and go to suggest_outfit."
        — agent.py::run_agent

     The grader checks your code against what you claim here, so the file and
     function have to be real. -->

**Branch rule:** If search_listings returns an empty list, put a message in session["error"] that says which filters to loosen (price, size, or wording) and return the session without calling suggest_outfit. Otherwise take the first result as selected_item and go on to suggest_outfit, then create_fit_card.

**Where it lives:** `agent.py::run_agent`

**How the query is parsed:** <!-- regex, string splitting, or asking the model — say which -->
Regex is used to pull out a price pattern wherever "under", "below", "up to" or "$" appear, a size wherever "size" appears, and whatever's left becomes description. 

**What moves through the session:** <!-- which fields, in what order -->
query -> parsed (description, size, max_price) -> searched + search_results -> selected_item -> outfit_suggestion -> fit_card, or error if the run stops at the branch.

---

## Sample Run

<!-- Two things go here.

     1. One FULL query and its output, pasted as text.
     2. Your three per-tool terminal tests — the command and what it printed. -->

**One full query**

```
$ python app.py ask 'black boots under $200'

```

**The three tools, tested one at a time**

```
$ python -c "from tools import search_listings; print(search_listings('graphic tee', max_price=30))"

[{'id': 'lst_006', 'title': 'Graphic Tee — 2003 Tour Bootleg Style', 'description': 'Vintage-style bootleg tee with faded graphic. Slightly boxy fit. 100% cotton, soft and worn-in.', 'category': 'tops', 'style_tags': ['graphic tee', 'vintage', 'grunge', 'streetwear', 'band tee'], 'size': 'L', 'condition': 'good', 'price': 24.0, 'colors': ['black'], 'brand': None, 'platform': 'depop'}, {'id': 'lst_002', 'title': 'Y2K Baby Tee — Butterfly Print', 'description': 'Super cute early 2000s baby tee with butterfly graphic. Fitted crop length. Tag says medium but fits like a small.', 'category': 'tops', 'style_tags': ['y2k', 'vintage', 'graphic tee', 'cottagecore'], 'size': 'S/M', 'condition': 'excellent', 'price': 18.0, 'colors': ['white', 'pink', 'purple'], 'brand': None, 'platform': 'depop'}, {'id': 'lst_033', 'title': 'Vintage Band Tee — Faded Grey', 'description': 'Faded grey band-style tee with distressed graphic. Crew neck. Fits boxy. Well-loved but no holes or major damage.', 'category': 'tops', 'style_tags': ['vintage', 'grunge', 'band tee', 'graphic tee', 'streetwear'], 'size': 'L', 'condition': 'fair', 'price': 19.0, 'colors': ['grey', 'charcoal'], 'brand': None, 'platform': 'depop'}, {'id': 'lst_015', 'title': 'Vintage Graphic Hoodie — Faded Black', 'description': 'Faded black pullover hoodie with barely-visible vintage graphic on the chest. Cozy interior. Some pilling but adds to the worn-in look.', 'category': 'tops', 'style_tags': ['vintage', 'grunge', 'graphic', 'streetwear'], 'size': 'L', 'condition': 'fair', 'price': 26.0, 'colors': ['black', 'charcoal'], 'brand': None, 'platform': 'depop'}, {'id': 'lst_017', 'title': 'Mesh Long-Sleeve Top — Black', 'description': 'Sheer black mesh long-sleeve. Great for layering under a graphic tee or over a bralette. Stretchy material, fits true to size.', 'category': 'tops', 'style_tags': ['y2k', 'grunge', 'goth', 'layering'], 'size': 'S/M', 'condition': 'excellent', 'price': 15.0, 'colors': ['black'], 'brand': None, 'platform': 'depop'}, {'id': 'lst_011', 'title': 'Low-Rise Cargo Pants — Khaki', 'description': 'Y2K era low-rise cargo pants. Lots of pockets. Khaki color, slightly distressed at the hems. Great for layering with a long tee.', 'category': 'bottoms', 'style_tags': ['y2k', 'cargo', '2000s', 'streetwear'], 'size': 'W29', 'condition': 'fair', 'price': 27.0, 'colors': ['khaki', 'tan'], 'brand': None, 'platform': 'poshmark'}, {'id': 'lst_012', 'title': 'Oversized Crewneck Sweatshirt — Vintage Navy', 'description': 'Perfectly faded navy crewneck. Genuinely vintage — not manufactured distressed. Ribbed cuffs and hem. No graphics, clean.', 'category': 'tops', 'style_tags': ['vintage', 'basics', 'oversized', 'classic'], 'size': 'XL (fits oversized)', 'condition': 'good', 'price': 20.0, 'colors': ['navy'], 'brand': None, 'platform': 'thredUp'}]

```


```
$ python -c "from tools import suggest_outfit; from utils.data_loader import get_example_wardrobe, load_listings; print(suggest_outfit(load_listings()[0], get_example_wardrobe()))"

**Outfit 1: Effortless Streetwear**
Pair the Vintage Levi's 501 Jeans with the White ribbed tank top, Black cropped zip hoodie, and Chunky white sneakers. Add the Black crossbody bag.
*Vibe:* Casual, 90s-inspired off-duty cool.

**Outfit 2: Grungy Contrast**
Pair the Vintage Levi's 501 Jeans with the Oversized grey crewneck sweatshirt, Brown leather belt, and Black combat boots. Throw on the Vintage black denim jacket over top.
*Vibe:* Edgy, thrifted-chic with cozy oversized proportions.

```

```
$ python -c "from tools import create_fit_card; from utils.data_loader import load_listings; print(create_fit_card('jeans and white sneakers', load_listings()[0]))"

Scored these vintage Levi's 501 jeans for just $38 on depop, and the medium wash with that light knee fading is literally unmatched. Paired them with crisp white sneakers for that effortless, classic streetwear look. Honestly never taking these off.

```

```
$ python -c "from tools import create_fit_card; from utils.data_loader import load_listings; print(create_fit_card('jeans and white sneakers', load_listings()[0]))"

Scored these vintage Levi's 501 jeans for just $38 on depop, and the medium wash with that light knee fading is literally unmatched. Paired them with crisp white sneakers for that effortless, classic streetwear look. Honestly never taking these off.
```

```
$ python -c "from tools import find_similar; from utils.data_loader import load_listings; [print(l['id'], l['title']) for l in find_similar(load_listings()[0])]"

lst_007 Denim Jacket — Light Wash, Cropped
lst_016 High-Waisted Denim Shorts — Cutoff
lst_037 Straight Leg Black Jeans — Faded
lst_031 Baggy Carpenter Jeans — Dark Wash
lst_021 Straight Leg Khaki Trousers — Olive
lst_003 Oversized Flannel Shirt — Plaid Red/Black
lst_004 90s Track Jacket — Navy/White Stripe
lst_006 Graphic Tee — 2003 Tour Bootleg Style
lst_010 Vintage Windbreaker — Color Block Purple/Teal
lst_012 Oversized Crewneck Sweatshirt — Vintage Navy

```

---

## How I Used AI
<!-- Two specific moments. What you asked, what came back, what you changed.

     "I used Claude to help me code" is not enough.

     "I gave Claude my search_listings spec. It returned None on no match
     instead of an empty list, so I changed it" is the level we want. -->

**Moment 1**

- *What I asked for:* I asked for Claude to implement the four tools built from my Tool Inventory and the tools.py docstrings, with a plan before any code was written.
- *What came back:* It returned a plan that pointed out my README disagreed with tools.py in two places. create_fit_card's outfit input as list[dict], but agent.py passes the string from suggest_outfit. I'd said suggest_outfit returns an error string on an empty wardrobe, but the docstring says it should give general styling advice. It also asked how "One Size" listings should match.
- *What I changed:* I rewrote the Tool Inventory to match the code: string input, styling advice for an empty wardrobe, and the whole-token size rule. I decided "One Size" listings only match when no size is given, so a request for a small top doesn't return bags and hats. The code was built according to that specification.

**Moment 2**

- *What I asked for:* I asked for a plan for run_agent before implementation.
- *What came back:* Claude gave two options. The first was a step loop that reads the session each pass to pick the next tool. The other was a straight-line version with an if empty: return. It also asked whether to add the unit 4 trace and error handling now, and whether "size medium" should become M. After I chose, Claude implemented the loop, the regex query parser and the no-results message.
- *What I changed:* I chose the step loop so the branch is a real decision based on state. I held back the additions Claude would make for unit 4 and asked for size words to be converted, then checked the result by comparing session["selected_item"] to the object that reached suggest_outfit. 

**Moment 3**
- *What I asked for:* I asked for Claude to look at my "before" criterion table grading and see if my grading was accurate according to the criteria I set up in unit 3. I told it that I suspected that my fifth criterion was too harsh and I wanted to know if it really did fail it (the criterion specifying that all outfit pieces must share a style tag).
- *What came back:* Claude suggested that I actually missed criterion 5 completely like I suspected, and pointed out that my criterion caused good outfits to "fail". It confirmed that my criterion was indeed broken and suggested fixes to improve it. It also pointed out that for criterion 4, I didn't test it correctly since I specified that the fits must be accurate for 5 different selected items, although the scenarios.py only tests with one item. 
- *What I changed:*
I improved criterion 5 in the criteria.md file and made the necessary changes to scenarios.py to add enough outfits so that criterion 4 could be properly assessed.

**Moment 4**
- *What I asked for:* I asked Claude if it made sense for me to list a specific mechanism responsible for criterion 5's failure although the problem was the criterion itself.
- *What came back:* Claude explained that although the criterion was flawed, the reason the system didn't pass the criterion specifically had to do with the model building complementary outfits, which don't always have pieces with the same style tags.
- *What I changed:* 
I used the advice to properly document why Criterion 5 was missed in the Diagnoses section, along with the responsible mechanism and how I revised the criterion as well.

**Moment 5**
- *What I asked for:* I asked Claude to fill in the run log tables and fix the wording and evidence in my unit 4 sections.
- *What came back:* Claude wrote parts of my unit 4 README: the Run Log notes and tables, the "Real output" block (copied from my results files), and wording and evidence fixes in The Improvement and What's Still Broken. 
- *What I changed:* The before-table grading, the criterion 5 revision, the diagnoses, and the choice of fix are mine. Claude proposed the criterion 4 scoring rule and scored the after table; I checked its counts against the run logs.

<!-- ═══════════════════════ UNIT 4 — THE TEST ═══════════════════════

     Don't fill these in during unit 3.
     ═══════════════════════════════════════════════════════════════════ -->

---

## Run Log — Before

<!-- Five criteria, five tries each, in this exact format.

     Five, because your criteria are written out of five. Mark each try PASS
     or FAIL, count the passes, and read that count against your target — a
     row targeting 4 of 5 with three PASS cells is MISSED (3/5).

     `python run_eval.py --label before` runs everything and writes the table
     into results/. Paste it here and fill in the verdicts. -->

| Criterion | Target | Try 1 | Try 2 | Try 3 | Try 4 | Try 5 | Verdict |
|---|---|---|---|---|---|---|---|
| 1.  Matching query completes all 3 tool calls | 4/5 | PASS | PASS | PASS | PASS | PASS | MET (5/5) |
| 2.  Impossible query stops early | 5/5 | PASS | PASS | PASS | PASS | PASS | MET (5/5) |
| 3.  Matching search item reaches suggest outfit | 5/5 | PASS | PASS | PASS | PASS | PASS | MET (5/5) |
| 4.  Fit cards are accurate | 4/5 | PASS | PASS | PASS | PASS | PASS | MET (5/5) |
| 5.  Suggested outfit pieces match | 5/5 | FAIL | FAIL | FAIL | FAIL | FAIL | MISSED (0/5) |

All rows are scored from `results/run_2026-10-10_1818_before.md`. Criteria 1, 3 and 5 use the five tries of the `vintage graphic tee under $30` scenario; criterion 2 uses the five tries of `designer ballgown size XXS under $5`. For criterion 4, Try N is the Try 1 fit card of item N (track jacket, silk slip dress, platform sneakers, graphic tee, denim jacket), a rule chosen before reading the cards. Criterion 5 is scored against the original wording of the criterion; against the revised criterion in `criteria.md`, the same five tries pass 5/5.

**Real output from one try**, pasted as text, naming the file and function
that produced it:

All output below is copied from `results/run_2026-10-10_1818_before.md`, written by `run_eval.py::main`, which calls `agent.py::run_agent` once per try.

**Criterion 1: matching query completes** (`vintage graphic tee under $30`, Try 1). Fit card produced by `tools.py::create_fit_card`, called from `agent.py::run_agent`; trace lines recorded by `trace.py::step`.

```
- stopped early: no
- selected_item: Graphic Tee — 2003 Tour Bootleg Style ($24.0, depop)
- search_results: 10

Fit card:
Found this ridiculously soft 2003 tour bootleg tee on depop for $24 and haven't taken it off since. It's got that perfect faded graphic and boxy fit, so I’ve been living in it layered over a white ribbed tank with wide-leg khaki trousers and chunky white sneakers. Gives off the best effortless streetwear energy without even trying.

[1] search_listings
      in:  dict with keys: description, size, max_price
      out: 10 items: Graphic Tee — 2003 Tour Bootleg Style, Vintage Band Tee — Faded Grey, Y2K Baby Tee — Butterfly Print … +7 more
[2] suggest_outfit
      in:  dict with keys: selected_item, wardrobe
      out: Outfit 1: Effortless Grunge Pair the Graphic Tee with the Baggy straight-leg jeans, dark wash. Tuck in the tee…
[3] create_fit_card
      in:  dict with keys: outfit_suggestion, selected_item
      out: Found this ridiculously soft 2003 tour bootleg tee on depop for $24 and haven't taken it off since. It's got t…
```

**Criterion 2: impossible query stops early** (`designer ballgown size XXS under $5`, Try 1). Error message produced by `agent.py::_no_results_message`, set at the branch in `agent.py::run_agent`.

```
- stopped early: yes — No listings matched "designer ballgown" in size XXS under $5. Try raising or removing the $5 price limit, dropping the size, or using fewer or broader words (just the item type, like "jacket" or "jeans").
- selected_item: (none)
- search_results: 0

[1] search_listings
      in:  dict with keys: description, size, max_price
      out: [] (empty)
```

**Criterion 3: search item reaches suggest_outfit** (`vintage graphic tee under $30`, Try 1). Search results from `mcp_server.py::search_listings` (wrapping `tools.py::search_listings`); `selected_item` set in `agent.py::run_agent`.

```
[1] search_listings
      in:  dict with keys: description, size, max_price
      out: 10 items: Graphic Tee — 2003 Tour Bootleg Style, Vintage Band Tee — Faded Grey, Y2K Baby Tee — Butterfly Print … +7 more

- selected_item: Graphic Tee — 2003 Tour Bootleg Style ($24.0, depop)

[2] suggest_outfit
      in:  dict with keys: selected_item, wardrobe
      out: Outfit 1: Effortless Grunge Pair the Graphic Tee with the Baggy straight-leg jeans, dark wash. Tuck in the tee…
```

**Criterion 4: fit cards are accurate** (`90s track jacket in size M`, Try 1, the first of the five items). Fit card produced by `tools.py::create_fit_card`.

```
- selected_item: 90s Track Jacket — Navy/White Stripe ($45.0, poshmark)

Fit card:
Found this vintage Champion 90s track jacket on Poshmark for just $45, and it’s basically lived on my shoulders ever since. Today I’m leaning into skater-off-duty energy by throwing it over a white ribbed tank with baggy straight-leg jeans and chunky white sneakers. The navy and white sleeve stripes just pull the whole effortless streetwear look together.
```

**Criterion 5: suggested outfit pieces match** (`vintage graphic tee under $30`, Try 1). Outfit suggestion produced by `tools.py::suggest_outfit`.

```
Outfit 1: Effortless Grunge
Pair the Graphic Tee with the Baggy straight-leg jeans, dark wash. Tuck in the tee and add the Black combat boots and Black crossbody bag.
Vibe: 90s skater streetwear, perfectly worn-in and casual.

Outfit 2: Layered Streetwear
Wear the Graphic Tee over the White ribbed tank top, paired with the Wide-leg khaki trousers. Cinch the waist with the Brown leather belt, and finish with the Chunky white sneakers and Black crossbody bag.
Vibe: Elevated urban minimal with a vintage edge.
```

---

## Verdicts and Diagnoses

<!-- MET or MISSED per criterion against LAST UNIT's target, plus a sentence on
     how you decided.

     Then, for every miss: which of the four places it happened — a tool, the
     loop's branch, the session, or the model's output — AND the mechanism.

     Not a diagnosis:  "The fit card was bad."
     A diagnosis:      "The fit card criterion missed on 2 of 5 items. Both had
                        an empty brand field. My prompt puts the brand in the
                        first sentence, so the card opened with a blank and read
                        like a fragment. The tool worked; the prompt assumed a
                        field that isn't always there."

     Look for a pattern. Three misses on the same tool is one problem, not
     three. -->

| # | Criterion | Target | Verdict | How I decided |
|---|---|---|---|---|
| 1 | Matching query completes all 3 tool calls | 4/5 | MET (5/5) | In the output, I saw the traces for all 3 tools, so I know that all three tools were completed. |
| 2 | Impossible query stops early | 5/5 | MET (5/5) | The trace stopped at the first tool, so I know that the system correctly stops when an impossible query is given. |
| 3 | Matching search item reaches suggest outfit | 5/5 | MET (5/5) | The search_listings trace shows that the out item is the same as the `selected_item`, and then the following suggest_outfit trace shows that selected_item is its input, so the session picked the same item. |
| 4 | Fit cards are accurate | 4/5 | MET (5/5) | The fit card successfully mentions a detail about the selected item, with the example run pasted above mentioning the jacket's navy and white sleeve stripes. |
| 5 | Suggested outfit pieces match | 5/5 | MISSED (0/5) | When searching the example wardrobe for the listed outfit pieces in the suggested outfit string, the pieces don't share any of the same style tags the original searched item contained. |

**Diagnoses**

Criterion 5 Diagnosis: The suggest_outfit criterion didn't pass for any of the runs. None of the listed pieces when searched in wardrobe_schema.json contained the same style tags as the originally searched item. The failure happened at the model's output since the text suggest_outfit got back from the model was what failed the check. The failed step was suggest_outfit and the failed mechanism was that nothing in the prompt specifies that returned outfit suggestion's pieces should share tags. In all 5 tries, Outfit 1 includes the Black crossbody bag (minimal, accessories, everyday), which shares no tag with Graphic Tee (graphic tee, vintage, grunge, streetwear, band tee). Outfit 2 uses khaki trousers and brown leather belt, which don't share any either. The outfits themselves are reasonable, so the criterion was checking the wrong property. I revised it in criteria rather than forcing tag matching into the prompt, which could make worse outfits or limit the possible outfits returned. 


---

## Loop Trace

**Happy path**

```
python app.py ask 'jean jacket size m under $60' --trace

[1] search_listings
      in:  dict with keys: description, size, max_price
      out: 2 items: 90s Track Jacket — Navy/White Stripe, Shacket — Olive Canvas
[2] suggest_outfit
      in:  dict with keys: selected_item, wardrobe
      out: Outfit 1: Retro Streetwear Pair the 90s Track Jacket with the white ribbed tank top and baggy straight-leg jea…
[3] create_fit_card
      in:  dict with keys: outfit_suggestion, selected_item
      out: Found this vintage Champion track jacket for $45 on Poshmark and I’m obsessed with the navy and white sleeve s…

  Found:    90s Track Jacket — Navy/White Stripe — $45.0 on poshmark

  Outfit:   Outfit 1: Retro Streetwear
Pair the 90s Track Jacket with the white ribbed tank top and baggy straight-leg jeans, dark wash. Finish withthe chunky white sneakers and black crossbody bag. 
Vibe: Effortless 90s skater-off-duty.

Outfit 2: High-Low Sporty
Layer the 90s Track Jacket over the white ribbed tank top, and pair with the wide-leg khaki trousers, securedwith the brown leather belt. Step into the chunky white sneakers and carry the black crossbody bag. 
Vibe: Elevated athletic casual with a vintage prep twist.

  Fit card: Found this vintage Champion track jacket for $45 on Poshmark and I’m obsessed with the navy and white sleeve stripes. I threw it on over a ribbed tank with baggy dark wash jeans and chunky sneakers for that effortless skater-off-duty vibe. Honestly the easiest throw-on-and-go piece for chilly mornings.

0 model calls this session, 2 served from cache

```

**Empty search**

```
python app.py ask 'Hyundai Sonata' --trace
[1] search_listings
      in:  dict with keys: description, size, max_price
      out: [] (empty)

  No listings matched "Hyundai Sonata". Try using fewer or broader words (just the item type, like "jacket" or "jeans").

0 model calls this session

```

**On the MCP move:** <!-- what changed in your code, and whether anything
behaved differently afterwards. If the rewire didn't work, say exactly where it
broke — the error text and the last thing that worked. That earns the point in
full. -->

The agent.py file now uses mcp_client.call_tool() during a session to use the search_listings() function rather than calling it directly. Everything behaved the same afterwards.



---

## The Improvement

A small problem I noticed was that the create_fit_card function seemed to output descriptions that would sometimes fabricate additional details about wardrobe items. For example, when making an outfit with the vintage t shirt, it paired it with a denim jacket and described the jacket as "oversized" when its wardrobe notes describe it as "slightly cropped". The two descriptions are contradictory and show that the model added on untrue wording describing the jacket. This came from `results/run_2026-10-10_1601_before.md` (the `vintage graphic tee under $30` scenario, Try 1), where the fit card read: "…I threw it on with baggy dark-wash denim, combat boots, and an oversized black denim jacket for peak 90s grunge." The `results/run_2026-10-10_1818_before.md` run had similar additions, like "heavy black denim jacket", "heavy grey crewneck sweatshirt", and "chunky combat boots", none of which appear in the wardrobe data.
<!-- What you changed, why your diagnosis pointed at it, and the after-run in
     the same table format. One change, measured properly.

     `python run_eval.py --label after` -->

**What I changed:**
I changed the system prompt behind the create_fit_card function to instruct the model to only describe wardrobe pieces with wording used in the actual outfit text, and to describe the thrifted item using its listing details. 

**Which failure it was meant to fix:**
The change was meant to fix a criterion 4 failure, although criterion 4 still met its target overall. The problem showed up on individual fit cards rather than the verdict, since the model generated fit cards with fabricated details about wardrobe pieces.

### Run Log — After

| Criterion | Target | Try 1 | Try 2 | Try 3 | Try 4 | Try 5 | Verdict |
|---|---|---|---|---|---|---|---|
| 1.  Matching query completes all 3 tool calls | 4/5 | PASS | PASS | PASS | PASS | PASS | MET (5/5) |
| 2.  Impossible query stops early | 5/5 | PASS | PASS | PASS | PASS | PASS | MET (5/5) |
| 3.  Matching search item reaches suggest outfit | 5/5 | PASS | PASS | PASS | PASS | PASS | MET (5/5) |
| 4.  Fit cards are accurate | 4/5 | PASS | PASS | PASS | PASS | PASS | MET (5/5) |
| 5.  Suggested outfit pieces match | 5/5 | FAIL | FAIL | FAIL | FAIL | FAIL | MISSED (0/5) |

All rows are scored from `results/run_2026-10-11_0116_after~.md`, using the same scenarios and rules as Run Log — Before. Criteria 1, 3 and 5 use the five tries of `vintage graphic tee under $30`; criterion 2 uses the five tries of `designer ballgown size XXS under $5`. For criterion 4, Try N is the Try 1 fit card of item N (track jacket, silk slip dress, platform sneakers, graphic tee, denim jacket). Criterion 5 is scored against the original wording; against the revised criterion in `criteria.md`, the same five tries pass 5/5.

**Did it help, and how do I know:**

It removed the invented wardrobe details since before 4 of 25 cards had invented details and 0 of 25 had invented details after, but also introduced a new problem: 17 of the 35 generated cards now show prices like "$24.0" and read more like listings when initially 0 of 35 did, which was the opposite of what a fit card was supposed to achieve. This is one run on each side, and all 4 "before" cases were on the silk slip dress, so some of the drop could be chance.

<!-- If it made things worse, say that. Honestly reported, that earns full
     credit and is more interesting than one that worked. -->



---

## What's Still Broken
Criterion 5 is still missed against the original wording. I didn't change the tool because I realized that my wording in the original criterion would encourage the model to possibly make worse outfits if I enforced the wording into the prompt to generate outfits where all the pieces have matching tags. I revised the criterion in `criteria.md` instead, and the revised version passes 5/5 in both runs.


What is still broken is the function that creates fit cards, since the fix I tried to make changed the fit cards such that they seem more like listings rather than captions ("$24.0" instead of "$24"). To fix it, I'd have to format the price as $24 in _describe_item, soften "using its listing details", then run the eval again and recount. I stopped after one change because that's the only way to tell which change caused which result: I know the prompt change caused both the improvement and the regression because it was the only thing that changed between the two runs. Another fix would need its own before and after run.

<!-- For each criterion still missed: what you'd do, and why you stopped where
     you did. "I ran out of time" is fine if it's true. Pretending nothing is
     left is not. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 3

       [ ] criteria.md has five numbered criteria, each with a target
       [ ] Each criterion has a reason underneath it
       [ ] All five unit 3 sections above have real content
       [ ] Tool Inventory: all three tools, inputs WITH TYPES, a specific
           return value, and the empty case
       [ ] Planning Loop names the branch rule and agent.py::run_agent
       [ ] Sample Run: one full query plus the three per-tool tests, as text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN, you submit the same one
           next unit

     SUBMISSION CHECKLIST — unit 4

       [ ] mcp_server.py exists with one tool registered
           (or a written record of exactly where the rewire broke)
       [ ] Run Log — Before, five criteria, five tries each
       [ ] Real output pasted underneath, naming file and function
       [ ] A verdict on every criterion
       [ ] A diagnosis for every miss, naming a place AND a mechanism
       [ ] Loop Trace, with the MCP call visible in it
       [ ] All three failure modes triggered and handled
       [ ] One improvement, with Run Log — After in the same format
       [ ] What's Still Broken
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository. Your commit history is what
     shows your criteria existed before your results did.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**


## Capstone 


## The Shape
For the Unit 9 capstone extension, I'm adding persistent personal wardrobes that allow the agent to retrieve saved clothing and create outfits grounded in the user's personal wardrobe.

## What's Out of Scope
For this extension, I’m not adding photo recognition; users will enter clothing details manually. I’m not adding accounts or authentication; I’ll use one demo user’s wardrobe. I’m also not adding weather integration or virtual try-on. I’m focusing on persistent wardrobe storage, the new `get_wardrobe` tool, and outfit recommendations grounded in saved items.

## Design Decisions
- **Wardrobe items are matched by `id`, not `name`.** Every saved item has an ID in the form `w_NNN` (e.g. `w_011`). IDs are never reused: the wardrobe file stores a `next_id` counter, and removing an item doesn't lower it, so an old outfit or eval result that mentions an ID can't end up pointing at a different piece. Outfit suggestions will reference items by this ID, and the grounding check will look for `w_NNN` IDs in the model's output.
- **An empty `style_tags` list is allowed; an empty `colors` list is not.** Style tags are optional descriptors, but colors are what outfit matching relies on, so every item needs at least one.
- **The saved wardrobe lives in `data/wardrobe.json`, which is not committed.** When the file is missing, `load_wardrobe()` recreates it from the example wardrobe, so deleting it resets the demo. Evals keep using the fixed example wardrobe so before/after runs stay comparable.


## Instrumentation

Every agent run writes one structured record: `run_log.py`, called from `serve.py` (`/ask`) and `app.py ask`. Each record is a single JSON line, appended to `logs/runs.jsonl` and, for `/ask`, also printed to stdout so it survives on Render, whose disk is wiped on every restart. Rejected requests and crashes write a record too. The fields are documented at the top of `run_log.py`. The ones that matter most here:

- **What happened:** `ts`, `run_id`, `source` (cli/http), `status` (ok / stopped / crashed / rejected), `query`, `error`
- **How long:** `duration_ms`, the server's own time for the run
- **What the agent did:** `wardrobe_source`, `wardrobe_items`, `selected_item`, `missing_categories`, `grounded`, `cited_ids`, `grounding_problems`, `grounding_retries`, plus the `outfit` and `fit_card` text the user saw
- **What it cost:** `model_calls`, `cache_hits`, `prompt_tokens`, `output_tokens`, from the counts the Gemini API reports for each call

**Eleven entries from the deployed app** (https://fitfindr-ppek.onrender.com), copied from Render's Logs tab on 2026-11-15. These are the ten cost-measurement runs below plus one rejected request:

```
{"ts": "2026-11-15T22:34:07.035+00:00", "run_id": "2cde0cbe", "source": "http", "status": "ok", "query": "vintage levi's jeans", "duration_ms": 10612, "error": null, "wardrobe_source": "saved", "wardrobe_items": 10, "selected_item": {"id": "lst_001", "title": "Vintage Levi's 501 Jeans — Medium Wash"}, "missing_categories": [], "wardrobe_note": null, "grounded": true, "cited_ids": ["w_003", "w_005", "w_007", "w_004", "w_008", "w_010"], "grounding_problems": [], "grounding_retries": 0, "outfit": "Outfit 1: Casual Streetwear\n- NEW: Vintage Levi's 501 Jeans — Medium Wash\n- w_003: White ribbed tank top\n- w_005: Black cropped zip hoodie\n- w_007: Chunky white sneakers\nVibe: An effortless, everyday streetwear look combining classic denim with sporty basics.\n\nOutfit 2: Vintage Edge\n- NEW: Vintage Levi's 501 Jeans — Medium Wash\n- w_004: Oversized grey crewneck sweatshirt\n- w_008: Black combat boots\n- w_010: Black crossbody bag\nVibe: A relaxed, grunge-inspired outfit that leans into the vintage aesthetic.", "fit_card": "Scored these Vintage Levi's 501 Jeans on Depop for $38.0! I threw them on with a white ribbed tank top, black cropped zip hoodie, and chunky white sneakers for an effortless, everyday streetwear look combining classic denim with sporty basics.", "model_calls": 2, "cache_hits": 0, "prompt_tokens": 1081, "output_tokens": 209}
{"ts": "2026-11-15T22:34:17.836+00:00", "run_id": "2a68e026", "source": "http", "status": "ok", "query": "y2k baby tee", "duration_ms": 10870, "error": null, "wardrobe_source": "saved", "wardrobe_items": 10, "selected_item": {"id": "lst_002", "title": "Y2K Baby Tee — Butterfly Print"}, "missing_categories": [], "wardrobe_note": null, "grounded": true, "cited_ids": ["w_001", "w_007", "w_010", "w_006", "w_008"], "grounding_problems": [], "grounding_retries": 0, "outfit": "Outfit 1: Y2K Street Denim\n- NEW: Y2K Baby Tee — Butterfly Print\n- w_001: Baggy straight-leg jeans, dark wash\n- w_007: Chunky white sneakers\n- w_010: Black crossbody bag\nVibe: A nostalgic early 2000s street style look balancing a fitted graphic top with relaxed denim.\n\nOutfit 2: Edgy Contrast\n- NEW: Y2K Baby Tee — Butterfly Print\n- w_006: Vintage black denim jacket\n- w_008: Black combat boots\nVibe: A toughened-up vintage combination pairing delicate graphics with heavy black layers.", "fit_card": "Scored this Y2K Baby Tee with Butterfly Print on Depop for $18. Styling the fitted crop length with baggy straight-leg jeans, dark wash, chunky white sneakers, and a black crossbody bag gives the ultimate nostalgic early 2000s street style look.", "model_calls": 2, "cache_hits": 0, "prompt_tokens": 1064, "output_tokens": 206}
{"ts": "2026-11-15T22:34:28.930+00:00", "run_id": "3b4be3ad", "source": "http", "status": "ok", "query": "graphic hoodie", "duration_ms": 10049, "error": null, "wardrobe_source": "saved", "wardrobe_items": 10, "selected_item": {"id": "lst_015", "title": "Vintage Graphic Hoodie — Faded Black"}, "missing_categories": [], "wardrobe_note": null, "grounded": true, "cited_ids": ["w_001", "w_008", "w_010", "w_002", "w_007", "w_009"], "grounding_problems": [], "grounding_retries": 0, "outfit": "Outfit 1: Grunge Streetwear\n- NEW: Vintage Graphic Hoodie — Faded Black\n- w_001: Baggy straight-leg jeans, dark wash\n- w_008: Black combat boots\n- w_010: Black crossbody bag\nVibe: A relaxed, effortless street style look anchored by worn-in textures and dark tones.\n\nOutfit 2: Casual Edge\n- NEW: Vintage Graphic Hoodie — Faded Black\n- w_002: Wide-leg khaki trousers\n- w_007: Chunky white sneakers\n- w_009: Brown leather belt\nVibe: An easy, balanced everyday outfit mixing vintage streetwear with neutral tailored elements.", "fit_card": "Scored this faded black vintage graphic hoodie on depop for $26.0 and it's so cozy. Paired it with baggy straight-leg jeans, black combat boots, and a black crossbody bag for a relaxed, effortless street style look anchored by worn-in textures and dark tones.", "model_calls": 2, "cache_hits": 0, "prompt_tokens": 1046, "output_tokens": 211}
{"ts": "2026-11-15T22:34:39.395+00:00", "run_id": "6e78e66a", "source": "http", "status": "ok", "query": "leather jacket", "duration_ms": 10391, "error": null, "wardrobe_source": "saved", "wardrobe_items": 10, "selected_item": {"id": "lst_022", "title": "90s Leather Bomber — Black"}, "missing_categories": [], "wardrobe_note": null, "grounded": true, "cited_ids": ["w_001", "w_003", "w_008", "w_002", "w_007"], "grounding_problems": [], "grounding_retries": 0, "outfit": "Outfit 1: 90s Grunge Street\n- NEW: 90s Leather Bomber — Black\n- w_001: Baggy straight-leg jeans, dark wash\n- w_003: White ribbed tank top\n- w_008: Black combat boots\nVibe: A classic, effortless everyday look leaning into vintage attitude.\n\nOutfit 2: Contrast Minimal\n- NEW: 90s Leather Bomber — Black\n- w_002: Wide-leg khaki trousers\n- w_003: White ribbed tank top\n- w_007: Chunky white sneakers\nVibe: An elevated mix of sharp tailoring and casual streetwear textures.", "fit_card": "Scored this genuine leather bomber jacket on depop for $75, and it instantly gave my everyday rotation the ultimate 90s grunge street edge. Worn over a white ribbed tank top with baggy straight-leg jeans and black combat boots, the slightly boxy silhouette and ribbed details lean right into that vintage attitude.", "model_calls": 2, "cache_hits": 0, "prompt_tokens": 1060, "output_tokens": 214}
{"ts": "2026-11-15T22:34:50.004+00:00", "run_id": "50fac038", "source": "http", "status": "ok", "query": "cargo pants", "duration_ms": 9792, "error": null, "wardrobe_source": "saved", "wardrobe_items": 10, "selected_item": {"id": "lst_011", "title": "Low-Rise Cargo Pants — Khaki"}, "missing_categories": [], "wardrobe_note": null, "grounded": true, "cited_ids": ["w_003", "w_006", "w_007", "w_005", "w_008", "w_010"], "grounding_problems": [], "grounding_retries": 0, "outfit": "Outfit 1: Y2K Streetwear\n- NEW: Low-Rise Cargo Pants — Khaki\n- w_003: White ribbed tank top\n- w_006: Vintage black denim jacket\n- w_007: Chunky white sneakers\nVibe: A classic noughties-inspired streetwear look featuring utilitarian cargo pockets and chunky sneakers.\n\nOutfit 2: Casual Grunge\n- NEW: Low-Rise Cargo Pants — Khaki\n- w_005: Black cropped zip hoodie\n- w_008: Black combat boots\n- w_010: Black crossbody bag\nVibe: An effortless everyday outfit that contrasts relaxed earth tones with tough black accents.", "fit_card": "Scored these Y2K era low-rise cargo pants for $27 on Poshmark and had so much fun styling them. Paired with a white ribbed tank top, vintage black denim jacket, and chunky white sneakers for a classic noughties-inspired streetwear look featuring utilitarian cargo pockets. They're also giving major Casual Grunge paired with a black cropped zip hoodie, black combat boots, and black crossbody bag for an effortless everyday outfit that contrasts relaxed earth tones with tough black accents.", "model_calls": 2, "cache_hits": 0, "prompt_tokens": 1068, "output_tokens": 247}
{"ts": "2026-11-15T22:34:59.998+00:00", "run_id": "5cf26ae3", "source": "http", "status": "ok", "query": "band tee", "duration_ms": 11182, "error": null, "wardrobe_source": "saved", "wardrobe_items": 10, "selected_item": {"id": "lst_033", "title": "Vintage Band Tee — Faded Grey"}, "missing_categories": [], "wardrobe_note": null, "grounded": true, "cited_ids": ["w_001", "w_008", "w_005", "w_007"], "grounding_problems": [], "grounding_retries": 0, "outfit": "Outfit 1: Grunge Street\n- NEW: Vintage Band Tee — Faded Grey\n- w_001: Baggy straight-leg jeans, dark wash\n- w_008: Black combat boots\nVibe: Effortless 90s streetwear with a classic worn-in edge.\n\nOutfit 2: Layered Edge\n- NEW: Vintage Band Tee — Faded Grey\n- w_005: Black cropped zip hoodie\n- w_001: Baggy straight-leg jeans, dark wash\n- w_007: Chunky white sneakers\nVibe: Casual skater-inspired proportions featuring a smart mix of street staples.", "fit_card": "Scored this Vintage Band Tee for $19.0 on depop and it is already doing all the heavy lifting in my wardrobe. I threw it on with baggy straight-leg jeans and black combat boots for that effortless 90s streetwear look, but it looks just as good layered under a black cropped zip hoodie with chunky white sneakers. The faded grey crew neck with the distressed graphic gives off the best grunge energy.", "model_calls": 2, "cache_hits": 0, "prompt_tokens": 1047, "output_tokens": 227}
{"ts": "2026-11-15T22:35:11.378+00:00", "run_id": "327bf6f0", "source": "http", "status": "ok", "query": "corduroy pants", "duration_ms": 10785, "error": null, "wardrobe_source": "saved", "wardrobe_items": 10, "selected_item": {"id": "lst_005", "title": "Corduroy Wide-Leg Pants — Rust"}, "missing_categories": [], "wardrobe_note": null, "grounded": true, "cited_ids": ["w_003", "w_006", "w_009", "w_007", "w_004", "w_008"], "grounding_problems": [], "grounding_retries": 0, "outfit": "Outfit 1: 70s Casual\n- NEW: Corduroy Wide-Leg Pants — Rust\n- w_003: White ribbed tank top\n- w_006: Vintage black denim jacket\n- w_009: Brown leather belt\n- w_007: Chunky white sneakers\nVibe: This retro-inspired combination pairs earthy autumn tones with crisp white accents for an easy, vintage everyday look.\n\nOutfit 2: Cozy Retro\n- NEW: Corduroy Wide-Leg Pants — Rust\n- w_004: Oversized grey crewneck sweatshirt\n- w_009: Brown leather belt\n- w_008: Black combat boots\nVibe: A relaxed, textured pairing that balances chunky cold-weather layers with rich vintage colors.", "fit_card": "Scored these wide-leg pants from depop for $32.0! They are so easy to style with a white ribbed tank top, vintage black denim jacket, brown leather belt, and chunky white sneakers for a retro-inspired, earthy autumn look. I also love wearing them with an oversized grey crewneck sweatshirt, brown leather belt, and black combat boots for a cozy, textured vibe.", "model_calls": 2, "cache_hits": 0, "prompt_tokens": 1071, "output_tokens": 250}
{"ts": "2026-11-15T22:35:22.355+00:00", "run_id": "bf068f3a", "source": "http", "status": "ok", "query": "knit cardigan", "duration_ms": 10401, "error": null, "wardrobe_source": "saved", "wardrobe_items": 10, "selected_item": {"id": "lst_008", "title": "Knit Cardigan — Chunky Brown"}, "missing_categories": [], "wardrobe_note": null, "grounded": true, "cited_ids": ["w_001", "w_003", "w_007", "w_002", "w_009", "w_008"], "grounding_problems": [], "grounding_retries": 0, "outfit": "Outfit 1: Earthy Contrast\n- NEW: Knit Cardigan — Chunky Brown\n- w_001: Baggy straight-leg jeans, dark wash\n- w_003: White ribbed tank top\n- w_007: Chunky white sneakers\nVibe: A relaxed, cozy street-style look blending rich earth tones with casual denim.\n\nOutfit 2: Tonal Comfort\n- NEW: Knit Cardigan — Chunky Brown\n- w_002: Wide-leg khaki trousers\n- w_009: Brown leather belt\n- w_008: Black combat boots\nVibe: A cohesive minimal outfit playing with warm neutrals and sturdy textures.", "fit_card": "Scored this chunky brown knit cardigan on Depop for $35.0, and it is the ultimate cozy layer. I love styling it with a white ribbed tank top, baggy straight-leg jeans, and chunky white sneakers for a relaxed street-style look. It also looks amazing dressed up with wide-leg khaki trousers, a brown leather belt, and black combat boots for a minimal outfit playing with warm neutrals.", "model_calls": 2, "cache_hits": 0, "prompt_tokens": 1051, "output_tokens": 234}
{"ts": "2026-11-15T22:35:32.996+00:00", "run_id": "db6ca040", "source": "http", "status": "ok", "query": "denim shorts", "duration_ms": 10645, "error": null, "wardrobe_source": "saved", "wardrobe_items": 10, "selected_item": {"id": "lst_016", "title": "High-Waisted Denim Shorts — Cutoff"}, "missing_categories": [], "wardrobe_note": null, "grounded": true, "cited_ids": ["w_003", "w_007", "w_010", "w_005", "w_008", "w_009"], "grounding_problems": [], "grounding_retries": 0, "outfit": "Outfit 1: Casual Summer\n- NEW: High-Waisted Denim Shorts — Cutoff\n- w_003: White ribbed tank top\n- w_007: Chunky white sneakers\n- w_010: Black crossbody bag\nVibe: This classic warm-weather combination is effortless and breathable.\n\nOutfit 2: Streetwear Edge\n- NEW: High-Waisted Denim Shorts — Cutoff\n- w_005: Black cropped zip hoodie\n- w_008: Black combat boots\n- w_009: Brown leather belt\nVibe: A contrasting mix of heavy hardware and light denim creates a bold silhouette.", "fit_card": "Scored these Levi's 501 DIY cutoff denim shorts for $24.0 on poshmark, and they are the ultimate warm-weather staple. I styled them into a casual summer look with a ribbed tank top, chunky sneakers, and a crossbody bag for an effortless, breathable vibe.", "model_calls": 2, "cache_hits": 0, "prompt_tokens": 1058, "output_tokens": 204}
{"ts": "2026-11-15T22:35:43.812+00:00", "run_id": "d5979462", "source": "http", "status": "ok", "query": "flannel shirt", "duration_ms": 10272, "error": null, "wardrobe_source": "saved", "wardrobe_items": 10, "selected_item": {"id": "lst_003", "title": "Oversized Flannel Shirt — Plaid Red/Black"}, "missing_categories": [], "wardrobe_note": null, "grounded": true, "cited_ids": ["w_003", "w_001", "w_008", "w_005", "w_007"], "grounding_problems": [], "grounding_retries": 0, "outfit": "Outfit 1: 90s Grunge Street\n- NEW: Oversized Flannel Shirt — Plaid Red/Black\n- w_003: White ribbed tank top\n- w_001: Baggy straight-leg jeans, dark wash\n- w_008: Black combat boots\nVibe: A classic, effortless grunge look anchored by dark denim and heavy boots.\n\nOutfit 2: Layered Streetwear\n- NEW: Oversized Flannel Shirt — Plaid Red/Black\n- w_005: Black cropped zip hoodie\n- w_001: Baggy straight-leg jeans, dark wash\n- w_007: Chunky white sneakers\nVibe: Casual streetwear pairing with comfortable layers and chunky footwear.", "fit_card": "Scored this oversized flannel shirt on thredUp for $22.00, and it's the ultimate layering piece for my streetwear looks. I love styling it with a white ribbed tank top, baggy straight-leg jeans, and black combat boots for effortless grunge vibes. It also looks so good paired over a black cropped zip hoodie with chunky white sneakers.", "model_calls": 2, "cache_hits": 0, "prompt_tokens": 1072, "output_tokens": 236}
{"ts": "2026-11-15T22:35:54.295+00:00", "run_id": "62b4de4f", "source": "http", "status": "rejected", "query": "denim jacket", "duration_ms": 0, "error": "The wardrobe you sent isn't valid. Item 1: Item field \"id\" must look like w_001 (got 'shirt1'). Item 1: Item field \"category\" must be one of: tops, bottoms, outerwear, shoes, accessories."}
```

**The failure entry** is the last one (`62b4de4f`). A wardrobe with a malformed ID (`shirt1`) and a category that doesn't exist (`hats`) was refused with HTTP 400 before the agent ran. That's why it has `duration_ms: 0` and no token fields. The caller got the same two `problems` in the response body.

**What the ten successful entries show:** all ten are `grounded: true` with `grounding_retries: 0`, and every cited ID is in the 10-item demo wardrobe Render reseeds from. They also show a known problem from unit 4 that's still there: 7 of the 10 fit cards write the price with a trailing decimal (`$38.0`, `$26.0`, `$22.00`) because the listing's float price goes into the prompt as-is.

### A failure the run records didn't catch

The first attempt at the cost measurement took the service down. At 5:12 PM local time, Render reported:

```
Instance failed: 4prpx
HTTP health check failed (timed out after 5 seconds) while running your code.
```

8 of the 10 runs and the rejected-request test came back as Render's own HTML `502 Bad Gateway` page (one of them: Request ID `a5b1978d3acc33a6-SEA`), and only 2 runs succeeded.

- **Cause:** gunicorn's default sync worker handles one request at a time, including `/health`, not only `/ask`. `measure_cost.py` sent ten `/ask` requests back to back, each 10–20 s on the free CPU, so Render's `/health` check queued behind them, passed its 5-second limit, and Render restarted the instance mid-run.
- **Fix:** `gunicorn serve:app --timeout 120 --threads 4` in `render.yaml`. It's still one process, so no extra memory on the 512 MB free tier, and agent runs still take turns through `serve.py`'s lock. But `/health` now gets its own thread.
- **Checked:** during a single 21-second `/ask` on Render, nine `/health` calls answered in 0.17–0.39 s each. The ten-run measurement above was then re-run on the fixed deploy with no failures.
- **The gap it exposed:** the requests that got a 502 left **no run record**, because the app wasn't running to write one. Only Render's Events tab and the client saw them. "Every run writes a record" holds for runs that reach the app; a crash of the host itself shows up only in the host's logs.

## What It Costs

**One run costs about 1,286 tokens (1,062 prompt + 224 output) across 2 model calls, and takes 10.5 s of server time.**

| | Average | Min | Max |
|---|---|---|---|
| Model calls | 2.0 | 2 | 2 |
| Prompt tokens | 1,062 | 1,046 | 1,081 |
| Output tokens | 224 | 204 | 250 |
| Total tokens | 1,286 | | |
| Server time | 10.5 s | 9.8 s | 11.2 s |

**How I measured it:**

- **What was run:** 10 runs against the deployed app on Render's free tier, sent one at a time with `python measure_cost.py send`. These are the ten `ok` entries under Instrumentation.
- **Why ten different queries:** each one selects a different listing (checked against `search_listings` first). The response cache is keyed by prompt, so a repeated listing would have come back from the cache at 0 tokens and pulled the average down. `cache_hits` was 0 on every run, so every number is a real model call.
- **Where the numbers come from:** tokens are the counts the Gemini API reported for each call (`usage_metadata`), summed per run by `generate.py` and written into each run's record by `run_log.py`. Time is `duration_ms`, measured on the server around `run_agent`. `python measure_cost.py summarize` averaged the ten records; the rejected request isn't in the average.
- **What the 2 calls are:** `suggest_outfit` and `create_fit_card`. The other two tool calls per run, `search_listings` and `get_wardrobe` over MCP, use no model, so their cost is only the server time already inside the 10.5 s. No run needed a grounding retry; one would add a third model call.

**In money:** the API key is on Google's free tier with no billing, so the actual spend for these runs was **$0**. The cost that counts is quota: each run uses 2 of the free tier's 15 requests per minute, and `generate.py` paces calls to stay under that limit. A paid-tier dollar figure would be the averages above multiplied by the model's per-token prices: `python measure_cost.py summarize logs/render_logs.txt --price-in <$ per 1M input> --price-out <$ per 1M output>`.

**Time varies more than tokens.** The first `/ask` after the threading fix took 21 s, against 9.8–11.2 s for these ten. That's most likely a freshly started instance warming up. It's one reason the measurement averages ten runs rather than reporting one.

## Capstone Run Log — Before

The five capstone criteria are in `criteria.md` → "Capstone criteria". Each one has three runs, and the cells count passes out of the trials in that run (criterion 1 counts operations: 5 adds and 5 removes per run).

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1.  Adding, removing, and persisting wardrobe items | 30/30 | 10/10 | 10/10 | 10/10 | MET (30/30) |
| 2.  Grounded outfit suggestions | 15/15 | 5/5 | 5/5 | 5/5 (re-run) | MET (15/15) |
| 3.  Empty wardrobe behavior | 15/15 | 5/5 | 5/5 | 5/5 | MET (15/15) |
| 4.  Corrupt wardrobe file handling | 15/15 | 5/5 | 5/5 | 5/5 | MET (15/15) |
| 5.  Validation and normalization when adding items | 18/18 | 6/6 | 6/6 | 5/6 | MISSED (17/18) |

All rows are scored from `results/run_2026-11-15_2327_capstone_before.md`, written by `run_capstone_eval.py`. Every step in it is a real `python app.py …` command in its own process, with response caching off. The one exception is criterion 2's run 3. In the original run, its setup step `wardrobe remove w_007` crashed with `PermissionError`, so the sneakers were never removed, and the agent was styling a wardrobe that still had them. That run was void, not failed, so I re-ran it on the same code: `results/run_2026-11-16_0030_capstone_before-rerun.md`. Its setup succeeded, and all 5 trials passed. Criterion 5's run-3 miss is the same crash, hitting a valid `wardrobe add`.

**Real output from one trial of each criterion.** Each block below is copied unedited from the results file: the console output of the command named above it, or, where marked, the text the harness typed in or read from `data/wardrobe.json`.

**Criterion 1: adding an item** (run 1, add 1). `python app.py wardrobe add`: the prompts and the `Added:` lines are printed by `app.py` (the `wardrobe add` command); the item is cleaned by `utils/wardrobe_store.py::normalize_item` and saved by `add_item`, which calls `save_wardrobe`.

Typed in at the prompts:

```
Navy Linen Shirt
Tops
Navy, navy, White
Minimal, summer
Runs large
```

Console output:

```
Enter the details of the item to add to your wardrobe.
Name: Category (tops, bottoms, outerwear, shoes, accessories): Colors (comma-separated): Style tags (comma-separated, optional): Notes (optional): Added:
  w_011  Navy Linen Shirt
        category:   tops
        colors:     navy, white
        style tags: minimal, summer
        notes:      Runs large
```

The item as `save_wardrobe` wrote it to `data/wardrobe.json`:

```
{"name": "Navy Linen Shirt", "category": "tops", "colors": ["navy", "white"], "style_tags": ["minimal", "summer"], "notes": "Runs large", "id": "w_011"}
```

**Criterion 2: grounded outfit** (run 1, trial 1, with w_007 and w_008 removed). `python app.py ask 'denim jacket under $50'`: trace lines from `trace.py::step`, called by `agent.py::run_agent`; the outfit is written by `tools.py::suggest_outfit` and checked by `tools.py::check_grounding`.

```
[1] search_listings
      in:  dict with keys: description, size, max_price
      out: 7 items: Denim Jacket — Light Wash, Cropped, High-Waisted Denim Shorts — Cutoff, Denim Vest — Medium Wash, Studded … +4 more
[2] get_wardrobe
      in:  dict with keys: 
      out: dict with keys: items
[3] check_wardrobe
      in:  dict with keys: items, selected_category
      out: 1 items: shoes…
      →    branch: missing shoes, continuing
[4] suggest_outfit
      in:  dict with keys: selected_item, wardrobe, missing_categories, feedback
      out: Outfit 1: Double Denim Streetwear - NEW: Denim Jacket — Light Wash, Cropped - w_001: Baggy straight-leg jeans,…
[5] check_grounding
      in:  dict with keys: cited
      out: True
      →    every piece is in the wardrobe
[6] create_fit_card
      in:  dict with keys: outfit_suggestion, selected_item
      out: Scored this Wrangler denim jacket in a light wash for $42.0 on poshmark, and it has the best structured should…

  Found:    Denim Jacket — Light Wash, Cropped — $42.0 on poshmark

  Outfit:   Outfit 1: Double Denim Streetwear
- NEW: Denim Jacket — Light Wash, Cropped
- w_001: Baggy straight-leg jeans, dark wash
- w_003: White ribbed tank top
- w_010: Black crossbody bag
Vibe: A contrasting Canadian tuxedo vibe playing with different denim washes and relaxed proportions.

Outfit 2: Casual Khaki Layer
- NEW: Denim Jacket — Light Wash, Cropped
- w_002: Wide-leg khaki trousers
- w_003: White ribbed tank top
- w_009: Brown leather belt
Vibe: A timeless, balanced mix of classic streetwear and minimal earth tones.

Missing: shoes

  Fit card: Scored this Wrangler denim jacket in a light wash for $42.0 on poshmark, and it has the best structured shoulders! I styled it for a contrasting Canadian tuxedo vibe playing with different denim washes and relaxed proportions by adding baggy straight-leg jeans, a white ribbed tank top, and a black crossbody bag. For a second look, it brings a timeless, balanced mix of classic streetwear and minimal earth tones when paired with wide-leg khaki trousers, a white ribbed tank top, and a brown leather belt.

  Note:     Your wardrobe has no shoes, so the outfit may be incomplete. Add some with: python app.py wardrobe add

2 model calls this session, 1028 prompt + 261 output tokens
```

The setup step that voided the original run 3, `python app.py wardrobe remove w_007` (exit 1). The error comes from `os.replace` in `utils/wardrobe_store.py::save_wardrobe`, printed by `app.py::main`. Typed in:

```
y
```

Console output:

```
w_007  Chunky white sneakers
        category:   shoes
        colors:     white
        style tags: sneakers, chunky, streetwear
        notes:      -
Remove this item? (y/n): 
PermissionError: [WinError 5] Access is denied: 'C:\\Users\\Antoine\\PersonalProjects&Learning\\CodePath\\ai201-project2-fitfindr-starter-v2026\\utils\\..\\data\\wardrobe.json.tmp' -> 'C:\\Users\\Antoine\\PersonalProjects&Learning\\CodePath\\ai201-project2-fitfindr-starter-v2026\\utils\\..\\data\\wardrobe.json'
```

**Criterion 3: empty wardrobe** (run 1, trial 1). `python app.py ask 'denim jacket under $50' --empty-wardrobe`: trace from `agent.py::run_agent`; the general-advice prompt is in `tools.py::suggest_outfit`; the `Note:` is set by `agent.py::run_agent` at the `check_wardrobe` branch.

```
(running with an empty wardrobe)
[1] search_listings
      in:  dict with keys: description, size, max_price
      out: 7 items: Denim Jacket — Light Wash, Cropped, High-Waisted Denim Shorts — Cutoff, Denim Vest — Medium Wash, Studded … +4 more
[2] check_wardrobe
      in:  dict with keys: items, selected_category
      out: [] (empty)
      →    branch: empty wardrobe, continuing with general advice
[3] suggest_outfit
      in:  dict with keys: selected_item, wardrobe, missing_categories, feedback
      out: Outfit 1: Layer it over a black ribbed turtleneck bodysuit, pair with high-waisted olive green utility pants, …
[4] check_grounding
      in:  dict with keys: cited
      →    empty wardrobe: general advice isn't meant to be grounded
[5] create_fit_card
      in:  dict with keys: outfit_suggestion, selected_item
      out: Found this vintage Wrangler denim jacket on Poshmark for $42.00, and it's the ultimate blank canvas with great…

  Found:    Denim Jacket — Light Wash, Cropped — $42.0 on poshmark

  Outfit:   Outfit 1: Layer it over a black ribbed turtleneck bodysuit, pair with high-waisted olive green utility pants, and finish with chunky black loafers. 
Vibe: 90s streetwear meets smart-casual. 

Outfit 2: Throw it on over a white cotton baby tee and a black-and-white plaid tennis skirt, add white crew socks, and lace-up retro sneakers. 
Vibe: Effortless skater-girl chic. 

Both are easy to build with basics you likely already own!

  Fit card: Found this vintage Wrangler denim jacket on Poshmark for $42.00, and it's the ultimate blank canvas with great structured shoulders. I paired the light blue cropped outerwear over a black ribbed turtleneck bodysuit, high-waisted olive green utility pants, and chunky black loafers for a true 90s streetwear meets smart-casual vibe.

  Note:     Your wardrobe is empty, so these are general styling ideas. Add your clothes with: python app.py wardrobe add

2 model calls this session, 549 prompt + 182 output tokens
```

**Criterion 4: corrupt wardrobe file** (run 1, trial 1, exit 0, with `data/wardrobe.json` containing `{"items": [broken`). `python app.py ask 'denim jacket under $50'`: the `get_wardrobe` call through `mcp_client.call_tool` fails, and `agent.py::run_agent` stops with this message.

```
[1] search_listings
      in:  dict with keys: description, size, max_price
      out: 7 items: Denim Jacket — Light Wash, Cropped, High-Waisted Denim Shorts — Cutoff, Denim Vest — Medium Wash, Studded … +4 more
[2] get_wardrobe
      in:  dict with keys: 
      →    branch: MCP call failed, stopping

  Couldn't read your saved wardrobe. Check that data/wardrobe.json is valid JSON, or delete it to reset to the demo wardrobe.

0 model calls this session
```

**Criterion 5: validation** (run 1, case B, whitespace-only name). `python app.py wardrobe add`: rejected by `utils/wardrobe_store.py::validate_item`, called from `add_item`; `Not saved:` is printed by `app.py`. Typed in (the name line is three spaces):

```
   
tops
red
```

Console output:

```
Enter the details of the item to add to your wardrobe.
Name: Category (tops, bottoms, outerwear, shoes, accessories): Colors (comma-separated): Style tags (comma-separated, optional): Notes (optional): Not saved:
  - Item field "name" cannot be empty.
```

And the miss (run 3, case A, exit 1): a valid item that should have been saved. Same `PermissionError` from `utils/wardrobe_store.py::save_wardrobe`, printed by `app.py::main`. Typed in:

```
Striped Tee
tops
  Red, red , NAVY, navy 
 Casual, casual,  STRIPED 
```

Console output:

```
Enter the details of the item to add to your wardrobe.
Name: Category (tops, bottoms, outerwear, shoes, accessories): Colors (comma-separated): Style tags (comma-separated, optional): Notes (optional): 
PermissionError: [WinError 5] Access is denied: 'C:\\Users\\Antoine\\PersonalProjects&Learning\\CodePath\\ai201-project2-fitfindr-starter-v2026\\utils\\..\\data\\wardrobe.json.tmp' -> 'C:\\Users\\Antoine\\PersonalProjects&Learning\\CodePath\\ai201-project2-fitfindr-starter-v2026\\utils\\..\\data\\wardrobe.json'
```

## Capstone Run Log — After

<!-- python run_capstone_eval.py --label after, graded the same way, same table. -->

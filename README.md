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
- **Inputs:** `new_item` (dict) and `wardrobe`(dict)
- **Returns:** It returns a string that describes a grouping of the new item and items from the input wardrobe that go with it and can make an outfit.
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

- *What I asked for:* I asked for Claude to implement the four tools built from my Tool Inventory and the tools.py docustrings, with a plan before any code was written.
- *What came back:* It returned a plan that pointed out my README disagreed with tools.py in two places. create_fit_card's outfit input as list[dict], but agent.py passes the string from suggest_outfit. I'd said suggest_outfit returns an error string on an empty wardrobe, but the docstring says it should give general styling advice. It also asked how "One Size" listings should match.
- *What I changed:* I rewrote the Tool Inventory to match the code: string input, styling advice for an empty wardrobe, and the whole-token size rule. I decided "One Size" listings only match when no size is given, so a request for a small top doesn't return bags and hats. The code was built according to that specification.

**Moment 2**

- *What I asked for:* I asked for a plan for run_agent before implementation.
- *What came back:*Claude gave two options. The first was a step loop that reads teh session each pass to pick the next tool. The other was a straight-line version with an if empty: return. It also asked whether to add the unit 4 trace and error handling now, and whether "size medium" should become M.
- *What I changed:* I chose the step loop so the branch is a real decision based on state. I held back the additions Claude would make for unit 4 and asked for size words to be converted, then checked the result by comparing session["selected)_item"] to the object that reached suggest_outfit. 

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

Criterion 5 Diagnosis: The suggest_outfit criterion didn't pass for any of the run. None of the listed pieces when searched in wardrobe_schema.json contained the same style tags as the originally searched item. The failure happened at the model's output since the text suggest_outfit got back from the model was what failed the check. The failed step was suggest_outfit and the failed mechanism was that nothing in the prompt specifies that returned outfit suggestion's pieces should share tags. In all 5 tries, Outfit 1 includes the Black crossbody bag (minimal, accessories, everyday), which shares no tag with Graphic Tee (graphic tee, vintage, grunge, streetwear, band tee). Outfit 2 uses khaki trousers and brown leather belt, which don't share any either. The outfits themselves are reasonable, so the criterion was checking the wrong property. I revised it in criteria rather than forcing tag matching into the prompt, which could make worse outfits or limit the possible outfits returned. 


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

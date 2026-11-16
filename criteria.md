# Acceptance criteria — FitFindr

Five criteria that say what "working" means for this agent, written in unit 3
**before** any results existed.

An acceptance criterion names a target: a number, a count, a rate, or something
a person could plainly observe. *"The agent handles errors"* is an opinion.
*"When search returns nothing, the agent stops before calling the second tool,
in 5 of 5 tries"* is a criterion.

Under each one, write a sentence or two on **why that target** and not a
stricter one. A reason that says something about your tools, your loop, or the
data earns credit; *"80% seemed reasonable"* does not.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

**Two are written for you. You write three.**

---

## 1. A matching query completes all three tools

Given a query that matches at least one listing, the agent completes all three
tool calls and returns a fit card — in at least 4 of 5 tries.

**Why this target:**
<!-- Why 4 of 5 and not 5 of 5? Something about your search, probably —
     "my search is a plain keyword match and some phrasings will miss" is a
     real answer. -->
This is the basic purpose of the FitFindr project: to search listings, work out potential outfits with the item, and to write a caption for it. 4 of 5 is a valid goal since it allows for an occasional failed model request from suggest_outfit or create_fit_card.
---

## 2. An impossible query stops before the second tool

Given a query that matches no listings, the agent stops before calling
`suggest_outfit` and returns a message naming what to change — 5 of 5 tries.

**Why this target:**
<!-- Why is 5 of 5 reasonable here when criterion 1 isn't? What's different
     about this path? -->
The system should be able to handle failed requests, and 5 of 5 is a valid goal since anything lower could allow the system to fabricate results for the first tool in order to continue to the second and third tools.
---

## 3. Something about state

In 5 of 5 tries, the first listing dict that is returned from the search in the first tool matches the listing dict that is used as input for the suggest_outfit tool. 
<!-- YOU WRITE THIS ONE.

     How would you know that the item your search found is the same item the
     next tool received? Name something countable or observable.

     This is the criterion people find hardest, because state failure doesn't
     look like state failure — it looks like a tool problem. Something that
     compares session["selected_item"] against what actually reached
     suggest_outfit is the shape you're after. -->



**Why this target:**
I chose this target because it tests the system's ability to carry input and output successfully through the different stages. I chose 5 of 5 tries specifically because this is critical and should succeed in all 5 tries since the step copies stored data between tools rather than relying on model generation.


---

## 4. Something about the fit card

For 5 different selected items, at least 4 of the 5 generated fit cards mention one accurate detail about the selected item or suggested outfit, such as its clothing type, color, a style tag, material, or combination of pieces, and contain no details that contradict those inputs.

<!-- YOU WRITE THIS ONE.

     The fit card calls a model, so the same input can produce different words
     each time. That's not a bug — it's the nature of the tool. So what would
     make it acceptable?

     Think about what you'd actually be unhappy to see. A caption that never
     mentions the price? Two different items producing the same opening
     sentence? A card longer than a caption anyone would post? Any of those can
     be turned into a number. -->



**Why this target:**
This target tests another important part of the system, which is the ability to generate accurate captions. There's flexibility in this part since it's model generated, and more than one caption can be accurate, so it's good to have a solid list of what all valid captions should definitely contain. I chose 4 of 5 different generated fit cards for 5 different items because it ensures that different inputs can have valid generated outputs, and model generation isn't always completely accurate so 4 suffices.



---

## 5. Your choice

For 5 of 5 tries, the suggest_outfit tool returns a grouping in which each listing item in the grouping list shares the same style tag value as the rest of the items in the grouping.


<!-- YOU WRITE THIS ONE TOO.

     Pick something you actually care about getting right. Speed, the empty
     wardrobe path, what happens when the model can't be reached, whether the
     search respects a price ceiling — anything, as long as it names a number
     or an observable outcome. -->



**Why this target:**
This tests the accuracy of the suggest_outfit tool since the system is supposed to group together items that are similar in some way rather than the groupings being random. I chose 5 of 5 as the goal because this doesn't rely on model generation, meaning it should be consistent.

**Revised in unit 4:** on a matching query with the example wardrobe, for 5 of 5 tries, every piece described in each outfit exists in the user's wardrobe, and each outfit includes the new item.

**Why revised:**

I inferred an incorrect output of suggest_outfit(a single group of listing items) when the actual output is a string paragraph of text naming wardrobe pieces instead of listings. I also said in my explanation that the function doesn't rely on model generation, but suggest_outfit does actually call the model. Thirdly, real outfits can mix style tags, or categories, epecially if they are contrast outfits. The previous criterion fails groupings of clothes that are actually good outfits. My previous criterion tried to make fashion, something that's subjective, objective by measuring it with style tags. The new criterion trusts the model to handle fashion choices and instead makes sure that the items listed in the outfit include the searched item and actual clothing pieces in the wardrobe rather than fabricating. I want to keep the 5/5 goal because the prompt tells the model to use only listed pieces and name them exactly, and an invented piece means the user is told to wear something they don't own, which shouldn't ever happen.



---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 4 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath it, like this:

         ## 4. Something about the fit card

         The fit card is different every time.

         **Why this target:** ...

         > **Revised in unit 4:** For 5 different items, the 5 fit cards share
         > no opening sentence.
         >
         > **Why revised:** "different" wasn't checkable — two cards that
         > differed by one word still counted. The new version is something I
         > can actually score.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "I said the empty search stops it 5 of 5 times, but I got 3 of 5,
            so 3 of 5 is more realistic."

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->

---

# Capstone criteria — unit 9, Milestone 4

Five criteria for the capstone extension (persistent wardrobe, `get_wardrobe`, grounded outfits), written before any capstone results existed. The unit 3/4 criteria above are unchanged.

**For every criterion:**
- **A fresh demo wardrobe** means: delete `data/wardrobe.json`. The next command recreates it from the 10-item demo wardrobe (`w_001`–`w_010`, `next_id` 11).
- **Quote queries with single quotes**, in bash and PowerShell alike. In double quotes, `$50` is read as a variable: bash turns `under $50` into `under 0` and PowerShell into `under ` with no price.

## Capstone criterion 1: Adding, removing, and persisting wardrobe items

Each run starts with a fresh demo wardrobe. Add five items through the CLI (`python app.py wardrobe add`), then remove the last listed item five times (`python app.py wardrobe remove <id>`, confirming with `y`), targeting the five newly added items.

Each addition passes if:
- The item's ID matches the wardrobe's `next_id` value recorded immediately before adding it.
- The item appears with the correct details in both `wardrobe list` and `data/wardrobe.json`. Style tags and notes must be checked in the JSON file. `wardrobe list` cuts names off after 40 characters and colors after 20, ending them with `…`; a value cut off this way still counts as correct in the list as long as the JSON file has the full value.
- All text fields are trimmed. Categories are lowercase, and colors and style tags are lowercase and deduplicated.
- Running `wardrobe list` in a separate process still shows the saved item.

Each removal passes if only the targeted ID disappears from both the list and JSON file, and every other item remains unchanged. After all five removals, the wardrobe must contain the original demo items.

**Target:** Five successful additions and five successful removals per run across three runs: **30/30 operations**.

**Why this target:** These operations are deterministic. Users must be able to trust that their wardrobe changes are saved accurately and that removing one item will not delete another.

## Capstone criterion 2: Grounded outfit suggestions

Start each run with a fresh demo wardrobe and remove shoes `w_007` and `w_008`:

```
python app.py wardrobe remove w_007
python app.py wardrobe remove w_008
```

Confirm each removal with `y`. Then run these queries through the agent loop:

```
python app.py ask 'denim jacket under $50'
python app.py ask 'vintage levis jeans'
```

Run the first query three times and the second query twice in each run.

A trial passes if every wardrobe piece cited in the final output, after any checking and retrying, uses an ID present in the loaded wardrobe and a name matching that item. A shortened name passes if it only uses words from the saved name: dropping words is fine ("Black denim jacket" for "Vintage black denim jacket"), adding words is not ("Oversized black denim jacket"). Evaluate the piece lines (lines starting with `- `); exclude the vibe line from this check. Every piece line other than the `- NEW:` line must cite a `w_NNN` ID; a piece line with no ID, such as `- Gold hoop earrings`, fails the trial. Neither removed shoe ID may appear as an owned piece.

An explicit "couldn't build" response also passes because it avoids inventing wardrobe items.

**Target:** **5/5 trials in each of three runs: 15/15 total.**

**Why this target:** Grounding is central to the extension. Users should receive suggestions based on clothing they actually own, and the system should acknowledge when it cannot build an outfit.

## Capstone criterion 3: Empty wardrobe behavior

Load an empty wardrobe using `--empty-wardrobe`, then run an `ask` query for a valid searchable item:

```
python app.py ask 'denim jacket under $50' --empty-wardrobe
```

A trial passes if:
- The response explicitly states that the wardrobe is empty and that the suggestions are general styling ideas, with the note: *"Your wardrobe is empty, so these are general styling ideas. Add your clothes with: python app.py wardrobe add"*.
- No wardrobe item IDs are cited.
- A fit card is produced.
- The command completes without a traceback.

**Target:** **5/5 trials in each of three runs: 15/15 total.**

**Why this target:** An empty wardrobe is an expected user state. The application must explain that limitation while still providing useful general advice.

## Capstone criterion 4: Corrupt wardrobe file handling

Back up `data/wardrobe.json`, then replace its contents with invalid JSON:

```text
{"items": [broken
```

Run:

```
python app.py ask 'denim jacket under $50'
```

A trial passes if the application displays:

> Couldn't read your saved wardrobe. Check that data/wardrobe.json is valid JSON, or delete it to reset to the demo wardrobe.

The command must exit normally with exit code `0`, without a traceback or silently treating the corrupt file as an empty wardrobe. Restore the original file after testing.

**Target:** **5/5 trials in each of three runs: 15/15 total.**

**Why this target:** Silently ignoring a corrupt file could mislead users into thinking their wardrobe is empty. A clear error and recovery instructions let them address the problem.

## Capstone criterion 5: Validation and normalization when adding items

Each run starts with a fresh demo wardrobe and contains the following six test cases, entered through `python app.py wardrobe add`. Use otherwise valid values whenever testing one field.

| Case | Input | Expected result |
|---|---|---|
| A | Repeated colors and style tags, including capitalization differences and surrounding spaces | The item is saved once. The CLI shows `Added:` with cleaned values, and the stored lists are lowercase, trimmed, and deduplicated. |
| B | Blank or whitespace-only name | The item is rejected with `Item field "name" cannot be empty.` |
| C | Blank or whitespace-only category | The item is rejected with `Item field "category" must be one of: tops, bottoms, outerwear, shoes, accessories.` |
| D | Blank or whitespace-only colors | The item is rejected with `Item field "colors" must contain at least one color.` |
| E | Invalid category, such as `furniture` | The item is rejected with the same category message as Case C. |
| F | Valid required fields, with style tags and notes left blank | The item is saved successfully because these fields are optional. |

For every rejected addition, the CLI must show `Not saved:` with the reason. The wardrobe list and JSON file must remain unchanged.

**Target:** **6/6 cases in each of three runs: 18/18 total.**

**Why this target:** Validation is deterministic. Required fields must be enforced consistently, optional fields must remain optional, and repeated tags should not create messy wardrobe data.

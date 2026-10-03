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

In 5 of 5 tries, the listing dict that is returned from the search in the first tool matches the listing dict that is used as input for the suggest_outfit tool. 
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

For 5 of 5 tries, the suggest_outfit tool returns grouping in which each listing item in the grouping list shares the same style tag value as the rest of the items in the grouping.
<!-- YOU WRITE THIS ONE TOO.

     Pick something you actually care about getting right. Speed, the empty
     wardrobe path, what happens when the model can't be reached, whether the
     search respects a price ceiling — anything, as long as it names a number
     or an observable outcome. -->



**Why this target:**
This tests the accuracy of the suggest_outfit tool since the system is supposed to group together items that are similar in some way rather than the groupings being random. I chose 5 of 5 as the goal because this doesn't rely on model generation, meaning it should be consistent.



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

# Capstone run log — before-rerun

- Produced by: `run_capstone_eval.py`, following criteria.md → "Capstone criteria"
- Each step is a real `python app.py …` command in its own process
- Runs per criterion: 1 · caching off · 9 s between asks
- When: 2026-11-16 00:30

The PASS/FAIL cells are blank on purpose: grade each trial against the
criterion's wording using the evidence underneath, then count.

## Capstone criterion 2: Grounded outfit suggestions

**Target:** 15/15 trials

| Trial | Run 1 |
|---|---|
| trial 1 | PASS |
| trial 2 | PASS |
| trial 3 | PASS |
| trial 4 | PASS |
| trial 5 | PASS |

**Verdict:** 5 / 5

Re-run of criterion 2's run 3 from `results/run_2026-11-15_2327_capstone_before.md`, whose setup crashed (`PermissionError` removing w_007), using the same code as that run (the save retry fix was stashed). Setup succeeded: the loaded wardrobe has no w_007 or w_008. Every piece line cites a loaded ID with its exact saved name, no piece line lacks an ID, neither removed shoe appears, and every outfit ends with `Missing: shoes`.

### Criterion 2, run 1

**setup: demo without shoes**

- wardrobe IDs loaded:

```
["w_001", "w_002", "w_003", "w_004", "w_005", "w_006", "w_009", "w_010"]
```


<details><summary>setup: <code>python app.py wardrobe list</code> → exit 0, 0.3 s</summary>

Output:

```
id     category     colors                name
--------------------------------------------------------------------------------
w_001  bottoms      dark blue, indigo     Baggy straight-leg jeans, dark wash
w_002  bottoms      khaki, tan            Wide-leg khaki trousers
w_003  tops         white                 White ribbed tank top
w_004  tops         grey, charcoal        Oversized grey crewneck sweatshirt
w_005  tops         black                 Black cropped zip hoodie
w_006  outerwear    black                 Vintage black denim jacket
w_007  shoes        white                 Chunky white sneakers
w_008  shoes        black                 Black combat boots
w_009  accessories  brown                 Brown leather belt
w_010  accessories  black                 Black crossbody bag

10 item(s).
```

</details>

<details><summary>remove w_007: <code>python app.py wardrobe remove w_007</code> → exit 0, 0.2 s</summary>

Typed input:

```
y
```

Output:

```
w_007  Chunky white sneakers
        category:   shoes
        colors:     white
        style tags: sneakers, chunky, streetwear
        notes:      -
Remove this item? (y/n): Removed w_007 (Chunky white sneakers).
```

</details>

<details><summary>remove w_008: <code>python app.py wardrobe remove w_008</code> → exit 0, 0.2 s</summary>

Typed input:

```
y
```

Output:

```
w_008  Black combat boots
        category:   shoes
        colors:     black
        style tags: boots, grunge, classic
        notes:      Lace-up, mid-ankle height
Remove this item? (y/n): Removed w_008 (Black combat boots).
```

</details>

**trial 1**

- query: `denim jacket under $50`
- status / error: `ok / None`
- grounding check verdict (code's, not yours): `True`
- grounding retries: `0`
- IDs cited:

```
["w_001", "w_003", "w_010", "w_002", "w_009"]
```

- cited IDs not in the loaded wardrobe:

```
[]
```

- final outfit (piece lines to grade):

```
Outfit 1: Double Denim Streetwear
- NEW: Denim Jacket — Light Wash, Cropped
- w_001: Baggy straight-leg jeans, dark wash
- w_003: White ribbed tank top
- w_010: Black crossbody bag
Vibe: This look plays with contrasting denim washes for an effortless, classic streetwear aesthetic.

Outfit 2: Casual Earth Tones
- NEW: Denim Jacket — Light Wash, Cropped
- w_002: Wide-leg khaki trousers
- w_003: White ribbed tank top
- w_009: Brown leather belt
Vibe: A minimalist combination of light blue and tan creates a relaxed, everyday ensemble.

Missing: shoes
```


<details><summary>ask: <code>python app.py ask 'denim jacket under $50'</code> → exit 0, 11.7 s</summary>

Output:

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
      out: Scored this Wrangler cropped denim jacket on Poshmark for $42, and it's such a blank canvas with great structu…

  Found:    Denim Jacket — Light Wash, Cropped — $42.0 on poshmark

  Outfit:   Outfit 1: Double Denim Streetwear
- NEW: Denim Jacket — Light Wash, Cropped
- w_001: Baggy straight-leg jeans, dark wash
- w_003: White ribbed tank top
- w_010: Black crossbody bag
Vibe: This look plays with contrasting denim washes for an effortless, classic streetwear aesthetic.

Outfit 2: Casual Earth Tones
- NEW: Denim Jacket — Light Wash, Cropped
- w_002: Wide-leg khaki trousers
- w_003: White ribbed tank top
- w_009: Brown leather belt
Vibe: A minimalist combination of light blue and tan creates a relaxed, everyday ensemble.

Missing: shoes

  Fit card: Scored this Wrangler cropped denim jacket on Poshmark for $42, and it's such a blank canvas with great structured shoulders. I paired it with a white ribbed tank top, dark wash baggy straight-leg jeans, and a black crossbody bag for a classic double denim streetwear vibe. It also looks so good styled with wide-leg khaki trousers, a brown leather belt, and the same white ribbed tank top for a relaxed, everyday minimalist ensemble.

  Note:     Your wardrobe has no shoes, so the outfit may be incomplete. Add some with: python app.py wardrobe add

2 model calls this session, 1031 prompt + 252 output tokens
```

</details>

**trial 2**

- query: `denim jacket under $50`
- status / error: `ok / None`
- grounding check verdict (code's, not yours): `True`
- grounding retries: `0`
- IDs cited:

```
["w_001", "w_003", "w_002", "w_009"]
```

- cited IDs not in the loaded wardrobe:

```
[]
```

- final outfit (piece lines to grade):

```
Outfit 1: Double Denim Streetwear
- NEW: Denim Jacket — Light Wash, Cropped
- w_001: Baggy straight-leg jeans, dark wash
- w_003: White ribbed tank top
Vibe: A classic Canadian tuxedo featuring a smart contrast of light and dark washes.

Outfit 2: Khaki Contrast
- NEW: Denim Jacket — Light Wash, Cropped
- w_002: Wide-leg khaki trousers
- w_003: White ribbed tank top
- w_009: Brown leather belt
Vibe: An easy, balanced mix of cool denim and warm earth tones.

Missing: shoes
```


<details><summary>ask: <code>python app.py ask 'denim jacket under $50'</code> → exit 0, 15.8 s</summary>

Output:

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
      out: Scored this Wrangler denim jacket for $42 on Poshmark and I am obsessed with the structured shoulders and blan…

  Found:    Denim Jacket — Light Wash, Cropped — $42.0 on poshmark

  Outfit:   Outfit 1: Double Denim Streetwear
- NEW: Denim Jacket — Light Wash, Cropped
- w_001: Baggy straight-leg jeans, dark wash
- w_003: White ribbed tank top
Vibe: A classic Canadian tuxedo featuring a smart contrast of light and dark washes.

Outfit 2: Khaki Contrast
- NEW: Denim Jacket — Light Wash, Cropped
- w_002: Wide-leg khaki trousers
- w_003: White ribbed tank top
- w_009: Brown leather belt
Vibe: An easy, balanced mix of cool denim and warm earth tones.

Missing: shoes

  Fit card: Scored this Wrangler denim jacket for $42 on Poshmark and I am obsessed with the structured shoulders and blank canvas. Paired it with dark wash baggy straight-leg jeans and a white ribbed tank top for a classic streetwear double denim vibe. Or, keep it grounded with wide-leg khaki trousers, a white ribbed tank top, and a brown leather belt for an easy earth-toned mix.

  Note:     Your wardrobe has no shoes, so the outfit may be incomplete. Add some with: python app.py wardrobe add

2 model calls this session, 1022 prompt + 226 output tokens
```

</details>

**trial 3**

- query: `denim jacket under $50`
- status / error: `ok / None`
- grounding check verdict (code's, not yours): `True`
- grounding retries: `0`
- IDs cited:

```
["w_001", "w_003", "w_010", "w_002", "w_009"]
```

- cited IDs not in the loaded wardrobe:

```
[]
```

- final outfit (piece lines to grade):

```
Outfit 1: Double Denim
- NEW: Denim Jacket — Light Wash, Cropped
- w_001: Baggy straight-leg jeans, dark wash
- w_003: White ribbed tank top
- w_010: Black crossbody bag
Vibe: This classic streetwear look plays with contrasting denim washes for a balanced vintage silhouette.

Outfit 2: Khaki Contrast
- NEW: Denim Jacket — Light Wash, Cropped
- w_002: Wide-leg khaki trousers
- w_003: White ribbed tank top
- w_009: Brown leather belt
Vibe: A minimalist earth-tone pairing that keeps the structured outerwear as the focal point.

Missing: shoes
```


<details><summary>ask: <code>python app.py ask 'denim jacket under $50'</code> → exit 0, 26.3 s</summary>

Output:

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
      out: Outfit 1: Double Denim - NEW: Denim Jacket — Light Wash, Cropped - w_001: Baggy straight-leg jeans, dark wash …
[5] check_grounding
      in:  dict with keys: cited
      out: True
      →    every piece is in the wardrobe
[6] create_fit_card
      in:  dict with keys: outfit_suggestion, selected_item
      out: Scored this Wrangler denim jacket for $42 on Poshmark and I am obsessed with the light wash, cropped fit. It l…

  Found:    Denim Jacket — Light Wash, Cropped — $42.0 on poshmark

  Outfit:   Outfit 1: Double Denim
- NEW: Denim Jacket — Light Wash, Cropped
- w_001: Baggy straight-leg jeans, dark wash
- w_003: White ribbed tank top
- w_010: Black crossbody bag
Vibe: This classic streetwear look plays with contrasting denim washes for a balanced vintage silhouette.

Outfit 2: Khaki Contrast
- NEW: Denim Jacket — Light Wash, Cropped
- w_002: Wide-leg khaki trousers
- w_003: White ribbed tank top
- w_009: Brown leather belt
Vibe: A minimalist earth-tone pairing that keeps the structured outerwear as the focal point.

Missing: shoes

  Fit card: Scored this Wrangler denim jacket for $42 on Poshmark and I am obsessed with the light wash, cropped fit. It looks so good paired with a white ribbed tank top and baggy straight-leg jeans for a double denim vintage streetwear moment. I also love wearing it with wide-leg khaki trousers and a brown leather belt for an earth-tone vibe.

  Note:     Your wardrobe has no shoes, so the outfit may be incomplete. Add some with: python app.py wardrobe add

2 model calls this session, 1029 prompt + 231 output tokens
```

</details>

**trial 4**

- query: `vintage levis jeans`
- status / error: `ok / None`
- grounding check verdict (code's, not yours): `True`
- grounding retries: `0`
- IDs cited:

```
["w_003", "w_006", "w_010", "w_004", "w_009"]
```

- cited IDs not in the loaded wardrobe:

```
[]
```

- final outfit (piece lines to grade):

```
Outfit 1: Casual Streetwear
- NEW: Vintage Levi's 501 Jeans — Medium Wash
- w_003: White ribbed tank top
- w_006: Vintage black denim jacket
- w_010: Black crossbody bag
Vibe: Effortless and classic everyday streetwear with a vintage edge.

Outfit 2: Cozy Layers
- NEW: Vintage Levi's 501 Jeans — Medium Wash
- w_004: Oversized grey crewneck sweatshirt
- w_009: Brown leather belt
- w_010: Black crossbody bag
Vibe: Relaxed and comfortable with a casual, lived-in feel.

Missing: shoes
```


<details><summary>ask: <code>python app.py ask 'vintage levis jeans'</code> → exit 0, 12.2 s</summary>

Output:

```
[1] search_listings
      in:  dict with keys: description, size, max_price
      out: 10 items: Vintage Levi's 501 Jeans — Medium Wash, Straight Leg Black Jeans — Faded, Oversized Crewneck Sweatshirt — Vintage Navy … +7 more
[2] get_wardrobe
      in:  dict with keys: 
      out: dict with keys: items
[3] check_wardrobe
      in:  dict with keys: items, selected_category
      out: 1 items: shoes…
      →    branch: missing shoes, continuing
[4] suggest_outfit
      in:  dict with keys: selected_item, wardrobe, missing_categories, feedback
      out: Outfit 1: Casual Streetwear - NEW: Vintage Levi's 501 Jeans — Medium Wash - w_003: White ribbed tank top - w_0…
[5] check_grounding
      in:  dict with keys: cited
      out: True
      →    every piece is in the wardrobe
[6] create_fit_card
      in:  dict with keys: outfit_suggestion, selected_item
      out: Scored these vintage Levi's 501 jeans for $38 on depop, and they are already my favorite pair. I love how the …

  Found:    Vintage Levi's 501 Jeans — Medium Wash — $38.0 on depop

  Outfit:   Outfit 1: Casual Streetwear
- NEW: Vintage Levi's 501 Jeans — Medium Wash
- w_003: White ribbed tank top
- w_006: Vintage black denim jacket
- w_010: Black crossbody bag
Vibe: Effortless and classic everyday streetwear with a vintage edge.

Outfit 2: Cozy Layers
- NEW: Vintage Levi's 501 Jeans — Medium Wash
- w_004: Oversized grey crewneck sweatshirt
- w_009: Brown leather belt
- w_010: Black crossbody bag
Vibe: Relaxed and comfortable with a casual, lived-in feel.

Missing: shoes

  Fit card: Scored these vintage Levi's 501 jeans for $38 on depop, and they are already my favorite pair. I love how the classic medium wash looks paired with a white ribbed tank top, black denim jacket, and a black crossbody bag for effortless streetwear. They also have an easy, lived-in feel with a grey crewneck sweatshirt and brown leather belt.

  Note:     Your wardrobe has no shoes, so the outfit may be incomplete. Add some with: python app.py wardrobe add

2 model calls this session, 1055 prompt + 231 output tokens
```

</details>

**trial 5**

- query: `vintage levis jeans`
- status / error: `ok / None`
- grounding check verdict (code's, not yours): `True`
- grounding retries: `0`
- IDs cited:

```
["w_003", "w_006", "w_010", "w_004", "w_009"]
```

- cited IDs not in the loaded wardrobe:

```
[]
```

- final outfit (piece lines to grade):

```
Outfit 1: Vintage Street
- NEW: Vintage Levi's 501 Jeans — Medium Wash
- w_003: White ribbed tank top
- w_006: Vintage black denim jacket
- w_010: Black crossbody bag
Vibe: A classic, effortless denim-on-denim streetwear look.

Outfit 2: Cozy Casual
- NEW: Vintage Levi's 501 Jeans — Medium Wash
- w_004: Oversized grey crewneck sweatshirt
- w_009: Brown leather belt
- w_010: Black crossbody bag
Vibe: A relaxed, comfortable weekend outfit with a vintage touch.

Missing: shoes
```


<details><summary>ask: <code>python app.py ask 'vintage levis jeans'</code> → exit 0, 11.0 s</summary>

Output:

```
[1] search_listings
      in:  dict with keys: description, size, max_price
      out: 10 items: Vintage Levi's 501 Jeans — Medium Wash, Straight Leg Black Jeans — Faded, Oversized Crewneck Sweatshirt — Vintage Navy … +7 more
[2] get_wardrobe
      in:  dict with keys: 
      out: dict with keys: items
[3] check_wardrobe
      in:  dict with keys: items, selected_category
      out: 1 items: shoes…
      →    branch: missing shoes, continuing
[4] suggest_outfit
      in:  dict with keys: selected_item, wardrobe, missing_categories, feedback
      out: Outfit 1: Vintage Street - NEW: Vintage Levi's 501 Jeans — Medium Wash - w_003: White ribbed tank top - w_006:…
[5] check_grounding
      in:  dict with keys: cited
      out: True
      →    every piece is in the wardrobe
[6] create_fit_card
      in:  dict with keys: outfit_suggestion, selected_item
      out: Scored these vintage Levi's 501 jeans on Depop for just $38.0! I love how the classic denim pairs with a white…

  Found:    Vintage Levi's 501 Jeans — Medium Wash — $38.0 on depop

  Outfit:   Outfit 1: Vintage Street
- NEW: Vintage Levi's 501 Jeans — Medium Wash
- w_003: White ribbed tank top
- w_006: Vintage black denim jacket
- w_010: Black crossbody bag
Vibe: A classic, effortless denim-on-denim streetwear look.

Outfit 2: Cozy Casual
- NEW: Vintage Levi's 501 Jeans — Medium Wash
- w_004: Oversized grey crewneck sweatshirt
- w_009: Brown leather belt
- w_010: Black crossbody bag
Vibe: A relaxed, comfortable weekend outfit with a vintage touch.

Missing: shoes

  Fit card: Scored these vintage Levi's 501 jeans on Depop for just $38.0! I love how the classic denim pairs with a white ribbed tank top, vintage black denim jacket, and black crossbody bag for a streetwear look, or an oversized grey crewneck sweatshirt, brown leather belt, and black crossbody bag for a cozy vibe.

  Note:     Your wardrobe has no shoes, so the outfit may be incomplete. Add some with: python app.py wardrobe add

2 model calls this session, 1054 prompt + 224 output tokens
```

</details>

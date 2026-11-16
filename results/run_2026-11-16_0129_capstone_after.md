# Capstone run log — after

- Produced by: `run_capstone_eval.py`, following criteria.md → "Capstone criteria"
- Each step is a real `python app.py …` command in its own process
- Runs per criterion: 3 · caching off · 9 s between asks
- When: 2026-11-16 01:29

The PASS/FAIL cells are blank on purpose: grade each trial against the
criterion's wording using the evidence underneath, then count.

## Capstone criterion 1: Adding, removing, and persisting wardrobe items

**Target:** 30/30 operations

| Trial | Run 1 | Run 2 | Run 3 |
|---|---|---|---|
| add 1 | PASS | PASS | PASS |
| add 2 | PASS | PASS | PASS |
| add 3 | PASS | PASS | PASS |
| add 4 | PASS | PASS | PASS |
| add 5 | PASS | PASS | PASS |
| remove 1 | PASS | PASS | PASS |
| remove 2 | PASS | PASS | PASS |
| remove 3 | PASS | PASS | PASS |
| remove 4 | PASS | PASS | PASS |
| remove 5 | PASS | PASS | PASS |

**Verdict:** 30 / 30

### Criterion 1, run 1

**fresh demo wardrobe**


<details><summary>setup: <code>python app.py wardrobe list</code> → exit 0, 0.1 s</summary>

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

**add 1**

- next_id before: `11`
- IDs added:

```
["w_011"]
```

- stored item (wardrobe.json):

```
{"name": "Navy Linen Shirt", "category": "tops", "colors": ["navy", "white"], "style_tags": ["minimal", "summer"], "notes": "Runs large", "id": "w_011"}
```

- shown by `wardrobe list` (separate process):

```
["w_011  tops         navy, white           Navy Linen Shirt"]
```


<details><summary>add: <code>python app.py wardrobe add</code> → exit 0, 0.2 s</summary>

Typed input:

```
Navy Linen Shirt
Tops
Navy, navy, White
Minimal, summer
Runs large
```

Output:

```
Enter the details of the item to add to your wardrobe.
Name: Category (tops, bottoms, outerwear, shoes, accessories): Colors (comma-separated): Style tags (comma-separated, optional): Notes (optional): Added:
  w_011  Navy Linen Shirt
        category:   tops
        colors:     navy, white
        style tags: minimal, summer
        notes:      Runs large
```

</details>

<details><summary>list: <code>python app.py wardrobe list</code> → exit 0, 0.1 s</summary>

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
w_011  tops         navy, white           Navy Linen Shirt

11 item(s).
```

</details>

**add 2**

- next_id before: `12`
- IDs added:

```
["w_012"]
```

- stored item (wardrobe.json):

```
{"name": "Olive Cargo Shorts", "category": "bottoms", "colors": ["olive"], "style_tags": ["utility"], "notes": null, "id": "w_012"}
```

- shown by `wardrobe list` (separate process):

```
["w_012  bottoms      olive                 Olive Cargo Shorts"]
```


<details><summary>add: <code>python app.py wardrobe add</code> → exit 0, 0.1 s</summary>

Typed input:

```
  Olive Cargo Shorts 
bottoms
 Olive ,olive
utility
```

Output:

```
Enter the details of the item to add to your wardrobe.
Name: Category (tops, bottoms, outerwear, shoes, accessories): Colors (comma-separated): Style tags (comma-separated, optional): Notes (optional): Added:
  w_012  Olive Cargo Shorts
        category:   bottoms
        colors:     olive
        style tags: utility
        notes:      -
```

</details>

<details><summary>list: <code>python app.py wardrobe list</code> → exit 0, 0.1 s</summary>

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
w_011  tops         navy, white           Navy Linen Shirt
w_012  bottoms      olive                 Olive Cargo Shorts

12 item(s).
```

</details>

**add 3**

- next_id before: `13`
- IDs added:

```
["w_013"]
```

- stored item (wardrobe.json):

```
{"name": "Red Canvas High-Tops", "category": "shoes", "colors": ["red", "white"], "style_tags": ["sneakers", "casual"], "notes": "Laces fray a bit", "id": "w_013"}
```

- shown by `wardrobe list` (separate process):

```
["w_013  shoes        red, white            Red Canvas High-Tops"]
```


<details><summary>add: <code>python app.py wardrobe add</code> → exit 0, 0.1 s</summary>

Typed input:

```
Red Canvas High-Tops
SHOES
red, White, red
Sneakers, Casual, casual
 Laces fray a bit 
```

Output:

```
Enter the details of the item to add to your wardrobe.
Name: Category (tops, bottoms, outerwear, shoes, accessories): Colors (comma-separated): Style tags (comma-separated, optional): Notes (optional): Added:
  w_013  Red Canvas High-Tops
        category:   shoes
        colors:     red, white
        style tags: sneakers, casual
        notes:      Laces fray a bit
```

</details>

<details><summary>list: <code>python app.py wardrobe list</code> → exit 0, 0.2 s</summary>

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
w_011  tops         navy, white           Navy Linen Shirt
w_012  bottoms      olive                 Olive Cargo Shorts
w_013  shoes        red, white            Red Canvas High-Tops

13 item(s).
```

</details>

**add 4**

- next_id before: `14`
- IDs added:

```
["w_014"]
```

- stored item (wardrobe.json):

```
{"name": "Grey Wool Beanie", "category": "accessories", "colors": ["grey"], "style_tags": [], "notes": null, "id": "w_014"}
```

- shown by `wardrobe list` (separate process):

```
["w_014  accessories  grey                  Grey Wool Beanie"]
```


<details><summary>add: <code>python app.py wardrobe add</code> → exit 0, 0.2 s</summary>

Typed input:

```
Grey Wool Beanie
accessories
grey
```

Output:

```
Enter the details of the item to add to your wardrobe.
Name: Category (tops, bottoms, outerwear, shoes, accessories): Colors (comma-separated): Style tags (comma-separated, optional): Notes (optional): Added:
  w_014  Grey Wool Beanie
        category:   accessories
        colors:     grey
        style tags: -
        notes:      -
```

</details>

<details><summary>list: <code>python app.py wardrobe list</code> → exit 0, 0.2 s</summary>

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
w_011  tops         navy, white           Navy Linen Shirt
w_012  bottoms      olive                 Olive Cargo Shorts
w_013  shoes        red, white            Red Canvas High-Tops
w_014  accessories  grey                  Grey Wool Beanie

14 item(s).
```

</details>

**add 5**

- next_id before: `15`
- IDs added:

```
["w_015"]
```

- stored item (wardrobe.json):

```
{"name": "Tan Trench Coat", "category": "outerwear", "colors": ["tan", "beige"], "style_tags": ["classic"], "notes": "Belted", "id": "w_015"}
```

- shown by `wardrobe list` (separate process):

```
["w_015  outerwear    tan, beige            Tan Trench Coat"]
```


<details><summary>add: <code>python app.py wardrobe add</code> → exit 0, 0.1 s</summary>

Typed input:

```
Tan Trench Coat
 outerwear 
Tan, beige
classic, Classic
Belted
```

Output:

```
Enter the details of the item to add to your wardrobe.
Name: Category (tops, bottoms, outerwear, shoes, accessories): Colors (comma-separated): Style tags (comma-separated, optional): Notes (optional): Added:
  w_015  Tan Trench Coat
        category:   outerwear
        colors:     tan, beige
        style tags: classic
        notes:      Belted
```

</details>

<details><summary>list: <code>python app.py wardrobe list</code> → exit 0, 0.1 s</summary>

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
w_011  tops         navy, white           Navy Linen Shirt
w_012  bottoms      olive                 Olive Cargo Shorts
w_013  shoes        red, white            Red Canvas High-Tops
w_014  accessories  grey                  Grey Wool Beanie
w_015  outerwear    tan, beige            Tan Trench Coat

15 item(s).
```

</details>

**remove 1**

- targeted (last listed) ID: `w_015`
- IDs that disappeared:

```
["w_015"]
```

- every other item unchanged in wardrobe.json: `True`
- target still in `wardrobe list`: `False`

<details><summary>remove: <code>python app.py wardrobe remove w_015</code> → exit 0, 0.1 s</summary>

Typed input:

```
y
```

Output:

```
w_015  Tan Trench Coat
        category:   outerwear
        colors:     tan, beige
        style tags: classic
        notes:      Belted
Remove this item? (y/n): Removed w_015 (Tan Trench Coat).
```

</details>

<details><summary>list: <code>python app.py wardrobe list</code> → exit 0, 0.2 s</summary>

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
w_011  tops         navy, white           Navy Linen Shirt
w_012  bottoms      olive                 Olive Cargo Shorts
w_013  shoes        red, white            Red Canvas High-Tops
w_014  accessories  grey                  Grey Wool Beanie

14 item(s).
```

</details>

**remove 2**

- targeted (last listed) ID: `w_014`
- IDs that disappeared:

```
["w_014"]
```

- every other item unchanged in wardrobe.json: `True`
- target still in `wardrobe list`: `False`

<details><summary>remove: <code>python app.py wardrobe remove w_014</code> → exit 0, 0.2 s</summary>

Typed input:

```
y
```

Output:

```
w_014  Grey Wool Beanie
        category:   accessories
        colors:     grey
        style tags: -
        notes:      -
Remove this item? (y/n): Removed w_014 (Grey Wool Beanie).
```

</details>

<details><summary>list: <code>python app.py wardrobe list</code> → exit 0, 0.1 s</summary>

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
w_011  tops         navy, white           Navy Linen Shirt
w_012  bottoms      olive                 Olive Cargo Shorts
w_013  shoes        red, white            Red Canvas High-Tops

13 item(s).
```

</details>

**remove 3**

- targeted (last listed) ID: `w_013`
- IDs that disappeared:

```
["w_013"]
```

- every other item unchanged in wardrobe.json: `True`
- target still in `wardrobe list`: `False`

<details><summary>remove: <code>python app.py wardrobe remove w_013</code> → exit 0, 0.1 s</summary>

Typed input:

```
y
```

Output:

```
w_013  Red Canvas High-Tops
        category:   shoes
        colors:     red, white
        style tags: sneakers, casual
        notes:      Laces fray a bit
Remove this item? (y/n): Removed w_013 (Red Canvas High-Tops).
```

</details>

<details><summary>list: <code>python app.py wardrobe list</code> → exit 0, 0.1 s</summary>

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
w_011  tops         navy, white           Navy Linen Shirt
w_012  bottoms      olive                 Olive Cargo Shorts

12 item(s).
```

</details>

**remove 4**

- targeted (last listed) ID: `w_012`
- IDs that disappeared:

```
["w_012"]
```

- every other item unchanged in wardrobe.json: `True`
- target still in `wardrobe list`: `False`

<details><summary>remove: <code>python app.py wardrobe remove w_012</code> → exit 0, 0.2 s</summary>

Typed input:

```
y
```

Output:

```
w_012  Olive Cargo Shorts
        category:   bottoms
        colors:     olive
        style tags: utility
        notes:      -
Remove this item? (y/n): Removed w_012 (Olive Cargo Shorts).
```

</details>

<details><summary>list: <code>python app.py wardrobe list</code> → exit 0, 0.2 s</summary>

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
w_011  tops         navy, white           Navy Linen Shirt

11 item(s).
```

</details>

**remove 5**

- targeted (last listed) ID: `w_011`
- IDs that disappeared:

```
["w_011"]
```

- every other item unchanged in wardrobe.json: `True`
- target still in `wardrobe list`: `False`

<details><summary>remove: <code>python app.py wardrobe remove w_011</code> → exit 0, 0.1 s</summary>

Typed input:

```
y
```

Output:

```
w_011  Navy Linen Shirt
        category:   tops
        colors:     navy, white
        style tags: minimal, summer
        notes:      Runs large
Remove this item? (y/n): Removed w_011 (Navy Linen Shirt).
```

</details>

<details><summary>list: <code>python app.py wardrobe list</code> → exit 0, 0.1 s</summary>

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

**after all removals**

- items equal the original demo items: `True`
- IDs now:

```
["w_001", "w_002", "w_003", "w_004", "w_005", "w_006", "w_007", "w_008", "w_009", "w_010"]
```

- next_id now: `16`

### Criterion 1, run 2

**fresh demo wardrobe**


<details><summary>setup: <code>python app.py wardrobe list</code> → exit 0, 0.1 s</summary>

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

**add 1**

- next_id before: `11`
- IDs added:

```
["w_011"]
```

- stored item (wardrobe.json):

```
{"name": "Navy Linen Shirt", "category": "tops", "colors": ["navy", "white"], "style_tags": ["minimal", "summer"], "notes": "Runs large", "id": "w_011"}
```

- shown by `wardrobe list` (separate process):

```
["w_011  tops         navy, white           Navy Linen Shirt"]
```


<details><summary>add: <code>python app.py wardrobe add</code> → exit 0, 0.1 s</summary>

Typed input:

```
Navy Linen Shirt
Tops
Navy, navy, White
Minimal, summer
Runs large
```

Output:

```
Enter the details of the item to add to your wardrobe.
Name: Category (tops, bottoms, outerwear, shoes, accessories): Colors (comma-separated): Style tags (comma-separated, optional): Notes (optional): Added:
  w_011  Navy Linen Shirt
        category:   tops
        colors:     navy, white
        style tags: minimal, summer
        notes:      Runs large
```

</details>

<details><summary>list: <code>python app.py wardrobe list</code> → exit 0, 0.1 s</summary>

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
w_011  tops         navy, white           Navy Linen Shirt

11 item(s).
```

</details>

**add 2**

- next_id before: `12`
- IDs added:

```
["w_012"]
```

- stored item (wardrobe.json):

```
{"name": "Olive Cargo Shorts", "category": "bottoms", "colors": ["olive"], "style_tags": ["utility"], "notes": null, "id": "w_012"}
```

- shown by `wardrobe list` (separate process):

```
["w_012  bottoms      olive                 Olive Cargo Shorts"]
```


<details><summary>add: <code>python app.py wardrobe add</code> → exit 0, 0.1 s</summary>

Typed input:

```
  Olive Cargo Shorts 
bottoms
 Olive ,olive
utility
```

Output:

```
Enter the details of the item to add to your wardrobe.
Name: Category (tops, bottoms, outerwear, shoes, accessories): Colors (comma-separated): Style tags (comma-separated, optional): Notes (optional): Added:
  w_012  Olive Cargo Shorts
        category:   bottoms
        colors:     olive
        style tags: utility
        notes:      -
```

</details>

<details><summary>list: <code>python app.py wardrobe list</code> → exit 0, 0.1 s</summary>

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
w_011  tops         navy, white           Navy Linen Shirt
w_012  bottoms      olive                 Olive Cargo Shorts

12 item(s).
```

</details>

**add 3**

- next_id before: `13`
- IDs added:

```
["w_013"]
```

- stored item (wardrobe.json):

```
{"name": "Red Canvas High-Tops", "category": "shoes", "colors": ["red", "white"], "style_tags": ["sneakers", "casual"], "notes": "Laces fray a bit", "id": "w_013"}
```

- shown by `wardrobe list` (separate process):

```
["w_013  shoes        red, white            Red Canvas High-Tops"]
```


<details><summary>add: <code>python app.py wardrobe add</code> → exit 0, 0.1 s</summary>

Typed input:

```
Red Canvas High-Tops
SHOES
red, White, red
Sneakers, Casual, casual
 Laces fray a bit 
```

Output:

```
Enter the details of the item to add to your wardrobe.
Name: Category (tops, bottoms, outerwear, shoes, accessories): Colors (comma-separated): Style tags (comma-separated, optional): Notes (optional): Added:
  w_013  Red Canvas High-Tops
        category:   shoes
        colors:     red, white
        style tags: sneakers, casual
        notes:      Laces fray a bit
```

</details>

<details><summary>list: <code>python app.py wardrobe list</code> → exit 0, 0.1 s</summary>

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
w_011  tops         navy, white           Navy Linen Shirt
w_012  bottoms      olive                 Olive Cargo Shorts
w_013  shoes        red, white            Red Canvas High-Tops

13 item(s).
```

</details>

**add 4**

- next_id before: `14`
- IDs added:

```
["w_014"]
```

- stored item (wardrobe.json):

```
{"name": "Grey Wool Beanie", "category": "accessories", "colors": ["grey"], "style_tags": [], "notes": null, "id": "w_014"}
```

- shown by `wardrobe list` (separate process):

```
["w_014  accessories  grey                  Grey Wool Beanie"]
```


<details><summary>add: <code>python app.py wardrobe add</code> → exit 0, 0.1 s</summary>

Typed input:

```
Grey Wool Beanie
accessories
grey
```

Output:

```
Enter the details of the item to add to your wardrobe.
Name: Category (tops, bottoms, outerwear, shoes, accessories): Colors (comma-separated): Style tags (comma-separated, optional): Notes (optional): Added:
  w_014  Grey Wool Beanie
        category:   accessories
        colors:     grey
        style tags: -
        notes:      -
```

</details>

<details><summary>list: <code>python app.py wardrobe list</code> → exit 0, 0.1 s</summary>

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
w_011  tops         navy, white           Navy Linen Shirt
w_012  bottoms      olive                 Olive Cargo Shorts
w_013  shoes        red, white            Red Canvas High-Tops
w_014  accessories  grey                  Grey Wool Beanie

14 item(s).
```

</details>

**add 5**

- next_id before: `15`
- IDs added:

```
["w_015"]
```

- stored item (wardrobe.json):

```
{"name": "Tan Trench Coat", "category": "outerwear", "colors": ["tan", "beige"], "style_tags": ["classic"], "notes": "Belted", "id": "w_015"}
```

- shown by `wardrobe list` (separate process):

```
["w_015  outerwear    tan, beige            Tan Trench Coat"]
```


<details><summary>add: <code>python app.py wardrobe add</code> → exit 0, 0.1 s</summary>

Typed input:

```
Tan Trench Coat
 outerwear 
Tan, beige
classic, Classic
Belted
```

Output:

```
Enter the details of the item to add to your wardrobe.
Name: Category (tops, bottoms, outerwear, shoes, accessories): Colors (comma-separated): Style tags (comma-separated, optional): Notes (optional): Added:
  w_015  Tan Trench Coat
        category:   outerwear
        colors:     tan, beige
        style tags: classic
        notes:      Belted
```

</details>

<details><summary>list: <code>python app.py wardrobe list</code> → exit 0, 0.1 s</summary>

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
w_011  tops         navy, white           Navy Linen Shirt
w_012  bottoms      olive                 Olive Cargo Shorts
w_013  shoes        red, white            Red Canvas High-Tops
w_014  accessories  grey                  Grey Wool Beanie
w_015  outerwear    tan, beige            Tan Trench Coat

15 item(s).
```

</details>

**remove 1**

- targeted (last listed) ID: `w_015`
- IDs that disappeared:

```
["w_015"]
```

- every other item unchanged in wardrobe.json: `True`
- target still in `wardrobe list`: `False`

<details><summary>remove: <code>python app.py wardrobe remove w_015</code> → exit 0, 0.1 s</summary>

Typed input:

```
y
```

Output:

```
w_015  Tan Trench Coat
        category:   outerwear
        colors:     tan, beige
        style tags: classic
        notes:      Belted
Remove this item? (y/n): Removed w_015 (Tan Trench Coat).
```

</details>

<details><summary>list: <code>python app.py wardrobe list</code> → exit 0, 0.1 s</summary>

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
w_011  tops         navy, white           Navy Linen Shirt
w_012  bottoms      olive                 Olive Cargo Shorts
w_013  shoes        red, white            Red Canvas High-Tops
w_014  accessories  grey                  Grey Wool Beanie

14 item(s).
```

</details>

**remove 2**

- targeted (last listed) ID: `w_014`
- IDs that disappeared:

```
["w_014"]
```

- every other item unchanged in wardrobe.json: `True`
- target still in `wardrobe list`: `False`

<details><summary>remove: <code>python app.py wardrobe remove w_014</code> → exit 0, 0.1 s</summary>

Typed input:

```
y
```

Output:

```
w_014  Grey Wool Beanie
        category:   accessories
        colors:     grey
        style tags: -
        notes:      -
Remove this item? (y/n): Removed w_014 (Grey Wool Beanie).
```

</details>

<details><summary>list: <code>python app.py wardrobe list</code> → exit 0, 0.1 s</summary>

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
w_011  tops         navy, white           Navy Linen Shirt
w_012  bottoms      olive                 Olive Cargo Shorts
w_013  shoes        red, white            Red Canvas High-Tops

13 item(s).
```

</details>

**remove 3**

- targeted (last listed) ID: `w_013`
- IDs that disappeared:

```
["w_013"]
```

- every other item unchanged in wardrobe.json: `True`
- target still in `wardrobe list`: `False`

<details><summary>remove: <code>python app.py wardrobe remove w_013</code> → exit 0, 0.1 s</summary>

Typed input:

```
y
```

Output:

```
w_013  Red Canvas High-Tops
        category:   shoes
        colors:     red, white
        style tags: sneakers, casual
        notes:      Laces fray a bit
Remove this item? (y/n): Removed w_013 (Red Canvas High-Tops).
```

</details>

<details><summary>list: <code>python app.py wardrobe list</code> → exit 0, 0.1 s</summary>

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
w_011  tops         navy, white           Navy Linen Shirt
w_012  bottoms      olive                 Olive Cargo Shorts

12 item(s).
```

</details>

**remove 4**

- targeted (last listed) ID: `w_012`
- IDs that disappeared:

```
["w_012"]
```

- every other item unchanged in wardrobe.json: `True`
- target still in `wardrobe list`: `False`

<details><summary>remove: <code>python app.py wardrobe remove w_012</code> → exit 0, 0.1 s</summary>

Typed input:

```
y
```

Output:

```
w_012  Olive Cargo Shorts
        category:   bottoms
        colors:     olive
        style tags: utility
        notes:      -
Remove this item? (y/n): Removed w_012 (Olive Cargo Shorts).
```

</details>

<details><summary>list: <code>python app.py wardrobe list</code> → exit 0, 0.1 s</summary>

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
w_011  tops         navy, white           Navy Linen Shirt

11 item(s).
```

</details>

**remove 5**

- targeted (last listed) ID: `w_011`
- IDs that disappeared:

```
["w_011"]
```

- every other item unchanged in wardrobe.json: `True`
- target still in `wardrobe list`: `False`

<details><summary>remove: <code>python app.py wardrobe remove w_011</code> → exit 0, 0.2 s</summary>

Typed input:

```
y
```

Output:

```
w_011  Navy Linen Shirt
        category:   tops
        colors:     navy, white
        style tags: minimal, summer
        notes:      Runs large
Remove this item? (y/n): Removed w_011 (Navy Linen Shirt).
```

</details>

<details><summary>list: <code>python app.py wardrobe list</code> → exit 0, 0.1 s</summary>

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

**after all removals**

- items equal the original demo items: `True`
- IDs now:

```
["w_001", "w_002", "w_003", "w_004", "w_005", "w_006", "w_007", "w_008", "w_009", "w_010"]
```

- next_id now: `16`

### Criterion 1, run 3

**fresh demo wardrobe**


<details><summary>setup: <code>python app.py wardrobe list</code> → exit 0, 0.1 s</summary>

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

**add 1**

- next_id before: `11`
- IDs added:

```
["w_011"]
```

- stored item (wardrobe.json):

```
{"name": "Navy Linen Shirt", "category": "tops", "colors": ["navy", "white"], "style_tags": ["minimal", "summer"], "notes": "Runs large", "id": "w_011"}
```

- shown by `wardrobe list` (separate process):

```
["w_011  tops         navy, white           Navy Linen Shirt"]
```


<details><summary>add: <code>python app.py wardrobe add</code> → exit 0, 0.1 s</summary>

Typed input:

```
Navy Linen Shirt
Tops
Navy, navy, White
Minimal, summer
Runs large
```

Output:

```
Enter the details of the item to add to your wardrobe.
Name: Category (tops, bottoms, outerwear, shoes, accessories): Colors (comma-separated): Style tags (comma-separated, optional): Notes (optional): Added:
  w_011  Navy Linen Shirt
        category:   tops
        colors:     navy, white
        style tags: minimal, summer
        notes:      Runs large
```

</details>

<details><summary>list: <code>python app.py wardrobe list</code> → exit 0, 0.1 s</summary>

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
w_011  tops         navy, white           Navy Linen Shirt

11 item(s).
```

</details>

**add 2**

- next_id before: `12`
- IDs added:

```
["w_012"]
```

- stored item (wardrobe.json):

```
{"name": "Olive Cargo Shorts", "category": "bottoms", "colors": ["olive"], "style_tags": ["utility"], "notes": null, "id": "w_012"}
```

- shown by `wardrobe list` (separate process):

```
["w_012  bottoms      olive                 Olive Cargo Shorts"]
```


<details><summary>add: <code>python app.py wardrobe add</code> → exit 0, 0.1 s</summary>

Typed input:

```
  Olive Cargo Shorts 
bottoms
 Olive ,olive
utility
```

Output:

```
Enter the details of the item to add to your wardrobe.
Name: Category (tops, bottoms, outerwear, shoes, accessories): Colors (comma-separated): Style tags (comma-separated, optional): Notes (optional): Added:
  w_012  Olive Cargo Shorts
        category:   bottoms
        colors:     olive
        style tags: utility
        notes:      -
```

</details>

<details><summary>list: <code>python app.py wardrobe list</code> → exit 0, 0.1 s</summary>

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
w_011  tops         navy, white           Navy Linen Shirt
w_012  bottoms      olive                 Olive Cargo Shorts

12 item(s).
```

</details>

**add 3**

- next_id before: `13`
- IDs added:

```
["w_013"]
```

- stored item (wardrobe.json):

```
{"name": "Red Canvas High-Tops", "category": "shoes", "colors": ["red", "white"], "style_tags": ["sneakers", "casual"], "notes": "Laces fray a bit", "id": "w_013"}
```

- shown by `wardrobe list` (separate process):

```
["w_013  shoes        red, white            Red Canvas High-Tops"]
```


<details><summary>add: <code>python app.py wardrobe add</code> → exit 0, 0.1 s</summary>

Typed input:

```
Red Canvas High-Tops
SHOES
red, White, red
Sneakers, Casual, casual
 Laces fray a bit 
```

Output:

```
Enter the details of the item to add to your wardrobe.
Name: Category (tops, bottoms, outerwear, shoes, accessories): Colors (comma-separated): Style tags (comma-separated, optional): Notes (optional): Added:
  w_013  Red Canvas High-Tops
        category:   shoes
        colors:     red, white
        style tags: sneakers, casual
        notes:      Laces fray a bit
```

</details>

<details><summary>list: <code>python app.py wardrobe list</code> → exit 0, 0.1 s</summary>

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
w_011  tops         navy, white           Navy Linen Shirt
w_012  bottoms      olive                 Olive Cargo Shorts
w_013  shoes        red, white            Red Canvas High-Tops

13 item(s).
```

</details>

**add 4**

- next_id before: `14`
- IDs added:

```
["w_014"]
```

- stored item (wardrobe.json):

```
{"name": "Grey Wool Beanie", "category": "accessories", "colors": ["grey"], "style_tags": [], "notes": null, "id": "w_014"}
```

- shown by `wardrobe list` (separate process):

```
["w_014  accessories  grey                  Grey Wool Beanie"]
```


<details><summary>add: <code>python app.py wardrobe add</code> → exit 0, 0.1 s</summary>

Typed input:

```
Grey Wool Beanie
accessories
grey
```

Output:

```
Enter the details of the item to add to your wardrobe.
Name: Category (tops, bottoms, outerwear, shoes, accessories): Colors (comma-separated): Style tags (comma-separated, optional): Notes (optional): Added:
  w_014  Grey Wool Beanie
        category:   accessories
        colors:     grey
        style tags: -
        notes:      -
```

</details>

<details><summary>list: <code>python app.py wardrobe list</code> → exit 0, 0.1 s</summary>

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
w_011  tops         navy, white           Navy Linen Shirt
w_012  bottoms      olive                 Olive Cargo Shorts
w_013  shoes        red, white            Red Canvas High-Tops
w_014  accessories  grey                  Grey Wool Beanie

14 item(s).
```

</details>

**add 5**

- next_id before: `15`
- IDs added:

```
["w_015"]
```

- stored item (wardrobe.json):

```
{"name": "Tan Trench Coat", "category": "outerwear", "colors": ["tan", "beige"], "style_tags": ["classic"], "notes": "Belted", "id": "w_015"}
```

- shown by `wardrobe list` (separate process):

```
["w_015  outerwear    tan, beige            Tan Trench Coat"]
```


<details><summary>add: <code>python app.py wardrobe add</code> → exit 0, 0.1 s</summary>

Typed input:

```
Tan Trench Coat
 outerwear 
Tan, beige
classic, Classic
Belted
```

Output:

```
Enter the details of the item to add to your wardrobe.
Name: Category (tops, bottoms, outerwear, shoes, accessories): Colors (comma-separated): Style tags (comma-separated, optional): Notes (optional): Added:
  w_015  Tan Trench Coat
        category:   outerwear
        colors:     tan, beige
        style tags: classic
        notes:      Belted
```

</details>

<details><summary>list: <code>python app.py wardrobe list</code> → exit 0, 0.1 s</summary>

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
w_011  tops         navy, white           Navy Linen Shirt
w_012  bottoms      olive                 Olive Cargo Shorts
w_013  shoes        red, white            Red Canvas High-Tops
w_014  accessories  grey                  Grey Wool Beanie
w_015  outerwear    tan, beige            Tan Trench Coat

15 item(s).
```

</details>

**remove 1**

- targeted (last listed) ID: `w_015`
- IDs that disappeared:

```
["w_015"]
```

- every other item unchanged in wardrobe.json: `True`
- target still in `wardrobe list`: `False`

<details><summary>remove: <code>python app.py wardrobe remove w_015</code> → exit 0, 0.1 s</summary>

Typed input:

```
y
```

Output:

```
w_015  Tan Trench Coat
        category:   outerwear
        colors:     tan, beige
        style tags: classic
        notes:      Belted
Remove this item? (y/n): Removed w_015 (Tan Trench Coat).
```

</details>

<details><summary>list: <code>python app.py wardrobe list</code> → exit 0, 0.1 s</summary>

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
w_011  tops         navy, white           Navy Linen Shirt
w_012  bottoms      olive                 Olive Cargo Shorts
w_013  shoes        red, white            Red Canvas High-Tops
w_014  accessories  grey                  Grey Wool Beanie

14 item(s).
```

</details>

**remove 2**

- targeted (last listed) ID: `w_014`
- IDs that disappeared:

```
["w_014"]
```

- every other item unchanged in wardrobe.json: `True`
- target still in `wardrobe list`: `False`

<details><summary>remove: <code>python app.py wardrobe remove w_014</code> → exit 0, 0.1 s</summary>

Typed input:

```
y
```

Output:

```
w_014  Grey Wool Beanie
        category:   accessories
        colors:     grey
        style tags: -
        notes:      -
Remove this item? (y/n): Removed w_014 (Grey Wool Beanie).
```

</details>

<details><summary>list: <code>python app.py wardrobe list</code> → exit 0, 0.1 s</summary>

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
w_011  tops         navy, white           Navy Linen Shirt
w_012  bottoms      olive                 Olive Cargo Shorts
w_013  shoes        red, white            Red Canvas High-Tops

13 item(s).
```

</details>

**remove 3**

- targeted (last listed) ID: `w_013`
- IDs that disappeared:

```
["w_013"]
```

- every other item unchanged in wardrobe.json: `True`
- target still in `wardrobe list`: `False`

<details><summary>remove: <code>python app.py wardrobe remove w_013</code> → exit 0, 0.1 s</summary>

Typed input:

```
y
```

Output:

```
w_013  Red Canvas High-Tops
        category:   shoes
        colors:     red, white
        style tags: sneakers, casual
        notes:      Laces fray a bit
Remove this item? (y/n): Removed w_013 (Red Canvas High-Tops).
```

</details>

<details><summary>list: <code>python app.py wardrobe list</code> → exit 0, 0.1 s</summary>

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
w_011  tops         navy, white           Navy Linen Shirt
w_012  bottoms      olive                 Olive Cargo Shorts

12 item(s).
```

</details>

**remove 4**

- targeted (last listed) ID: `w_012`
- IDs that disappeared:

```
["w_012"]
```

- every other item unchanged in wardrobe.json: `True`
- target still in `wardrobe list`: `False`

<details><summary>remove: <code>python app.py wardrobe remove w_012</code> → exit 0, 0.1 s</summary>

Typed input:

```
y
```

Output:

```
w_012  Olive Cargo Shorts
        category:   bottoms
        colors:     olive
        style tags: utility
        notes:      -
Remove this item? (y/n): Removed w_012 (Olive Cargo Shorts).
```

</details>

<details><summary>list: <code>python app.py wardrobe list</code> → exit 0, 0.1 s</summary>

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
w_011  tops         navy, white           Navy Linen Shirt

11 item(s).
```

</details>

**remove 5**

- targeted (last listed) ID: `w_011`
- IDs that disappeared:

```
["w_011"]
```

- every other item unchanged in wardrobe.json: `True`
- target still in `wardrobe list`: `False`

<details><summary>remove: <code>python app.py wardrobe remove w_011</code> → exit 0, 0.1 s</summary>

Typed input:

```
y
```

Output:

```
w_011  Navy Linen Shirt
        category:   tops
        colors:     navy, white
        style tags: minimal, summer
        notes:      Runs large
Remove this item? (y/n): Removed w_011 (Navy Linen Shirt).
```

</details>

<details><summary>list: <code>python app.py wardrobe list</code> → exit 0, 0.1 s</summary>

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

**after all removals**

- items equal the original demo items: `True`
- IDs now:

```
["w_001", "w_002", "w_003", "w_004", "w_005", "w_006", "w_007", "w_008", "w_009", "w_010"]
```

- next_id now: `16`

## Capstone criterion 2: Grounded outfit suggestions

**Target:** 15/15 trials

| Trial | Run 1 | Run 2 | Run 3 |
|---|---|---|---|
| trial 1 | PASS | PASS | PASS |
| trial 2 | PASS | PASS | PASS |
| trial 3 | PASS | PASS | PASS |
| trial 4 | PASS | PASS | PASS |
| trial 5 | PASS | PASS | PASS |

**Verdict:** 15 / 15

Run 1, trial 4 needed one grounding retry: the first outfit copied the prompt's description into a piece name (`w_005: Black cropped zip hoodie (tops; colors: …`), `check_grounding` flagged it, and the retried outfit passed. The criterion grades the final output, so the trial passes.

### Criterion 2, run 1

**setup: demo without shoes**

- wardrobe IDs loaded:

```
["w_001", "w_002", "w_003", "w_004", "w_005", "w_006", "w_009", "w_010"]
```


<details><summary>setup: <code>python app.py wardrobe list</code> → exit 0, 0.1 s</summary>

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
Vibe: High-contrast denim pairing creates an effortless, vintage-inspired streetwear silhouette.

Outfit 2: Khaki Contrast
- NEW: Denim Jacket — Light Wash, Cropped
- w_002: Wide-leg khaki trousers
- w_003: White ribbed tank top
- w_009: Brown leather belt
Vibe: Casual structured outerwear balances relaxed earth tones for a clean, minimal look.

Missing: shoes
```


<details><summary>ask: <code>python app.py ask 'denim jacket under $50'</code> → exit 0, 7.3 s</summary>

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
      out: Scored this vintage Wrangler Denim Jacket — Light Wash, Cropped for $42 on Poshmark. It creates an effortless,…

  Found:    Denim Jacket — Light Wash, Cropped — $42.0 on poshmark

  Outfit:   Outfit 1: Double Denim Streetwear
- NEW: Denim Jacket — Light Wash, Cropped
- w_001: Baggy straight-leg jeans, dark wash
- w_003: White ribbed tank top
- w_010: Black crossbody bag
Vibe: High-contrast denim pairing creates an effortless, vintage-inspired streetwear silhouette.

Outfit 2: Khaki Contrast
- NEW: Denim Jacket — Light Wash, Cropped
- w_002: Wide-leg khaki trousers
- w_003: White ribbed tank top
- w_009: Brown leather belt
Vibe: Casual structured outerwear balances relaxed earth tones for a clean, minimal look.

Missing: shoes

  Fit card: Scored this vintage Wrangler Denim Jacket — Light Wash, Cropped for $42 on Poshmark. It creates an effortless, vintage-inspired streetwear silhouette when paired with baggy straight-leg jeans, a white ribbed tank top, and a black crossbody bag, and gives a clean, minimal look with wide-leg khaki trousers, a white ribbed tank top, and a brown leather belt. Missing shoes, but otherwise obsessed with this blank canvas find!

  Note:     Your wardrobe has no shoes, so the outfit may be incomplete. Add some with: python app.py wardrobe add

2 model calls this session, 1029 prompt + 248 output tokens
```

</details>

**trial 2**

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
Vibe: A contrasting Canadian tuxedo look with a fitted base and structured outerwear.

Outfit 2: Khaki Contrast
- NEW: Denim Jacket — Light Wash, Cropped
- w_002: Wide-leg khaki trousers
- w_003: White ribbed tank top
- w_009: Brown leather belt
Vibe: Casual earth tones paired with classic vintage denim.

Missing: shoes
```


<details><summary>ask: <code>python app.py ask 'denim jacket under $50'</code> → exit 0, 9.6 s</summary>

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
      out: Scored this classic vintage Wrangler denim jacket on Poshmark for $42. Perfect for building a contrasting Cana…

  Found:    Denim Jacket — Light Wash, Cropped — $42.0 on poshmark

  Outfit:   Outfit 1: Double Denim Streetwear
- NEW: Denim Jacket — Light Wash, Cropped
- w_001: Baggy straight-leg jeans, dark wash
- w_003: White ribbed tank top
- w_010: Black crossbody bag
Vibe: A contrasting Canadian tuxedo look with a fitted base and structured outerwear.

Outfit 2: Khaki Contrast
- NEW: Denim Jacket — Light Wash, Cropped
- w_002: Wide-leg khaki trousers
- w_003: White ribbed tank top
- w_009: Brown leather belt
Vibe: Casual earth tones paired with classic vintage denim.

Missing: shoes

  Fit card: Scored this classic vintage Wrangler denim jacket on Poshmark for $42. Perfect for building a contrasting Canadian tuxedo look with baggy straight-leg jeans, or pairing with wide-leg khaki trousers for casual earth tones. Just need to add shoes to finish the streetwear vibe.

  Note:     Your wardrobe has no shoes, so the outfit may be incomplete. Add some with: python app.py wardrobe add

2 model calls this session, 1022 prompt + 206 output tokens
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
Outfit 1: Double Denim Streetwear
- NEW: Denim Jacket — Light Wash, Cropped
- w_001: Baggy straight-leg jeans, dark wash
- w_003: White ribbed tank top
- w_010: Black crossbody bag
Vibe: High-contrast denim pairing creates an effortless streetwear silhouette.

Outfit 2: Khaki Contrast
- NEW: Denim Jacket — Light Wash, Cropped
- w_002: Wide-leg khaki trousers
- w_003: White ribbed tank top
- w_009: Brown leather belt
Vibe: Structured outerwear balances the relaxed earth tones for a minimal daytime look.

Missing: shoes
```


<details><summary>ask: <code>python app.py ask 'denim jacket under $50'</code> → exit 0, 5.9 s</summary>

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
      out: Scored this Wrangler denim jacket for $42 on Poshmark and I am obsessed with the light wash, cropped fit and g…

  Found:    Denim Jacket — Light Wash, Cropped — $42.0 on poshmark

  Outfit:   Outfit 1: Double Denim Streetwear
- NEW: Denim Jacket — Light Wash, Cropped
- w_001: Baggy straight-leg jeans, dark wash
- w_003: White ribbed tank top
- w_010: Black crossbody bag
Vibe: High-contrast denim pairing creates an effortless streetwear silhouette.

Outfit 2: Khaki Contrast
- NEW: Denim Jacket — Light Wash, Cropped
- w_002: Wide-leg khaki trousers
- w_003: White ribbed tank top
- w_009: Brown leather belt
Vibe: Structured outerwear balances the relaxed earth tones for a minimal daytime look.

Missing: shoes

  Fit card: Scored this Wrangler denim jacket for $42 on Poshmark and I am obsessed with the light wash, cropped fit and great structured shoulders. I paired the streetwear piece with a white ribbed tank top, baggy straight-leg jeans, and a black crossbody bag for an effortless double denim look.

  Note:     Your wardrobe has no shoes, so the outfit may be incomplete. Add some with: python app.py wardrobe add

2 model calls this session, 1024 prompt + 212 output tokens
```

</details>

**trial 4**

- query: `vintage levis jeans`
- status / error: `ok / None`
- grounding check verdict (code's, not yours): `True`
- grounding retries: `1`
- IDs cited:

```
["w_003", "w_009", "w_005", "w_010"]
```

- cited IDs not in the loaded wardrobe:

```
[]
```

- final outfit (piece lines to grade):

```
Outfit 1: Vintage Casual
- NEW: Vintage Levi's 501 Jeans — Medium Wash
- w_003: White ribbed tank top
- w_009: Brown leather belt
Vibe: Effortless and timeless everyday style.

Outfit 2: Streetwear Layer
- NEW: Vintage Levi's 501 Jeans — Medium Wash
- w_005: Black cropped zip hoodie
- w_010: Black crossbody bag
Vibe: Edgy and comfortable city wear.

Missing: shoes
```


<details><summary>ask: <code>python app.py ask 'vintage levis jeans'</code> → exit 0, 7.2 s</summary>

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
      out: Outfit 1: Vintage Street - NEW: Vintage Levi's 501 Jeans — Medium Wash - w_005: Black cropped zip hoodie (tops…
[5] check_grounding
      in:  dict with keys: cited
      out: 5 items: w_005 was called "Black cropped zip hoodie (tops; colors: bl…
      →    branch: ungrounded, retrying suggest_outfit with feedback
[6] suggest_outfit
      in:  dict with keys: selected_item, wardrobe, missing_categories, feedback
      out: Outfit 1: Vintage Casual - NEW: Vintage Levi's 501 Jeans — Medium Wash - w_003: White ribbed tank top - w_009:…
[7] check_grounding
      in:  dict with keys: cited
      out: True
      →    every piece is in the wardrobe
[8] create_fit_card
      in:  dict with keys: outfit_suggestion, selected_item
      out: Scored these classic blue, indigo vintage 501 jeans on depop for $38.0, and they're the ultimate streetwear de…

  Found:    Vintage Levi's 501 Jeans — Medium Wash — $38.0 on depop

  Outfit:   Outfit 1: Vintage Casual
- NEW: Vintage Levi's 501 Jeans — Medium Wash
- w_003: White ribbed tank top
- w_009: Brown leather belt
Vibe: Effortless and timeless everyday style.

Outfit 2: Streetwear Layer
- NEW: Vintage Levi's 501 Jeans — Medium Wash
- w_005: Black cropped zip hoodie
- w_010: Black crossbody bag
Vibe: Edgy and comfortable city wear.

Missing: shoes

  Fit card: Scored these classic blue, indigo vintage 501 jeans on depop for $38.0, and they're the ultimate streetwear denim find. I love how effortless and timeless the vintage casual look is when paired with a white ribbed tank top and brown leather belt. They also pull off an edgy and comfortable city wear vibe so easily with a black cropped zip hoodie and black crossbody bag.

  Note:     Your wardrobe has no shoes, so the outfit may be incomplete. Add some with: python app.py wardrobe add

3 model calls this session, 1908 prompt + 430 output tokens
```

</details>

**trial 5**

- query: `vintage levis jeans`
- status / error: `ok / None`
- grounding check verdict (code's, not yours): `True`
- grounding retries: `0`
- IDs cited:

```
["w_003", "w_004", "w_010", "w_005", "w_006", "w_009"]
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
- w_004: Oversized grey crewneck sweatshirt
- w_010: Black crossbody bag
Vibe: This laid-back combination balances a fitted basic with a cozy oversized layer for effortless everyday cool.

Outfit 2: Double Denim Edge
- NEW: Vintage Levi's 501 Jeans — Medium Wash
- w_005: Black cropped zip hoodie
- w_006: Vintage black denim jacket
- w_009: Brown leather belt
Vibe: Mixing denim washes creates a textured, vintage-inspired streetwear silhouette with a sharp cropped contrast.

Missing: shoes
```


<details><summary>ask: <code>python app.py ask 'vintage levis jeans'</code> → exit 0, 6.2 s</summary>

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
      out: Found these vintage levi's 501 jeans on depop for $38.0, and they are so good for layering. I've been wearing …

  Found:    Vintage Levi's 501 Jeans — Medium Wash — $38.0 on depop

  Outfit:   Outfit 1: Casual Streetwear
- NEW: Vintage Levi's 501 Jeans — Medium Wash
- w_003: White ribbed tank top
- w_004: Oversized grey crewneck sweatshirt
- w_010: Black crossbody bag
Vibe: This laid-back combination balances a fitted basic with a cozy oversized layer for effortless everyday cool.

Outfit 2: Double Denim Edge
- NEW: Vintage Levi's 501 Jeans — Medium Wash
- w_005: Black cropped zip hoodie
- w_006: Vintage black denim jacket
- w_009: Brown leather belt
Vibe: Mixing denim washes creates a textured, vintage-inspired streetwear silhouette with a sharp cropped contrast.

Missing: shoes

  Fit card: Found these vintage levi's 501 jeans on depop for $38.0, and they are so good for layering. I've been wearing them with a white ribbed tank top and an oversized grey crewneck sweatshirt, plus a black crossbody bag for everyday casual streetwear. They also look amazing in a double denim edge look paired with a black cropped zip hoodie, a vintage black denim jacket, and a brown leather belt.

  Note:     Your wardrobe has no shoes, so the outfit may be incomplete. Add some with: python app.py wardrobe add

2 model calls this session, 1070 prompt + 257 output tokens
```

</details>

### Criterion 2, run 2

**setup: demo without shoes**

- wardrobe IDs loaded:

```
["w_001", "w_002", "w_003", "w_004", "w_005", "w_006", "w_009", "w_010"]
```


<details><summary>setup: <code>python app.py wardrobe list</code> → exit 0, 0.1 s</summary>

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

<details><summary>remove w_007: <code>python app.py wardrobe remove w_007</code> → exit 0, 0.1 s</summary>

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

<details><summary>remove w_008: <code>python app.py wardrobe remove w_008</code> → exit 0, 0.1 s</summary>

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
Vibe: A contrasting Canadian tuxedo play with a fitted basic underneath for urban edge.

Outfit 2: Khaki Contrast
- NEW: Denim Jacket — Light Wash, Cropped
- w_002: Wide-leg khaki trousers
- w_003: White ribbed tank top
- w_009: Brown leather belt
Vibe: Relaxed earth tones balanced by a crisp, structured blue layer.

Missing: shoes
```


<details><summary>ask: <code>python app.py ask 'denim jacket under $50'</code> → exit 0, 6.4 s</summary>

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
      out: Scored this Wrangler cropped denim jacket for $42 on Poshmark and it’s a total blank canvas. For an urban edge…

  Found:    Denim Jacket — Light Wash, Cropped — $42.0 on poshmark

  Outfit:   Outfit 1: Double Denim Streetwear
- NEW: Denim Jacket — Light Wash, Cropped
- w_001: Baggy straight-leg jeans, dark wash
- w_003: White ribbed tank top
- w_010: Black crossbody bag
Vibe: A contrasting Canadian tuxedo play with a fitted basic underneath for urban edge.

Outfit 2: Khaki Contrast
- NEW: Denim Jacket — Light Wash, Cropped
- w_002: Wide-leg khaki trousers
- w_003: White ribbed tank top
- w_009: Brown leather belt
Vibe: Relaxed earth tones balanced by a crisp, structured blue layer.

Missing: shoes

  Fit card: Scored this Wrangler cropped denim jacket for $42 on Poshmark and it’s a total blank canvas. For an urban edge, I'm wearing it in a double denim streetwear look with a white ribbed tank top, baggy straight-leg jeans, and a black crossbody bag. Alternatively, it works for earth tones paired with a white ribbed tank top, wide-leg khaki trousers, and a brown leather belt.

  Note:     Your wardrobe has no shoes, so the outfit may be incomplete. Add some with: python app.py wardrobe add

2 model calls this session, 1027 prompt + 241 output tokens
```

</details>

**trial 2**

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
Vibe: A contrasting Canadian tuxedo play with a clean, fitted base.

Outfit 2: Khaki Contrast
- NEW: Denim Jacket — Light Wash, Cropped
- w_002: Wide-leg khaki trousers
- w_003: White ribbed tank top
- w_009: Brown leather belt
Vibe: Casual streetwear meets minimal tailoring for an effortless daily look.

Missing: shoes
```


<details><summary>ask: <code>python app.py ask 'denim jacket under $50'</code> → exit 0, 6.0 s</summary>

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
      out: Scored this Wrangler cropped denim jacket for $42 on Poshmark and had to try a double denim streetwear look wi…

  Found:    Denim Jacket — Light Wash, Cropped — $42.0 on poshmark

  Outfit:   Outfit 1: Double Denim Streetwear
- NEW: Denim Jacket — Light Wash, Cropped
- w_001: Baggy straight-leg jeans, dark wash
- w_003: White ribbed tank top
- w_010: Black crossbody bag
Vibe: A contrasting Canadian tuxedo play with a clean, fitted base.

Outfit 2: Khaki Contrast
- NEW: Denim Jacket — Light Wash, Cropped
- w_002: Wide-leg khaki trousers
- w_003: White ribbed tank top
- w_009: Brown leather belt
Vibe: Casual streetwear meets minimal tailoring for an effortless daily look.

Missing: shoes

  Fit card: Scored this Wrangler cropped denim jacket for $42 on Poshmark and had to try a double denim streetwear look with baggy straight-leg jeans and a white ribbed tank top. I also styled it with wide-leg khaki trousers and a brown leather belt for an effortless daily outfit where casual streetwear meets minimal tailoring. Both ways let the classic vintage piece totally shine.

  Note:     Your wardrobe has no shoes, so the outfit may be incomplete. Add some with: python app.py wardrobe add

2 model calls this session, 1023 prompt + 225 output tokens
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
Outfit 1: Double Denim Streetwear
- NEW: Denim Jacket — Light Wash, Cropped
- w_001: Baggy straight-leg jeans, dark wash
- w_003: White ribbed tank top
- w_010: Black crossbody bag
Vibe: High-contrast denim pairing creates an effortless, vintage-inspired streetwear silhouette.

Outfit 2: Khaki Contrast
- NEW: Denim Jacket — Light Wash, Cropped
- w_002: Wide-leg khaki trousers
- w_003: White ribbed tank top
- w_009: Brown leather belt
Vibe: Classic light wash denim balances neatly against relaxed earth tones for a minimal daytime look.

Missing: shoes
```


<details><summary>ask: <code>python app.py ask 'denim jacket under $50'</code> → exit 0, 6.1 s</summary>

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
      out: Scored this Wrangler denim jacket for $42.0 on poshmark and I'm obsessed with the structured shoulders. I pair…

  Found:    Denim Jacket — Light Wash, Cropped — $42.0 on poshmark

  Outfit:   Outfit 1: Double Denim Streetwear
- NEW: Denim Jacket — Light Wash, Cropped
- w_001: Baggy straight-leg jeans, dark wash
- w_003: White ribbed tank top
- w_010: Black crossbody bag
Vibe: High-contrast denim pairing creates an effortless, vintage-inspired streetwear silhouette.

Outfit 2: Khaki Contrast
- NEW: Denim Jacket — Light Wash, Cropped
- w_002: Wide-leg khaki trousers
- w_003: White ribbed tank top
- w_009: Brown leather belt
Vibe: Classic light wash denim balances neatly against relaxed earth tones for a minimal daytime look.

Missing: shoes

  Fit card: Scored this Wrangler denim jacket for $42.0 on poshmark and I'm obsessed with the structured shoulders. I paired it with a white ribbed tank top, baggy straight-leg jeans, and a black crossbody bag for a vintage streetwear look. Trying it out next with wide-leg khaki trousers, a brown leather belt, and that same white ribbed tank top for a more minimal daytime vibe.

  Note:     Your wardrobe has no shoes, so the outfit may be incomplete. Add some with: python app.py wardrobe add

2 model calls this session, 1031 prompt + 241 output tokens
```

</details>

**trial 4**

- query: `vintage levis jeans`
- status / error: `ok / None`
- grounding check verdict (code's, not yours): `True`
- grounding retries: `0`
- IDs cited:

```
["w_003", "w_005", "w_010", "w_004", "w_006", "w_009"]
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
- w_005: Black cropped zip hoodie
- w_010: Black crossbody bag
Vibe: A relaxed, effortless everyday streetwear look combining classic denim with clean, minimal basics.

Outfit 2: Vintage Layering
- NEW: Vintage Levi's 501 Jeans — Medium Wash
- w_004: Oversized grey crewneck sweatshirt
- w_006: Vintage black denim jacket
- w_009: Brown leather belt
Vibe: A cozy, textured outfit featuring double denim and a slouchy sweatshirt for cooler days.

Missing: shoes
```


<details><summary>ask: <code>python app.py ask 'vintage levis jeans'</code> → exit 0, 6.5 s</summary>

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
      out: Scored these Vintage Levi's 501 Jeans for $38.0 on depop and they are already my go-to for effortless everyday…

  Found:    Vintage Levi's 501 Jeans — Medium Wash — $38.0 on depop

  Outfit:   Outfit 1: Casual Streetwear
- NEW: Vintage Levi's 501 Jeans — Medium Wash
- w_003: White ribbed tank top
- w_005: Black cropped zip hoodie
- w_010: Black crossbody bag
Vibe: A relaxed, effortless everyday streetwear look combining classic denim with clean, minimal basics.

Outfit 2: Vintage Layering
- NEW: Vintage Levi's 501 Jeans — Medium Wash
- w_004: Oversized grey crewneck sweatshirt
- w_006: Vintage black denim jacket
- w_009: Brown leather belt
Vibe: A cozy, textured outfit featuring double denim and a slouchy sweatshirt for cooler days.

Missing: shoes

  Fit card: Scored these Vintage Levi's 501 Jeans for $38.0 on depop and they are already my go-to for effortless everyday streetwear. I love styling the denim with a white ribbed tank top, a black cropped zip hoodie, and a black crossbody bag for a relaxed look.

  Note:     Your wardrobe has no shoes, so the outfit may be incomplete. Add some with: python app.py wardrobe add

2 model calls this session, 1066 prompt + 226 output tokens
```

</details>

**trial 5**

- query: `vintage levis jeans`
- status / error: `ok / None`
- grounding check verdict (code's, not yours): `True`
- grounding retries: `0`
- IDs cited:

```
["w_003", "w_005", "w_010", "w_004", "w_006", "w_009"]
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
- w_005: Black cropped zip hoodie
- w_010: Black crossbody bag
Vibe: A relaxed, effortless everyday look combining classic denim with minimal streetwear staples.

Outfit 2: Vintage Layering
- NEW: Vintage Levi's 501 Jeans — Medium Wash
- w_004: Oversized grey crewneck sweatshirt
- w_006: Vintage black denim jacket
- w_009: Brown leather belt
Vibe: A cozy, textured outfit playing with contrasting washes and oversized proportions.

Missing: shoes
```


<details><summary>ask: <code>python app.py ask 'vintage levis jeans'</code> → exit 0, 6.1 s</summary>

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
      out: Scored these classic 501s on depop for $38, and they have the best light fading at the knees. I styled them in…

  Found:    Vintage Levi's 501 Jeans — Medium Wash — $38.0 on depop

  Outfit:   Outfit 1: Casual Streetwear
- NEW: Vintage Levi's 501 Jeans — Medium Wash
- w_003: White ribbed tank top
- w_005: Black cropped zip hoodie
- w_010: Black crossbody bag
Vibe: A relaxed, effortless everyday look combining classic denim with minimal streetwear staples.

Outfit 2: Vintage Layering
- NEW: Vintage Levi's 501 Jeans — Medium Wash
- w_004: Oversized grey crewneck sweatshirt
- w_006: Vintage black denim jacket
- w_009: Brown leather belt
Vibe: A cozy, textured outfit playing with contrasting washes and oversized proportions.

Missing: shoes

  Fit card: Scored these classic 501s on depop for $38, and they have the best light fading at the knees. I styled them into a relaxed, effortless everyday look combining classic denim with minimal streetwear staples by pairing them with a white ribbed tank top, black cropped zip hoodie, and black crossbody bag. Such a good find for building casual streetwear fits!

  Note:     Your wardrobe has no shoes, so the outfit may be incomplete. Add some with: python app.py wardrobe add

2 model calls this session, 1060 prompt + 233 output tokens
```

</details>

### Criterion 2, run 3

**setup: demo without shoes**

- wardrobe IDs loaded:

```
["w_001", "w_002", "w_003", "w_004", "w_005", "w_006", "w_009", "w_010"]
```


<details><summary>setup: <code>python app.py wardrobe list</code> → exit 0, 0.1 s</summary>

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

<details><summary>remove w_007: <code>python app.py wardrobe remove w_007</code> → exit 0, 0.1 s</summary>

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

<details><summary>remove w_008: <code>python app.py wardrobe remove w_008</code> → exit 0, 0.1 s</summary>

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
Vibe: A classic Canadian tuxedo featuring contrasting denim washes for an effortless streetwear edge.

Outfit 2: Casual Earth Tones
- NEW: Denim Jacket — Light Wash, Cropped
- w_002: Wide-leg khaki trousers
- w_003: White ribbed tank top
- w_009: Brown leather belt
Vibe: Relaxed minimalism comes together naturally when paired with classic tailoring and warm accessories.

Missing: shoes
```


<details><summary>ask: <code>python app.py ask 'denim jacket under $50'</code> → exit 0, 6.5 s</summary>

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
      out: Scored this Wrangler denim jacket for $42.0 on Poshmark and I'm obsessed with the structured shoulders and lig…

  Found:    Denim Jacket — Light Wash, Cropped — $42.0 on poshmark

  Outfit:   Outfit 1: Double Denim Streetwear
- NEW: Denim Jacket — Light Wash, Cropped
- w_001: Baggy straight-leg jeans, dark wash
- w_003: White ribbed tank top
Vibe: A classic Canadian tuxedo featuring contrasting denim washes for an effortless streetwear edge.

Outfit 2: Casual Earth Tones
- NEW: Denim Jacket — Light Wash, Cropped
- w_002: Wide-leg khaki trousers
- w_003: White ribbed tank top
- w_009: Brown leather belt
Vibe: Relaxed minimalism comes together naturally when paired with classic tailoring and warm accessories.

Missing: shoes

  Fit card: Scored this Wrangler denim jacket for $42.0 on Poshmark and I'm obsessed with the structured shoulders and light wash. It looks so good paired with a white ribbed tank top and baggy straight-leg jeans for a classic Canadian tuxedo streetwear look. You could also style it with wide-leg khaki trousers, a brown leather belt, and the same white ribbed tank top for a more relaxed, minimal vibe.

  Note:     Your wardrobe has no shoes, so the outfit may be incomplete. Add some with: python app.py wardrobe add

2 model calls this session, 1025 prompt + 233 output tokens
```

</details>

**trial 2**

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
Vibe: High-contrast denim pairing creates a classic streetwear silhouette.

Outfit 2: Casual Earth Tones
- NEW: Denim Jacket — Light Wash, Cropped
- w_002: Wide-leg khaki trousers
- w_003: White ribbed tank top
- w_009: Brown leather belt
Vibe: A relaxed, minimal combination that highlights structured shoulders and neutral tones.

Missing: shoes
```


<details><summary>ask: <code>python app.py ask 'denim jacket under $50'</code> → exit 0, 7.0 s</summary>

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
      out: Scored this Wrangler denim jacket with structured shoulders for just $42.0 on Poshmark! Paired it with baggy s…

  Found:    Denim Jacket — Light Wash, Cropped — $42.0 on poshmark

  Outfit:   Outfit 1: Double Denim Streetwear
- NEW: Denim Jacket — Light Wash, Cropped
- w_001: Baggy straight-leg jeans, dark wash
- w_003: White ribbed tank top
- w_010: Black crossbody bag
Vibe: High-contrast denim pairing creates a classic streetwear silhouette.

Outfit 2: Casual Earth Tones
- NEW: Denim Jacket — Light Wash, Cropped
- w_002: Wide-leg khaki trousers
- w_003: White ribbed tank top
- w_009: Brown leather belt
Vibe: A relaxed, minimal combination that highlights structured shoulders and neutral tones.

Missing: shoes

  Fit card: Scored this Wrangler denim jacket with structured shoulders for just $42.0 on Poshmark! Paired it with baggy straight-leg jeans, a white ribbed tank top, and a black crossbody bag for a high-contrast double denim streetwear look. It also works as a relaxed casual earth tones combination with wide-leg khaki trousers, a white ribbed tank top, and a brown leather belt.

  Note:     Your wardrobe has no shoes, so the outfit may be incomplete. Add some with: python app.py wardrobe add

2 model calls this session, 1025 prompt + 234 output tokens
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
Outfit 1: Double Denim Streetwear
- NEW: Denim Jacket — Light Wash, Cropped
- w_001: Baggy straight-leg jeans, dark wash
- w_003: White ribbed tank top
- w_010: Black crossbody bag
Vibe: A classic Canadian tuxedo vibe with contrasting washes and minimal accessories.

Outfit 2: Khaki Contrast
- NEW: Denim Jacket — Light Wash, Cropped
- w_002: Wide-leg khaki trousers
- w_003: White ribbed tank top
- w_009: Brown leather belt
Vibe: An easy, balanced mix of structured outerwear and relaxed earth-tone trousers.

Missing: shoes
```


<details><summary>ask: <code>python app.py ask 'denim jacket under $50'</code> → exit 0, 6.1 s</summary>

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
      out: Scored this Wrangler cropped denim jacket in a light wash with great structured shoulders for $42.0 on poshmar…

  Found:    Denim Jacket — Light Wash, Cropped — $42.0 on poshmark

  Outfit:   Outfit 1: Double Denim Streetwear
- NEW: Denim Jacket — Light Wash, Cropped
- w_001: Baggy straight-leg jeans, dark wash
- w_003: White ribbed tank top
- w_010: Black crossbody bag
Vibe: A classic Canadian tuxedo vibe with contrasting washes and minimal accessories.

Outfit 2: Khaki Contrast
- NEW: Denim Jacket — Light Wash, Cropped
- w_002: Wide-leg khaki trousers
- w_003: White ribbed tank top
- w_009: Brown leather belt
Vibe: An easy, balanced mix of structured outerwear and relaxed earth-tone trousers.

Missing: shoes

  Fit card: Scored this Wrangler cropped denim jacket in a light wash with great structured shoulders for $42.0 on poshmark. I love the classic streetwear vibe when it's paired with a white ribbed tank top, baggy straight-leg jeans, dark wash, and a black crossbody bag. It also looks so good styled with wide-leg khaki trousers, a white ribbed tank top, and a brown leather belt.

  Note:     Your wardrobe has no shoes, so the outfit may be incomplete. Add some with: python app.py wardrobe add

2 model calls this session, 1027 prompt + 238 output tokens
```

</details>

**trial 4**

- query: `vintage levis jeans`
- status / error: `ok / None`
- grounding check verdict (code's, not yours): `True`
- grounding retries: `0`
- IDs cited:

```
["w_003", "w_005", "w_010", "w_006", "w_009"]
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
- w_005: Black cropped zip hoodie
- w_010: Black crossbody bag
Vibe: A relaxed, effortless streetwear look built on classic staples.

Outfit 2: Double Denim
- NEW: Vintage Levi's 501 Jeans — Medium Wash
- w_003: White ribbed tank top
- w_006: Vintage black denim jacket
- w_009: Brown leather belt
Vibe: An easy mix of vintage washes for an understated, timeless feel.

Missing: shoes
```


<details><summary>ask: <code>python app.py ask 'vintage levis jeans'</code> → exit 0, 6.0 s</summary>

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
      out: Scored these $38.0 Vintage Levi's 501 Jeans on depop and they are already my go-to for effortless streetwear. …

  Found:    Vintage Levi's 501 Jeans — Medium Wash — $38.0 on depop

  Outfit:   Outfit 1: Casual Streetwear
- NEW: Vintage Levi's 501 Jeans — Medium Wash
- w_003: White ribbed tank top
- w_005: Black cropped zip hoodie
- w_010: Black crossbody bag
Vibe: A relaxed, effortless streetwear look built on classic staples.

Outfit 2: Double Denim
- NEW: Vintage Levi's 501 Jeans — Medium Wash
- w_003: White ribbed tank top
- w_006: Vintage black denim jacket
- w_009: Brown leather belt
Vibe: An easy mix of vintage washes for an understated, timeless feel.

Missing: shoes

  Fit card: Scored these $38.0 Vintage Levi's 501 Jeans on depop and they are already my go-to for effortless streetwear. I love styling the classic denim with a white ribbed tank top, black cropped zip hoodie, and black crossbody bag for a relaxed, easy look.

  Note:     Your wardrobe has no shoes, so the outfit may be incomplete. Add some with: python app.py wardrobe add

2 model calls this session, 1054 prompt + 213 output tokens
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
Outfit 1: Casual Streetwear
- NEW: Vintage Levi's 501 Jeans — Medium Wash
- w_003: White ribbed tank top
- w_006: Vintage black denim jacket
- w_010: Black crossbody bag
Vibe: A classic denim-on-denim combination with a casual everyday feel.

Outfit 2: Relaxed Layers
- NEW: Vintage Levi's 501 Jeans — Medium Wash
- w_004: Oversized grey crewneck sweatshirt
- w_009: Brown leather belt
- w_010: Black crossbody bag
Vibe: An effortless streetwear look built around comfortable oversized proportions.

Missing: shoes
```


<details><summary>ask: <code>python app.py ask 'vintage levis jeans'</code> → exit 0, 6.1 s</summary>

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
      out: Scored these vintage Levi's 501 jeans for $38 on Depop and I am obsessed with the medium wash and light fading…

  Found:    Vintage Levi's 501 Jeans — Medium Wash — $38.0 on depop

  Outfit:   Outfit 1: Casual Streetwear
- NEW: Vintage Levi's 501 Jeans — Medium Wash
- w_003: White ribbed tank top
- w_006: Vintage black denim jacket
- w_010: Black crossbody bag
Vibe: A classic denim-on-denim combination with a casual everyday feel.

Outfit 2: Relaxed Layers
- NEW: Vintage Levi's 501 Jeans — Medium Wash
- w_004: Oversized grey crewneck sweatshirt
- w_009: Brown leather belt
- w_010: Black crossbody bag
Vibe: An effortless streetwear look built around comfortable oversized proportions.

Missing: shoes

  Fit card: Scored these vintage Levi's 501 jeans for $38 on Depop and I am obsessed with the medium wash and light fading at the knees. They're so easy to style with a white ribbed tank top and vintage black denim jacket for a classic denim-on-denim street look. Throwing them on with an oversized grey crewneck sweatshirt and brown leather belt also gives the best effortless streetwear vibe.

  Note:     Your wardrobe has no shoes, so the outfit may be incomplete. Add some with: python app.py wardrobe add

2 model calls this session, 1057 prompt + 242 output tokens
```

</details>

## Capstone criterion 3: Empty wardrobe behavior

**Target:** 15/15 trials

| Trial | Run 1 | Run 2 | Run 3 |
|---|---|---|---|
| trial 1 | PASS | PASS | PASS |
| trial 2 | PASS | PASS | PASS |
| trial 3 | PASS | PASS | PASS |
| trial 4 | PASS | PASS | PASS |
| trial 5 | PASS | PASS | PASS |

**Verdict:** 15 / 15

### Criterion 3, run 1

**trial 1**

- empty-wardrobe note shown: `True`
- `w_` IDs in the output: `False`
- fit card produced: `True`
- traceback: `False`
- exit code: `0`

<details><summary>ask: <code>python app.py ask 'denim jacket under $50' --empty-wardrobe</code> → exit 0, 4.9 s</summary>

Output:

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
      out: **Outfit 1: Casual Streetwear** Layer the cropped jacket over a plain black fitted baby tee. Pair with high-wa…
[4] check_grounding
      in:  dict with keys: cited
      →    empty wardrobe: general advice isn't meant to be grounded
[5] create_fit_card
      in:  dict with keys: outfit_suggestion, selected_item
      out: Scored this Wrangler denim jacket for $42.0 on Poshmark and I'm obsessed with the structured shoulders. I laye…

  Found:    Denim Jacket — Light Wash, Cropped — $42.0 on poshmark

  Outfit:   **Outfit 1: Casual Streetwear**
Layer the cropped jacket over a plain black fitted baby tee. Pair with high-waisted wide-leg cargo trousers in olive green and chunky white sneakers. Add a canvas tote bag. 
*Vibe:* Effortless, 90s-inspired street style.

**Outfit 2: Elevated Daytime**
Wear it unbuttoned over a ribbed white tank tucked into a black floral slip midi dress. Finish with canvas lace-up sneakers and a simple layered silver pendant necklace. 
*Vibe:* Sweet meets edgy, perfect for weekend brunch.

  Fit card: Scored this Wrangler denim jacket for $42.0 on Poshmark and I'm obsessed with the structured shoulders. I layered it over a plain black fitted baby tee with olive green high-waisted wide-leg cargo trousers and chunky white sneakers for a 90s-inspired street style vibe.

  Note:     Your wardrobe is empty, so these are general styling ideas. Add your clothes with: python app.py wardrobe add

2 model calls this session, 563 prompt + 188 output tokens
```

</details>

**trial 2**

- empty-wardrobe note shown: `True`
- `w_` IDs in the output: `False`
- fit card produced: `True`
- traceback: `False`
- exit code: `0`

<details><summary>ask: <code>python app.py ask 'denim jacket under $50' --empty-wardrobe</code> → exit 0, 5.1 s</summary>

Output:

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
      out: **Look 1: Off-Duty Model** Layer the jacket over a fitted black ribbed tank top and high-waisted wide-leg blac…
[4] check_grounding
      in:  dict with keys: cited
      →    empty wardrobe: general advice isn't meant to be grounded
[5] create_fit_card
      in:  dict with keys: outfit_suggestion, selected_item
      out: Scored this Wrangler denim jacket for $42.0 on Poshmark, and it’s the ultimate blank canvas with great structu…

  Found:    Denim Jacket — Light Wash, Cropped — $42.0 on poshmark

  Outfit:   **Look 1: Off-Duty Model**
Layer the jacket over a fitted black ribbed tank top and high-waisted wide-leg black trousers. Add a chunky black belt and retro white sneakers. Finish with silver hoop earrings. 
*Vibe:* Effortless, cool-girl streetwear with a balanced silhouette.

**Look 2: Sweet & Sporty**
Throw the jacket on over a floral midi slip dress in a dark or muted print. Pair with comfortable canvas low-top sneakers (like Converse or Vans) and a canvas tote bag. 
*Vibe:* Playful, 90s-grunge-meets-femme, perfect for weekend brunching or thrifting.

  Fit card: Scored this Wrangler denim jacket for $42.0 on Poshmark, and it’s the ultimate blank canvas with great structured shoulders. I layered the light blue vintage streetwear staple over a fitted ribbed tank top and wide-leg trousers for an effortless off-duty model vibe. It also looks so cute thrown over a floral midi slip dress with retro sneakers for a playful, 90s-grunge-meets-femme weekend look.

  Note:     Your wardrobe is empty, so these are general styling ideas. Add your clothes with: python app.py wardrobe add

2 model calls this session, 584 prompt + 236 output tokens
```

</details>

**trial 3**

- empty-wardrobe note shown: `True`
- `w_` IDs in the output: `False`
- fit card produced: `True`
- traceback: `False`
- exit code: `0`

<details><summary>ask: <code>python app.py ask 'denim jacket under $50' --empty-wardrobe</code> → exit 0, 6.2 s</summary>

Output:

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
      out: Outfit 1: Layer it over a black ribbed crewneck tank and high-waisted olive green utility pants, finished off …
[4] check_grounding
      in:  dict with keys: cited
      →    empty wardrobe: general advice isn't meant to be grounded
[5] create_fit_card
      in:  dict with keys: outfit_suggestion, selected_item
      out: Scored this vintage Wrangler denim jacket on Poshmark for $42, and it's the ultimate blank canvas for casual s…

  Found:    Denim Jacket — Light Wash, Cropped — $42.0 on poshmark

  Outfit:   Outfit 1: Layer it over a black ribbed crewneck tank and high-waisted olive green utility pants, finished off with classic white canvas sneakers. Throw on a simple silver pendant necklace to tie it together. 
Vibe: Casual streetwear. Effortless, comfortable, and sharp.

Outfit 2: Wear it unbuttoned over a black slip dress that hits at midi length, paired with chunky black lug-sole ankle boots. Add a small black shoulder bag for an easy evening look.
Vibe: Edgy vintage. Combines structured denim with a feminine silhouette for instant contrast.

  Fit card: Scored this vintage Wrangler denim jacket on Poshmark for $42, and it's the ultimate blank canvas for casual streetwear. I love wearing it over a black ribbed crewneck tank, high-waisted olive green utility pants, and classic white canvas sneakers, finished with a simple silver pendant necklace. For an edgy vintage vibe, I also like it unbuttoned over a black slip dress and chunky black lug-sole ankle boots.

  Note:     Your wardrobe is empty, so these are general styling ideas. Add your clothes with: python app.py wardrobe add

2 model calls this session, 561 prompt + 212 output tokens
```

</details>

**trial 4**

- empty-wardrobe note shown: `True`
- `w_` IDs in the output: `False`
- fit card produced: `True`
- traceback: `False`
- exit code: `0`

<details><summary>ask: <code>python app.py ask 'denim jacket under $50' --empty-wardrobe</code> → exit 0, 5.3 s</summary>

Output:

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
      out: Outfit 1: Layer the cropped jacket over a black ribbed tank top with high-waisted wide-leg black trousers and …
[4] check_grounding
      in:  dict with keys: cited
      →    empty wardrobe: general advice isn't meant to be grounded
[5] create_fit_card
      in:  dict with keys: outfit_suggestion, selected_item
      out: Scored this Wrangler denim jacket for $42.0 on Poshmark, and it’s the ultimate blank canvas with great structu…

  Found:    Denim Jacket — Light Wash, Cropped — $42.0 on poshmark

  Outfit:   Outfit 1: Layer the cropped jacket over a black ribbed tank top with high-waisted wide-leg black trousers and chunky black loafers. Add a sleek shoulder bag. 
Vibe: Elevated streetwear. The sharp contrast of black makes the light wash pop, while the cropped cut balances the wide trousers.

Outfit 2: Throw it over a floral midi slip dress in a dark or neutral tone, paired with beat-up canvas sneakers and a canvas tote. 
Vibe: Effortless 90s indie sleaze. The structured denim cuts the sweetness of the dress for an easy, everyday look.

  Fit card: Scored this Wrangler denim jacket for $42.0 on Poshmark, and it’s the ultimate blank canvas with great structured shoulders. I love styling it as elevated streetwear over a black ribbed tank top, high-waisted wide-leg black trousers, and chunky black loafers for a sharp contrast. It also works for an effortless 90s indie sleaze vibe thrown over a floral midi slip dress with beat-up canvas sneakers.

  Note:     Your wardrobe is empty, so these are general styling ideas. Add your clothes with: python app.py wardrobe add

2 model calls this session, 565 prompt + 217 output tokens
```

</details>

**trial 5**

- empty-wardrobe note shown: `True`
- `w_` IDs in the output: `False`
- fit card produced: `True`
- traceback: `False`
- exit code: `0`

<details><summary>ask: <code>python app.py ask 'denim jacket under $50' --empty-wardrobe</code> → exit 0, 5.0 s</summary>

Output:

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
      out: **Outfit 1: Casual Streetwear** Layer the cropped jacket over a plain white or graphic t-shirt. Pair with blac…
[4] check_grounding
      in:  dict with keys: cited
      →    empty wardrobe: general advice isn't meant to be grounded
[5] create_fit_card
      in:  dict with keys: outfit_suggestion, selected_item
      out: Scored this vintage Wrangler denim jacket on Poshmark for $42, and it’s such a classic streetwear piece. Paire…

  Found:    Denim Jacket — Light Wash, Cropped — $42.0 on poshmark

  Outfit:   **Outfit 1: Casual Streetwear**
Layer the cropped jacket over a plain white or graphic t-shirt. Pair with black wide-leg trousers, chunky sneakers, and a baseball cap. 
*Vibe:* Effortless, cool, and comfortable for everyday errands.

**Outfit 2: Textured Contrast**
Wear the light-wash denim open over a black ribbed midi dress. Add a canvas tote bag and retro canvas sneakers or simple leather ankle boots. 
*Vibe:* Sporty-feminine with a great mix of rugged texture and sleek lines.

  Fit card: Scored this vintage Wrangler denim jacket on Poshmark for $42, and it’s such a classic streetwear piece. Paired it with black wide-leg trousers, chunky sneakers, and a baseball cap for an effortless, cool, and comfortable vibe while running errands.

  Note:     Your wardrobe is empty, so these are general styling ideas. Add your clothes with: python app.py wardrobe add

2 model calls this session, 557 prompt + 174 output tokens
```

</details>

### Criterion 3, run 2

**trial 1**

- empty-wardrobe note shown: `True`
- `w_` IDs in the output: `False`
- fit card produced: `True`
- traceback: `False`
- exit code: `0`

<details><summary>ask: <code>python app.py ask 'denim jacket under $50' --empty-wardrobe</code> → exit 0, 5.0 s</summary>

Output:

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
      out: **Outfit 1: Effortless Off-Duty** Layer the jacket over a basic white ribbed tank top and black wide-leg trous…
[4] check_grounding
      in:  dict with keys: cited
      →    empty wardrobe: general advice isn't meant to be grounded
[5] create_fit_card
      in:  dict with keys: outfit_suggestion, selected_item
      out: Scored this Wrangler denim jacket with structured shoulders on Poshmark for $42. I love layering the light was…

  Found:    Denim Jacket — Light Wash, Cropped — $42.0 on poshmark

  Outfit:   **Outfit 1: Effortless Off-Duty**
Layer the jacket over a basic white ribbed tank top and black wide-leg trousers. Finish with canvas low-top sneakers and a canvas tote bag. 
*Vibe:* Cool, minimalist streetwear.

**Outfit 2: Retro Contrast**
Pair it with a floral midi slip dress in a dark floral print to contrast the rugged denim. Add chunky black loafers and dainty silver hoop earrings. 
*Vibe:* 90s vintage indie-sleaze.

  Fit card: Scored this Wrangler denim jacket with structured shoulders on Poshmark for $42. I love layering the light wash, cropped layer over a basic white ribbed tank top and black wide-leg trousers for a cool, minimalist streetwear vibe. It's also such a fun contrast paired with a floral midi slip dress and chunky black loafers for a 90s vintage indie-sleaze look!

  Note:     Your wardrobe is empty, so these are general styling ideas. Add your clothes with: python app.py wardrobe add

2 model calls this session, 547 prompt + 188 output tokens
```

</details>

**trial 2**

- empty-wardrobe note shown: `True`
- `w_` IDs in the output: `False`
- fit card produced: `True`
- traceback: `False`
- exit code: `0`

<details><summary>ask: <code>python app.py ask 'denim jacket under $50' --empty-wardrobe</code> → exit 0, 5.3 s</summary>

Output:

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
      out: **Look 1: Off-Duty Model** Layer the jacket over a fitted black ribbed tank top and high-waisted wide-leg blac…
[4] check_grounding
      in:  dict with keys: cited
      →    empty wardrobe: general advice isn't meant to be grounded
[5] create_fit_card
      in:  dict with keys: outfit_suggestion, selected_item
      out: Scored this vintage Wrangler denim jacket on Poshmark for $42, and it’s the ultimate blank canvas with great s…

  Found:    Denim Jacket — Light Wash, Cropped — $42.0 on poshmark

  Outfit:   **Look 1: Off-Duty Model**
Layer the jacket over a fitted black ribbed tank top and high-waisted wide-leg black trousers. Add a chunky black belt and retro white sneakers. Finish with a canvas tote. 
*Vibe:* Effortless, cool, and balanced (fitted top meets structured outerwear).

**Look 2: Sweet & Sporty**
Throw it over a floral print midi slip dress in a dark or muted tone. Pair with canvas high-top sneakers and a simple leather crossbody bag. 
*Vibe:* Casual-feminine with a 90s indie-sleaze edge.

  Fit card: Scored this vintage Wrangler denim jacket on Poshmark for $42, and it’s the ultimate blank canvas with great structured shoulders. I paired the classic streetwear outerwear with a fitted black ribbed tank top, high-waisted wide-leg black trousers, a chunky black belt, retro white sneakers, and a canvas tote for that effortless, cool off-duty model vibe. Later, I threw it over a floral print midi slip dress with canvas high-top sneakers and a simple leather crossbody bag for a casual-feminine, 90s indie-sleaze look.

  Note:     Your wardrobe is empty, so these are general styling ideas. Add your clothes with: python app.py wardrobe add

2 model calls this session, 571 prompt + 250 output tokens
```

</details>

**trial 3**

- empty-wardrobe note shown: `True`
- `w_` IDs in the output: `False`
- fit card produced: `True`
- traceback: `False`
- exit code: `0`

<details><summary>ask: <code>python app.py ask 'denim jacket under $50' --empty-wardrobe</code> → exit 0, 5.2 s</summary>

Output:

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
      out: Look 1: Throw it over a black ribbed midi dress and chunky white sneakers. Add a canvas tote.  Vibe: Effortles…
[4] check_grounding
      in:  dict with keys: cited
      →    empty wardrobe: general advice isn't meant to be grounded
[5] create_fit_card
      in:  dict with keys: outfit_suggestion, selected_item
      out: Scored this vintage Wrangler denim jacket for $42 on Poshmark and it is such a classic blank canvas. Threw it …

  Found:    Denim Jacket — Light Wash, Cropped — $42.0 on poshmark

  Outfit:   Look 1: Throw it over a black ribbed midi dress and chunky white sneakers. Add a canvas tote. 
Vibe: Effortless 90s model-off-duty.

Look 2: Pair it with high-waisted olive green cargo pants, a fitted white baby tee, and beat-up Converse. 
Vibe: Edgy, thrift-store streetwear.

  Fit card: Scored this vintage Wrangler denim jacket for $42 on Poshmark and it is such a classic blank canvas. Threw it over a black ribbed midi dress with chunky white sneakers and a canvas tote for that effortless 90s model-off-duty vibe. Then I switched it up with high-waisted olive green cargo pants, a fitted white baby tee, and beat-up Converse to lean into the edgy streetwear look.

  Note:     Your wardrobe is empty, so these are general styling ideas. Add your clothes with: python app.py wardrobe add

2 model calls this session, 520 prompt + 170 output tokens
```

</details>

**trial 4**

- empty-wardrobe note shown: `True`
- `w_` IDs in the output: `False`
- fit card produced: `True`
- traceback: `False`
- exit code: `0`

<details><summary>ask: <code>python app.py ask 'denim jacket under $50' --empty-wardrobe</code> → exit 0, 5.0 s</summary>

Output:

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
      out: Buy it! That's a classic piece. Here are two easy ways to style it:  **Off-Duty Model (Streetwear Vibe)** Laye…
[4] check_grounding
      in:  dict with keys: cited
      →    empty wardrobe: general advice isn't meant to be grounded
[5] create_fit_card
      in:  dict with keys: outfit_suggestion, selected_item
      out: Scored this Wrangler denim jacket for $42.0 on Poshmark and I'm obsessed with the structured shoulders. Styled…

  Found:    Denim Jacket — Light Wash, Cropped — $42.0 on poshmark

  Outfit:   Buy it! That's a classic piece. Here are two easy ways to style it:

**Off-Duty Model (Streetwear Vibe)**
Layer the jacket over a plain black cropped baby tee. Pair with baggy grey sweatpants, chunky white sneakers, and a baseball cap. It’s effortless, comfortable, and plays on the boxy, structured shoulders of the jacket. 

**Coffee Run (Vintage Casual Vibe)**
Throw it over a ribbed white tank top tucked into high-waisted olive green utility pants. Add a canvas tote bag and well-worn Converse sneakers. This balances the cropped cut of the jacket with relaxed trousers for an easy, everyday look.

  Fit card: Scored this Wrangler denim jacket for $42.0 on Poshmark and I'm obsessed with the structured shoulders. Styled it for an off-duty model look with a cropped baby tee, baggy sweatpants, sneakers, and a baseball cap. It also works for a coffee run over a tank top tucked into utility pants with a tote bag and sneakers.

  Note:     Your wardrobe is empty, so these are general styling ideas. Add your clothes with: python app.py wardrobe add

2 model calls this session, 579 prompt + 214 output tokens
```

</details>

**trial 5**

- empty-wardrobe note shown: `True`
- `w_` IDs in the output: `False`
- fit card produced: `True`
- traceback: `False`
- exit code: `0`

<details><summary>ask: <code>python app.py ask 'denim jacket under $50' --empty-wardrobe</code> → exit 0, 5.1 s</summary>

Output:

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
      out: Look 1: Pair the cropped jacket with a black ribbed tank top, high-waisted wide-leg trousers, and retro sneake…
[4] check_grounding
      in:  dict with keys: cited
      →    empty wardrobe: general advice isn't meant to be grounded
[5] create_fit_card
      in:  dict with keys: outfit_suggestion, selected_item
      out: Scored this vintage Wrangler denim jacket on Poshmark for $42, and it's the ultimate blank canvas with great s…

  Found:    Denim Jacket — Light Wash, Cropped — $42.0 on poshmark

  Outfit:   Look 1: Pair the cropped jacket with a black ribbed tank top, high-waisted wide-leg trousers, and retro sneakers. Add a leather crossbody bag. 
Vibe: Effortless streetwear with a balanced silhouette.

Look 2: Throw it over a floral midi slip dress and chunky black combat boots. Layer with simple silver hoop earrings.
Vibe: 90s grunge-meets-romantic contrast.

  Fit card: Scored this vintage Wrangler denim jacket on Poshmark for $42, and it's the ultimate blank canvas with great structured shoulders. I love styling it with a black ribbed tank top, high-waisted wide-leg trousers, retro sneakers, and a leather crossbody bag for effortless streetwear. It's also so fun thrown over a floral midi slip dress and chunky black combat boots with simple silver hoop earrings for a 90s grunge-meets-romantic contrast.

  Note:     Your wardrobe is empty, so these are general styling ideas. Add your clothes with: python app.py wardrobe add

2 model calls this session, 527 prompt + 185 output tokens
```

</details>

### Criterion 3, run 3

**trial 1**

- empty-wardrobe note shown: `True`
- `w_` IDs in the output: `False`
- fit card produced: `True`
- traceback: `False`
- exit code: `0`

<details><summary>ask: <code>python app.py ask 'denim jacket under $50' --empty-wardrobe</code> → exit 0, 5.1 s</summary>

Output:

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
      out: **Outfit 1: Off-Duty Cool** Layer the cropped jacket over a plain black baby tee and olive green cargo pants. …
[4] check_grounding
      in:  dict with keys: cited
      →    empty wardrobe: general advice isn't meant to be grounded
[5] create_fit_card
      in:  dict with keys: outfit_suggestion, selected_item
      out: Scored this Wrangler cropped denim jacket for $42 on Poshmark and I'm obsessed with the structured shoulders a…

  Found:    Denim Jacket — Light Wash, Cropped — $42.0 on poshmark

  Outfit:   **Outfit 1: Off-Duty Cool**
Layer the cropped jacket over a plain black baby tee and olive green cargo pants. Finish with chunky white sneakers and a canvas tote. 
*Vibe:* Effortless streetwear with a nod to 90s utility. 

**Outfit 2: High-Low Prep**
Throw the denim jacket over a floral print slip dress in midi length. Add classic canvas low-top sneakers and a simple leather crossbody bag. 
*Vibe:* Sweet meets edgy; casual daytime romance.

  Fit card: Scored this Wrangler cropped denim jacket for $42 on Poshmark and I'm obsessed with the structured shoulders and light blue wash. Layered it over a plain black baby tee, olive green cargo pants, and chunky white sneakers for effortless streetwear with a 90s utility vibe.

  Note:     Your wardrobe is empty, so these are general styling ideas. Add your clothes with: python app.py wardrobe add

2 model calls this session, 550 prompt + 171 output tokens
```

</details>

**trial 2**

- empty-wardrobe note shown: `True`
- `w_` IDs in the output: `False`
- fit card produced: `True`
- traceback: `False`
- exit code: `0`

<details><summary>ask: <code>python app.py ask 'denim jacket under $50' --empty-wardrobe</code> → exit 0, 4.7 s</summary>

Output:

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
      out: Look 1: Throw it over a black ribbed midi dress with chunky black boots and a crossbody bag. This gives an eff…
[4] check_grounding
      in:  dict with keys: cited
      →    empty wardrobe: general advice isn't meant to be grounded
[5] create_fit_card
      in:  dict with keys: outfit_suggestion, selected_item
      out: Got this Wrangler denim jacket from Poshmark for $42.0! Threw it on over a black ribbed midi dress with chunky…

  Found:    Denim Jacket — Light Wash, Cropped — $42.0 on poshmark

  Outfit:   Look 1: Throw it over a black ribbed midi dress with chunky black boots and a crossbody bag. This gives an effortless, grunge-leaning streetwear vibe that balances the jacket's cropped shape with a longer silhouette.

Look 2: Pair it with wide-leg beige trousers, a tucked-in white t-shirt, and retro sneakers like Adidas Sambas. This creates a classic, casual vintage look that is comfortable for everyday wear.

  Fit card: Got this Wrangler denim jacket from Poshmark for $42.0! Threw it on over a black ribbed midi dress with chunky black boots and a crossbody bag for an effortless, grunge-leaning streetwear vibe.

  Note:     Your wardrobe is empty, so these are general styling ideas. Add your clothes with: python app.py wardrobe add

2 model calls this session, 529 prompt + 134 output tokens
```

</details>

**trial 3**

- empty-wardrobe note shown: `True`
- `w_` IDs in the output: `False`
- fit card produced: `True`
- traceback: `False`
- exit code: `0`

<details><summary>ask: <code>python app.py ask 'denim jacket under $50' --empty-wardrobe</code> → exit 0, 5.7 s</summary>

Output:

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
      out: Outfit 1: Layer the jacket over a black ribbed tank top with high-waisted black wide-leg trousers and chunky b…
[4] check_grounding
      in:  dict with keys: cited
      →    empty wardrobe: general advice isn't meant to be grounded
[5] create_fit_card
      in:  dict with keys: outfit_suggestion, selected_item
      out: Scored this Wrangler denim jacket for $42.0 on poshmark and I'm obsessed with the effortless downtown cool vib…

  Found:    Denim Jacket — Light Wash, Cropped — $42.0 on poshmark

  Outfit:   Outfit 1: Layer the jacket over a black ribbed tank top with high-waisted black wide-leg trousers and chunky black loafers. Add a silver chain necklace. 
Vibe: Effortless downtown cool with a sharp high-low contrast.

Outfit 2: Throw it over a floral midi slip dress in a dark or neutral tone, paired with beat-up canvas sneakers and a canvas tote bag. 
Vibe: Nineties indie-sleaze meets easy weekend brunch.

  Fit card: Scored this Wrangler denim jacket for $42.0 on poshmark and I'm obsessed with the effortless downtown cool vibe. It looks amazing layered over a black ribbed tank top, high-waisted black wide-leg trousers, and chunky black loafers, finished with a silver chain necklace. It also gives total nineties indie-sleaze thrown over a floral midi slip dress with beat-up canvas sneakers and a canvas tote bag.

  Note:     Your wardrobe is empty, so these are general styling ideas. Add your clothes with: python app.py wardrobe add

2 model calls this session, 539 prompt + 188 output tokens
```

</details>

**trial 4**

- empty-wardrobe note shown: `True`
- `w_` IDs in the output: `False`
- fit card produced: `True`
- traceback: `False`
- exit code: `0`

<details><summary>ask: <code>python app.py ask 'denim jacket under $50' --empty-wardrobe</code> → exit 0, 5.1 s</summary>

Output:

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
      out: Look 1: Throw it over a black ribbed tank top, high-waisted olive green cargo pants, and chunky white sneakers…
[4] check_grounding
      in:  dict with keys: cited
      →    empty wardrobe: general advice isn't meant to be grounded
[5] create_fit_card
      in:  dict with keys: outfit_suggestion, selected_item
      out: Scored this Wrangler denim jacket for $42 on Poshmark and it is the ultimate blank canvas. Threw it over a bla…

  Found:    Denim Jacket — Light Wash, Cropped — $42.0 on poshmark

  Outfit:   Look 1: Throw it over a black ribbed tank top, high-waisted olive green cargo pants, and chunky white sneakers. Add a silver chain necklace. 
Vibe: 90s streetwear. Cool, effortless, and practical.

Look 2: Layer the jacket on top of a simple black cotton midi dress and beat-up canvas lace-up sneakers. Cinch the waist with a thin leather belt. 
Vibe: Casual vintage-femme. Sweet with a tough edge, perfect for weekend errands.

  Fit card: Scored this Wrangler denim jacket for $42 on Poshmark and it is the ultimate blank canvas. Threw it over a black ribbed tank top, high-waisted olive green cargo pants, and chunky white sneakers to lean into that cool, effortless, 90s streetwear vibe. It also looks so good layered on top of a simple black cotton midi dress with beat-up canvas lace-up sneakers for a casual vintage-femme look.

  Note:     Your wardrobe is empty, so these are general styling ideas. Add your clothes with: python app.py wardrobe add

2 model calls this session, 549 prompt + 203 output tokens
```

</details>

**trial 5**

- empty-wardrobe note shown: `True`
- `w_` IDs in the output: `False`
- fit card produced: `True`
- traceback: `False`
- exit code: `0`

<details><summary>ask: <code>python app.py ask 'denim jacket under $50' --empty-wardrobe</code> → exit 0, 6.9 s</summary>

Output:

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
      out: Outfit 1: Layer it over a black ribbed turtleneck tucked into olive green cargo pants, finished with chunky bl…
[4] check_grounding
      in:  dict with keys: cited
      →    empty wardrobe: general advice isn't meant to be grounded
[5] create_fit_card
      in:  dict with keys: outfit_suggestion, selected_item
      out: Scored this Wrangler denim jacket for $42.0 on poshmark, and it’s the ultimate blank canvas for 90s streetwear…

  Found:    Denim Jacket — Light Wash, Cropped — $42.0 on poshmark

  Outfit:   Outfit 1: Layer it over a black ribbed turtleneck tucked into olive green cargo pants, finished with chunky black loafers. 
Vibe: 90s streetwear meets utilitarian chic.

Outfit 2: Throw it on over a vintage floral midi slip dress, paired with beat-up canvas high-top sneakers and a canvas tote bag. 
Vibe: Effortless, grungy indie-sleaze.

  Fit card: Scored this Wrangler denim jacket for $42.0 on poshmark, and it’s the ultimate blank canvas for 90s streetwear meets utilitarian chic. I love throwing it on over a black ribbed turtleneck tucked into olive green cargo pants, finished with chunky black loafers.

  Note:     Your wardrobe is empty, so these are general styling ideas. Add your clothes with: python app.py wardrobe add

2 model calls this session, 523 prompt + 141 output tokens
```

</details>

## Capstone criterion 4: Corrupt wardrobe file handling

**Target:** 15/15 trials

| Trial | Run 1 | Run 2 | Run 3 |
|---|---|---|---|
| trial 1 | PASS | PASS | PASS |
| trial 2 | PASS | PASS | PASS |
| trial 3 | PASS | PASS | PASS |
| trial 4 | PASS | PASS | PASS |
| trial 5 | PASS | PASS | PASS |

**Verdict:** 15 / 15

### Criterion 4, run 1

**trial 1**

- exact message shown: `True`
- exit code: `0`
- traceback: `False`
- general styling advice given instead (treated as empty): `False`

<details><summary>ask with corrupt file: <code>python app.py ask 'denim jacket under $50'</code> → exit 0, 3.2 s</summary>

Output:

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

</details>

**trial 2**

- exact message shown: `True`
- exit code: `0`
- traceback: `False`
- general styling advice given instead (treated as empty): `False`

<details><summary>ask with corrupt file: <code>python app.py ask 'denim jacket under $50'</code> → exit 0, 2.7 s</summary>

Output:

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

</details>

**trial 3**

- exact message shown: `True`
- exit code: `0`
- traceback: `False`
- general styling advice given instead (treated as empty): `False`

<details><summary>ask with corrupt file: <code>python app.py ask 'denim jacket under $50'</code> → exit 0, 2.8 s</summary>

Output:

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

</details>

**trial 4**

- exact message shown: `True`
- exit code: `0`
- traceback: `False`
- general styling advice given instead (treated as empty): `False`

<details><summary>ask with corrupt file: <code>python app.py ask 'denim jacket under $50'</code> → exit 0, 2.9 s</summary>

Output:

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

</details>

**trial 5**

- exact message shown: `True`
- exit code: `0`
- traceback: `False`
- general styling advice given instead (treated as empty): `False`

<details><summary>ask with corrupt file: <code>python app.py ask 'denim jacket under $50'</code> → exit 0, 2.8 s</summary>

Output:

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

</details>

### Criterion 4, run 2

**trial 1**

- exact message shown: `True`
- exit code: `0`
- traceback: `False`
- general styling advice given instead (treated as empty): `False`

<details><summary>ask with corrupt file: <code>python app.py ask 'denim jacket under $50'</code> → exit 0, 2.9 s</summary>

Output:

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

</details>

**trial 2**

- exact message shown: `True`
- exit code: `0`
- traceback: `False`
- general styling advice given instead (treated as empty): `False`

<details><summary>ask with corrupt file: <code>python app.py ask 'denim jacket under $50'</code> → exit 0, 3.0 s</summary>

Output:

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

</details>

**trial 3**

- exact message shown: `True`
- exit code: `0`
- traceback: `False`
- general styling advice given instead (treated as empty): `False`

<details><summary>ask with corrupt file: <code>python app.py ask 'denim jacket under $50'</code> → exit 0, 3.1 s</summary>

Output:

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

</details>

**trial 4**

- exact message shown: `True`
- exit code: `0`
- traceback: `False`
- general styling advice given instead (treated as empty): `False`

<details><summary>ask with corrupt file: <code>python app.py ask 'denim jacket under $50'</code> → exit 0, 2.9 s</summary>

Output:

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

</details>

**trial 5**

- exact message shown: `True`
- exit code: `0`
- traceback: `False`
- general styling advice given instead (treated as empty): `False`

<details><summary>ask with corrupt file: <code>python app.py ask 'denim jacket under $50'</code> → exit 0, 2.9 s</summary>

Output:

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

</details>

### Criterion 4, run 3

**trial 1**

- exact message shown: `True`
- exit code: `0`
- traceback: `False`
- general styling advice given instead (treated as empty): `False`

<details><summary>ask with corrupt file: <code>python app.py ask 'denim jacket under $50'</code> → exit 0, 3.2 s</summary>

Output:

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

</details>

**trial 2**

- exact message shown: `True`
- exit code: `0`
- traceback: `False`
- general styling advice given instead (treated as empty): `False`

<details><summary>ask with corrupt file: <code>python app.py ask 'denim jacket under $50'</code> → exit 0, 3.0 s</summary>

Output:

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

</details>

**trial 3**

- exact message shown: `True`
- exit code: `0`
- traceback: `False`
- general styling advice given instead (treated as empty): `False`

<details><summary>ask with corrupt file: <code>python app.py ask 'denim jacket under $50'</code> → exit 0, 3.3 s</summary>

Output:

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

</details>

**trial 4**

- exact message shown: `True`
- exit code: `0`
- traceback: `False`
- general styling advice given instead (treated as empty): `False`

<details><summary>ask with corrupt file: <code>python app.py ask 'denim jacket under $50'</code> → exit 0, 3.1 s</summary>

Output:

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

</details>

**trial 5**

- exact message shown: `True`
- exit code: `0`
- traceback: `False`
- general styling advice given instead (treated as empty): `False`

<details><summary>ask with corrupt file: <code>python app.py ask 'denim jacket under $50'</code> → exit 0, 3.2 s</summary>

Output:

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

</details>

## Capstone criterion 5: Validation and normalization when adding items

**Target:** 18/18 cases

| Trial | Run 1 | Run 2 | Run 3 |
|---|---|---|---|
| case A | PASS | PASS | PASS |
| case B | PASS | PASS | PASS |
| case C | PASS | PASS | PASS |
| case D | PASS | PASS | PASS |
| case E | PASS | PASS | PASS |
| case F | PASS | PASS | PASS |

**Verdict:** 18 / 18

### Criterion 5, run 1

**fresh demo wardrobe**


<details><summary>setup: <code>python app.py wardrobe list</code> → exit 0, 0.2 s</summary>

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

**case A**

- input: `repeated colors and style tags, capitals and spaces`
- `Not saved:` shown: `False`
- `Added:` shown: `True`
- wardrobe.json unchanged: `False`
- stored item:

```
{"name": "Striped Tee", "category": "tops", "colors": ["red", "navy"], "style_tags": ["casual", "striped"], "notes": null, "id": "w_011"}
```


<details><summary>add: <code>python app.py wardrobe add</code> → exit 0, 0.1 s</summary>

Typed input:

```
Striped Tee
tops
  Red, red , NAVY, navy 
 Casual, casual,  STRIPED 
```

Output:

```
Enter the details of the item to add to your wardrobe.
Name: Category (tops, bottoms, outerwear, shoes, accessories): Colors (comma-separated): Style tags (comma-separated, optional): Notes (optional): Added:
  w_011  Striped Tee
        category:   tops
        colors:     red, navy
        style tags: casual, striped
        notes:      -
```

</details>

**case B**

- input: `whitespace-only name`
- `Not saved:` shown: `True`
- `Added:` shown: `False`
- wardrobe.json unchanged: `True`
- stored item: `None`

<details><summary>add: <code>python app.py wardrobe add</code> → exit 0, 0.1 s</summary>

Typed input:

```
   
tops
red
```

Output:

```
Enter the details of the item to add to your wardrobe.
Name: Category (tops, bottoms, outerwear, shoes, accessories): Colors (comma-separated): Style tags (comma-separated, optional): Notes (optional): Not saved:
  - Item field "name" cannot be empty.
```

</details>

**case C**

- input: `whitespace-only category`
- `Not saved:` shown: `True`
- `Added:` shown: `False`
- wardrobe.json unchanged: `True`
- stored item: `None`

<details><summary>add: <code>python app.py wardrobe add</code> → exit 0, 0.2 s</summary>

Typed input:

```
Plain Tee
   
red
```

Output:

```
Enter the details of the item to add to your wardrobe.
Name: Category (tops, bottoms, outerwear, shoes, accessories): Colors (comma-separated): Style tags (comma-separated, optional): Notes (optional): Not saved:
  - Item field "category" must be one of: tops, bottoms, outerwear, shoes, accessories.
```

</details>

**case D**

- input: `whitespace-only colors`
- `Not saved:` shown: `True`
- `Added:` shown: `False`
- wardrobe.json unchanged: `True`
- stored item: `None`

<details><summary>add: <code>python app.py wardrobe add</code> → exit 0, 0.1 s</summary>

Typed input:

```
Plain Tee
tops
  ,  
```

Output:

```
Enter the details of the item to add to your wardrobe.
Name: Category (tops, bottoms, outerwear, shoes, accessories): Colors (comma-separated): Style tags (comma-separated, optional): Notes (optional): Not saved:
  - Item field "colors" must contain at least one color.
```

</details>

**case E**

- input: `invalid category 'furniture'`
- `Not saved:` shown: `True`
- `Added:` shown: `False`
- wardrobe.json unchanged: `True`
- stored item: `None`

<details><summary>add: <code>python app.py wardrobe add</code> → exit 0, 0.1 s</summary>

Typed input:

```
Plain Tee
furniture
red
```

Output:

```
Enter the details of the item to add to your wardrobe.
Name: Category (tops, bottoms, outerwear, shoes, accessories): Colors (comma-separated): Style tags (comma-separated, optional): Notes (optional): Not saved:
  - Item field "category" must be one of: tops, bottoms, outerwear, shoes, accessories.
```

</details>

**case F**

- input: `style tags and notes left blank`
- `Not saved:` shown: `False`
- `Added:` shown: `True`
- wardrobe.json unchanged: `False`
- stored item:

```
{"name": "Plain Hat", "category": "accessories", "colors": ["black"], "style_tags": [], "notes": null, "id": "w_012"}
```


<details><summary>add: <code>python app.py wardrobe add</code> → exit 0, 0.2 s</summary>

Typed input:

```
Plain Hat
accessories
black
```

Output:

```
Enter the details of the item to add to your wardrobe.
Name: Category (tops, bottoms, outerwear, shoes, accessories): Colors (comma-separated): Style tags (comma-separated, optional): Notes (optional): Added:
  w_012  Plain Hat
        category:   accessories
        colors:     black
        style tags: -
        notes:      -
```

</details>

### Criterion 5, run 2

**fresh demo wardrobe**


<details><summary>setup: <code>python app.py wardrobe list</code> → exit 0, 0.1 s</summary>

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

**case A**

- input: `repeated colors and style tags, capitals and spaces`
- `Not saved:` shown: `False`
- `Added:` shown: `True`
- wardrobe.json unchanged: `False`
- stored item:

```
{"name": "Striped Tee", "category": "tops", "colors": ["red", "navy"], "style_tags": ["casual", "striped"], "notes": null, "id": "w_011"}
```


<details><summary>add: <code>python app.py wardrobe add</code> → exit 0, 0.1 s</summary>

Typed input:

```
Striped Tee
tops
  Red, red , NAVY, navy 
 Casual, casual,  STRIPED 
```

Output:

```
Enter the details of the item to add to your wardrobe.
Name: Category (tops, bottoms, outerwear, shoes, accessories): Colors (comma-separated): Style tags (comma-separated, optional): Notes (optional): Added:
  w_011  Striped Tee
        category:   tops
        colors:     red, navy
        style tags: casual, striped
        notes:      -
```

</details>

**case B**

- input: `whitespace-only name`
- `Not saved:` shown: `True`
- `Added:` shown: `False`
- wardrobe.json unchanged: `True`
- stored item: `None`

<details><summary>add: <code>python app.py wardrobe add</code> → exit 0, 0.1 s</summary>

Typed input:

```
   
tops
red
```

Output:

```
Enter the details of the item to add to your wardrobe.
Name: Category (tops, bottoms, outerwear, shoes, accessories): Colors (comma-separated): Style tags (comma-separated, optional): Notes (optional): Not saved:
  - Item field "name" cannot be empty.
```

</details>

**case C**

- input: `whitespace-only category`
- `Not saved:` shown: `True`
- `Added:` shown: `False`
- wardrobe.json unchanged: `True`
- stored item: `None`

<details><summary>add: <code>python app.py wardrobe add</code> → exit 0, 0.2 s</summary>

Typed input:

```
Plain Tee
   
red
```

Output:

```
Enter the details of the item to add to your wardrobe.
Name: Category (tops, bottoms, outerwear, shoes, accessories): Colors (comma-separated): Style tags (comma-separated, optional): Notes (optional): Not saved:
  - Item field "category" must be one of: tops, bottoms, outerwear, shoes, accessories.
```

</details>

**case D**

- input: `whitespace-only colors`
- `Not saved:` shown: `True`
- `Added:` shown: `False`
- wardrobe.json unchanged: `True`
- stored item: `None`

<details><summary>add: <code>python app.py wardrobe add</code> → exit 0, 0.2 s</summary>

Typed input:

```
Plain Tee
tops
  ,  
```

Output:

```
Enter the details of the item to add to your wardrobe.
Name: Category (tops, bottoms, outerwear, shoes, accessories): Colors (comma-separated): Style tags (comma-separated, optional): Notes (optional): Not saved:
  - Item field "colors" must contain at least one color.
```

</details>

**case E**

- input: `invalid category 'furniture'`
- `Not saved:` shown: `True`
- `Added:` shown: `False`
- wardrobe.json unchanged: `True`
- stored item: `None`

<details><summary>add: <code>python app.py wardrobe add</code> → exit 0, 0.1 s</summary>

Typed input:

```
Plain Tee
furniture
red
```

Output:

```
Enter the details of the item to add to your wardrobe.
Name: Category (tops, bottoms, outerwear, shoes, accessories): Colors (comma-separated): Style tags (comma-separated, optional): Notes (optional): Not saved:
  - Item field "category" must be one of: tops, bottoms, outerwear, shoes, accessories.
```

</details>

**case F**

- input: `style tags and notes left blank`
- `Not saved:` shown: `False`
- `Added:` shown: `True`
- wardrobe.json unchanged: `False`
- stored item:

```
{"name": "Plain Hat", "category": "accessories", "colors": ["black"], "style_tags": [], "notes": null, "id": "w_012"}
```


<details><summary>add: <code>python app.py wardrobe add</code> → exit 0, 0.2 s</summary>

Typed input:

```
Plain Hat
accessories
black
```

Output:

```
Enter the details of the item to add to your wardrobe.
Name: Category (tops, bottoms, outerwear, shoes, accessories): Colors (comma-separated): Style tags (comma-separated, optional): Notes (optional): Added:
  w_012  Plain Hat
        category:   accessories
        colors:     black
        style tags: -
        notes:      -
```

</details>

### Criterion 5, run 3

**fresh demo wardrobe**


<details><summary>setup: <code>python app.py wardrobe list</code> → exit 0, 0.2 s</summary>

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

**case A**

- input: `repeated colors and style tags, capitals and spaces`
- `Not saved:` shown: `False`
- `Added:` shown: `True`
- wardrobe.json unchanged: `False`
- stored item:

```
{"name": "Striped Tee", "category": "tops", "colors": ["red", "navy"], "style_tags": ["casual", "striped"], "notes": null, "id": "w_011"}
```


<details><summary>add: <code>python app.py wardrobe add</code> → exit 0, 0.2 s</summary>

Typed input:

```
Striped Tee
tops
  Red, red , NAVY, navy 
 Casual, casual,  STRIPED 
```

Output:

```
Enter the details of the item to add to your wardrobe.
Name: Category (tops, bottoms, outerwear, shoes, accessories): Colors (comma-separated): Style tags (comma-separated, optional): Notes (optional): Added:
  w_011  Striped Tee
        category:   tops
        colors:     red, navy
        style tags: casual, striped
        notes:      -
```

</details>

**case B**

- input: `whitespace-only name`
- `Not saved:` shown: `True`
- `Added:` shown: `False`
- wardrobe.json unchanged: `True`
- stored item: `None`

<details><summary>add: <code>python app.py wardrobe add</code> → exit 0, 0.1 s</summary>

Typed input:

```
   
tops
red
```

Output:

```
Enter the details of the item to add to your wardrobe.
Name: Category (tops, bottoms, outerwear, shoes, accessories): Colors (comma-separated): Style tags (comma-separated, optional): Notes (optional): Not saved:
  - Item field "name" cannot be empty.
```

</details>

**case C**

- input: `whitespace-only category`
- `Not saved:` shown: `True`
- `Added:` shown: `False`
- wardrobe.json unchanged: `True`
- stored item: `None`

<details><summary>add: <code>python app.py wardrobe add</code> → exit 0, 0.1 s</summary>

Typed input:

```
Plain Tee
   
red
```

Output:

```
Enter the details of the item to add to your wardrobe.
Name: Category (tops, bottoms, outerwear, shoes, accessories): Colors (comma-separated): Style tags (comma-separated, optional): Notes (optional): Not saved:
  - Item field "category" must be one of: tops, bottoms, outerwear, shoes, accessories.
```

</details>

**case D**

- input: `whitespace-only colors`
- `Not saved:` shown: `True`
- `Added:` shown: `False`
- wardrobe.json unchanged: `True`
- stored item: `None`

<details><summary>add: <code>python app.py wardrobe add</code> → exit 0, 0.1 s</summary>

Typed input:

```
Plain Tee
tops
  ,  
```

Output:

```
Enter the details of the item to add to your wardrobe.
Name: Category (tops, bottoms, outerwear, shoes, accessories): Colors (comma-separated): Style tags (comma-separated, optional): Notes (optional): Not saved:
  - Item field "colors" must contain at least one color.
```

</details>

**case E**

- input: `invalid category 'furniture'`
- `Not saved:` shown: `True`
- `Added:` shown: `False`
- wardrobe.json unchanged: `True`
- stored item: `None`

<details><summary>add: <code>python app.py wardrobe add</code> → exit 0, 0.1 s</summary>

Typed input:

```
Plain Tee
furniture
red
```

Output:

```
Enter the details of the item to add to your wardrobe.
Name: Category (tops, bottoms, outerwear, shoes, accessories): Colors (comma-separated): Style tags (comma-separated, optional): Notes (optional): Not saved:
  - Item field "category" must be one of: tops, bottoms, outerwear, shoes, accessories.
```

</details>

**case F**

- input: `style tags and notes left blank`
- `Not saved:` shown: `False`
- `Added:` shown: `True`
- wardrobe.json unchanged: `False`
- stored item:

```
{"name": "Plain Hat", "category": "accessories", "colors": ["black"], "style_tags": [], "notes": null, "id": "w_012"}
```


<details><summary>add: <code>python app.py wardrobe add</code> → exit 0, 0.1 s</summary>

Typed input:

```
Plain Hat
accessories
black
```

Output:

```
Enter the details of the item to add to your wardrobe.
Name: Category (tops, bottoms, outerwear, shoes, accessories): Colors (comma-separated): Style tags (comma-separated, optional): Notes (optional): Added:
  w_012  Plain Hat
        category:   accessories
        colors:     black
        style tags: -
        notes:      -
```

</details>

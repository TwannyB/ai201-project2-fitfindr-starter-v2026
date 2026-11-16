# Capstone run log — before

- Produced by: `run_capstone_eval.py`, following criteria.md → "Capstone criteria"
- Each step is a real `python app.py …` command in its own process
- Runs per criterion: 3 · caching off · 9 s between asks
- When: 2026-11-15 23:27

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

<details><summary>list: <code>python app.py wardrobe list</code> → exit 0, 0.3 s</summary>

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
| trial 1 | PASS | PASS | VOID |
| trial 2 | PASS | PASS | VOID |
| trial 3 | PASS | PASS | VOID |
| trial 4 | PASS | PASS | VOID |
| trial 5 | PASS | PASS | VOID |

**Verdict:** 10 / 10 graded trials pass; run 3 (5 trials) is void, so 15/15 is not yet shown

**Run 3 is void, not failed.** Its setup step `wardrobe remove w_007` crashed with `PermissionError: [WinError 5] Access is denied` (renaming `wardrobe.json.tmp` over `wardrobe.json`), so w_007 was never removed and the agent was given a wardrobe that still had Chunky white sneakers. Every run-3 trial cites w_007, which is in the wardrobe it loaded, so the outfits are grounded in what the agent saw, but the trial the criterion describes (both shoes removed) never ran. Runs 1 and 2: every piece line cites a loaded ID with its exact saved name, no piece line lacks an ID, neither w_007 nor w_008 appears, and every outfit ends with `Missing: shoes`. Run 3 needs re-running: `python run_capstone_eval.py --criteria 2 --runs 1 --label before-rerun`.

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
Vibe: A contrasting Canadian tuxedo vibe playing with different denim washes and relaxed proportions.

Outfit 2: Casual Khaki Layer
- NEW: Denim Jacket — Light Wash, Cropped
- w_002: Wide-leg khaki trousers
- w_003: White ribbed tank top
- w_009: Brown leather belt
Vibe: A timeless, balanced mix of classic streetwear and minimal earth tones.

Missing: shoes
```


<details><summary>ask: <code>python app.py ask 'denim jacket under $50'</code> → exit 0, 7.2 s</summary>

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
Vibe: High-contrast denim pairing creates an effortless streetwear silhouette.

Outfit 2: Neutral Contrast
- NEW: Denim Jacket — Light Wash, Cropped
- w_002: Wide-leg khaki trousers
- w_003: White ribbed tank top
- w_009: Brown leather belt
Vibe: Classic light wash denim contrasts cleanly against earth-toned trousers.

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
      out: Scored this cropped Wrangler denim jacket for $42 on Poshmark and built two easy looks around it. For the stre…

  Found:    Denim Jacket — Light Wash, Cropped — $42.0 on poshmark

  Outfit:   Outfit 1: Double Denim Streetwear
- NEW: Denim Jacket — Light Wash, Cropped
- w_001: Baggy straight-leg jeans, dark wash
- w_003: White ribbed tank top
Vibe: High-contrast denim pairing creates an effortless streetwear silhouette.

Outfit 2: Neutral Contrast
- NEW: Denim Jacket — Light Wash, Cropped
- w_002: Wide-leg khaki trousers
- w_003: White ribbed tank top
- w_009: Brown leather belt
Vibe: Classic light wash denim contrasts cleanly against earth-toned trousers.

Missing: shoes

  Fit card: Scored this cropped Wrangler denim jacket for $42 on Poshmark and built two easy looks around it. For the streetwear vibe, I paired it with a white ribbed tank top and baggy straight-leg jeans for a double denim contrast. Then I switched it up with wide-leg khaki trousers, a white ribbed tank top, and a brown leather belt for an effortless neutral contrast.

  Note:     Your wardrobe has no shoes, so the outfit may be incomplete. Add some with: python app.py wardrobe add

2 model calls this session, 1017 prompt + 217 output tokens
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
Vibe: A classic double-denim look that plays with contrasting light and dark washes for effortless streetwear appeal.

Outfit 2: Khaki Contrast
- NEW: Denim Jacket — Light Wash, Cropped
- w_002: Wide-leg khaki trousers
- w_003: White ribbed tank top
- w_009: Brown leather belt
Vibe: A minimal outfit balancing structured outerwear with relaxed earth-tone trousers and classic accessories.

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
      out: Scored this cropped denim jacket with great structured shoulders from Wrangler for $42 on Poshmark. It is such…

  Found:    Denim Jacket — Light Wash, Cropped — $42.0 on poshmark

  Outfit:   Outfit 1: Double Denim Streetwear
- NEW: Denim Jacket — Light Wash, Cropped
- w_001: Baggy straight-leg jeans, dark wash
- w_003: White ribbed tank top
- w_010: Black crossbody bag
Vibe: A classic double-denim look that plays with contrasting light and dark washes for effortless streetwear appeal.

Outfit 2: Khaki Contrast
- NEW: Denim Jacket — Light Wash, Cropped
- w_002: Wide-leg khaki trousers
- w_003: White ribbed tank top
- w_009: Brown leather belt
Vibe: A minimal outfit balancing structured outerwear with relaxed earth-tone trousers and classic accessories.

Missing: shoes

  Fit card: Scored this cropped denim jacket with great structured shoulders from Wrangler for $42 on Poshmark. It is such a blank canvas and has already been on heavy rotation. I love styling it as classic streetwear with baggy straight-leg jeans and a white ribbed tank top, or keeping it minimal paired with wide-leg khaki trousers.

  Note:     Your wardrobe has no shoes, so the outfit may be incomplete. Add some with: python app.py wardrobe add

2 model calls this session, 1036 prompt + 231 output tokens
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
Vibe: Effortless streetwear layering with a vintage edge.

Outfit 2: Cozy Off-Duty
- NEW: Vintage Levi's 501 Jeans — Medium Wash
- w_004: Oversized grey crewneck sweatshirt
- w_009: Brown leather belt
- w_010: Black crossbody bag
Vibe: Relaxed and classic comfort for everyday wear.

Missing: shoes
```


<details><summary>ask: <code>python app.py ask 'vintage levis jeans'</code> → exit 0, 7.0 s</summary>

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
      out: Scored these medium wash Vintage Levi's 501 Jeans with light fading at the knees for just $38.0 on depop. I lo…

  Found:    Vintage Levi's 501 Jeans — Medium Wash — $38.0 on depop

  Outfit:   Outfit 1: Casual Streetwear
- NEW: Vintage Levi's 501 Jeans — Medium Wash
- w_003: White ribbed tank top
- w_006: Vintage black denim jacket
- w_010: Black crossbody bag
Vibe: Effortless streetwear layering with a vintage edge.

Outfit 2: Cozy Off-Duty
- NEW: Vintage Levi's 501 Jeans — Medium Wash
- w_004: Oversized grey crewneck sweatshirt
- w_009: Brown leather belt
- w_010: Black crossbody bag
Vibe: Relaxed and classic comfort for everyday wear.

Missing: shoes

  Fit card: Scored these medium wash Vintage Levi's 501 Jeans with light fading at the knees for just $38.0 on depop. I love building effortless streetwear looks with them by pairing the denim with a white ribbed tank top, a vintage black denim jacket, and a black crossbody bag. They also give off such a relaxed off-duty vibe when I switch things up with an oversized grey crewneck sweatshirt and a brown leather belt.

  Note:     Your wardrobe has no shoes, so the outfit may be incomplete. Add some with: python app.py wardrobe add

2 model calls this session, 1051 prompt + 240 output tokens
```

</details>

**trial 5**

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
Vibe: A relaxed, effortless streetwear look built for everyday comfort.

Outfit 2: Vintage Double Denim
- NEW: Vintage Levi's 501 Jeans — Medium Wash
- w_003: White ribbed tank top
- w_006: Vintage black denim jacket
- w_009: Brown leather belt
Vibe: A classic vintage combination highlighting contrasting denim washes and clean accessories.

Missing: shoes
```


<details><summary>ask: <code>python app.py ask 'vintage levis jeans'</code> → exit 0, 6.6 s</summary>

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
      out: Scored these vintage Levi's 501 jeans for $38 on Depop and I'm obsessed. I threw together a relaxed, effortles…

  Found:    Vintage Levi's 501 Jeans — Medium Wash — $38.0 on depop

  Outfit:   Outfit 1: Casual Streetwear
- NEW: Vintage Levi's 501 Jeans — Medium Wash
- w_003: White ribbed tank top
- w_005: Black cropped zip hoodie
- w_010: Black crossbody bag
Vibe: A relaxed, effortless streetwear look built for everyday comfort.

Outfit 2: Vintage Double Denim
- NEW: Vintage Levi's 501 Jeans — Medium Wash
- w_003: White ribbed tank top
- w_006: Vintage black denim jacket
- w_009: Brown leather belt
Vibe: A classic vintage combination highlighting contrasting denim washes and clean accessories.

Missing: shoes

  Fit card: Scored these vintage Levi's 501 jeans for $38 on Depop and I'm obsessed. I threw together a relaxed, effortless streetwear look with a white ribbed tank top, black cropped zip hoodie, and black crossbody bag for everyday comfort.

  Note:     Your wardrobe has no shoes, so the outfit may be incomplete. Add some with: python app.py wardrobe add

2 model calls this session, 1054 prompt + 206 output tokens
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
Vibe: A classic Canadian tuxedo effect playing with light and dark denim tones.

Outfit 2: Khaki Contrast
- NEW: Denim Jacket — Light Wash, Cropped
- w_002: Wide-leg khaki trousers
- w_003: White ribbed tank top
- w_009: Brown leather belt
Vibe: Effortless casual styling pairing structured denim with relaxed earth tones.

Missing: shoes
```


<details><summary>ask: <code>python app.py ask 'denim jacket under $50'</code> → exit 0, 6.7 s</summary>

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
      out: Scored this Wrangler denim jacket for $42 on Poshmark, and it's such a classic blank canvas with great structu…

  Found:    Denim Jacket — Light Wash, Cropped — $42.0 on poshmark

  Outfit:   Outfit 1: Double Denim Streetwear
- NEW: Denim Jacket — Light Wash, Cropped
- w_001: Baggy straight-leg jeans, dark wash
- w_003: White ribbed tank top
Vibe: A classic Canadian tuxedo effect playing with light and dark denim tones.

Outfit 2: Khaki Contrast
- NEW: Denim Jacket — Light Wash, Cropped
- w_002: Wide-leg khaki trousers
- w_003: White ribbed tank top
- w_009: Brown leather belt
Vibe: Effortless casual styling pairing structured denim with relaxed earth tones.

Missing: shoes

  Fit card: Scored this Wrangler denim jacket for $42 on Poshmark, and it's such a classic blank canvas with great structured shoulders. I'm obsessed with how the light blue crop plays against baggy straight-leg jeans and a white ribbed tank top for a double denim streetwear vibe. It also looks effortless paired with wide-leg khaki trousers, a brown leather belt, and the same white ribbed tank top.

  Note:     Your wardrobe has no shoes, so the outfit may be incomplete. Add some with: python app.py wardrobe add

2 model calls this session, 1020 prompt + 226 output tokens
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
Vibe: A contrasting Canadian tuxedo look that plays with different denim washes and relaxed proportions.

Outfit 2: Casual Khaki Contrast
- NEW: Denim Jacket — Light Wash, Cropped
- w_002: Wide-leg khaki trousers
- w_003: White ribbed tank top
- w_009: Brown leather belt
Vibe: An effortless combination of classic blue denim and relaxed neutral earth tones.

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
      out: Scored this Wrangler cropped denim jacket in a light wash with structured shoulders for $42 on Poshmark. It's …

  Found:    Denim Jacket — Light Wash, Cropped — $42.0 on poshmark

  Outfit:   Outfit 1: Double Denim Streetwear
- NEW: Denim Jacket — Light Wash, Cropped
- w_001: Baggy straight-leg jeans, dark wash
- w_003: White ribbed tank top
- w_010: Black crossbody bag
Vibe: A contrasting Canadian tuxedo look that plays with different denim washes and relaxed proportions.

Outfit 2: Casual Khaki Contrast
- NEW: Denim Jacket — Light Wash, Cropped
- w_002: Wide-leg khaki trousers
- w_003: White ribbed tank top
- w_009: Brown leather belt
Vibe: An effortless combination of classic blue denim and relaxed neutral earth tones.

Missing: shoes

  Fit card: Scored this Wrangler cropped denim jacket in a light wash with structured shoulders for $42 on Poshmark. It's a blank canvas ready to customize, and I love pairing it with a white ribbed tank top, baggy straight-leg jeans, and a black crossbody bag for a double denim streetwear look. It also works effortlessly with wide-leg khaki trousers and a brown leather belt for a casual khaki contrast.

  Note:     Your wardrobe has no shoes, so the outfit may be incomplete. Add some with: python app.py wardrobe add

2 model calls this session, 1029 prompt + 241 output tokens
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
Vibe: High-contrast denim pairing creates an effortless streetwear aesthetic.

Outfit 2: Khaki Contrast
- NEW: Denim Jacket — Light Wash, Cropped
- w_002: Wide-leg khaki trousers
- w_003: White ribbed tank top
- w_009: Brown leather belt
Vibe: A classic light wash layer elevates minimal earth tones.

Missing: shoes
```


<details><summary>ask: <code>python app.py ask 'denim jacket under $50'</code> → exit 0, 5.7 s</summary>

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
      out: Scored this Wrangler denim jacket for $42.0 on Poshmark, and it brings such a classic, vintage streetwear vibe…

  Found:    Denim Jacket — Light Wash, Cropped — $42.0 on poshmark

  Outfit:   Outfit 1: Double Denim Streetwear
- NEW: Denim Jacket — Light Wash, Cropped
- w_001: Baggy straight-leg jeans, dark wash
- w_003: White ribbed tank top
- w_010: Black crossbody bag
Vibe: High-contrast denim pairing creates an effortless streetwear aesthetic.

Outfit 2: Khaki Contrast
- NEW: Denim Jacket — Light Wash, Cropped
- w_002: Wide-leg khaki trousers
- w_003: White ribbed tank top
- w_009: Brown leather belt
Vibe: A classic light wash layer elevates minimal earth tones.

Missing: shoes

  Fit card: Scored this Wrangler denim jacket for $42.0 on Poshmark, and it brings such a classic, vintage streetwear vibe to a double denim look with dark wash baggy straight-leg jeans, a white ribbed tank top, and a black crossbody bag. It also works effortlessly with wide-leg khaki trousers, a white ribbed tank top, and a brown leather belt for a more minimal earth tone mix. The structured shoulders make it the ultimate blank canvas.

  Note:     Your wardrobe has no shoes, so the outfit may be incomplete. Add some with: python app.py wardrobe add

2 model calls this session, 1021 prompt + 242 output tokens
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
Vibe: A relaxed, effortless everyday streetwear look combining classic denim and sporty layers.

Outfit 2: Vintage Double Denim
- NEW: Vintage Levi's 501 Jeans — Medium Wash
- w_003: White ribbed tank top
- w_006: Vintage black denim jacket
- w_009: Brown leather belt
Vibe: An easy monochrome-contrast denim outfit that leans into retro textures and timeless staples.

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
      out: Scored these Vintage Levi's 501 Jeans on Depop for $38.0, and they are already my go-to for effortless everyda…

  Found:    Vintage Levi's 501 Jeans — Medium Wash — $38.0 on depop

  Outfit:   Outfit 1: Casual Streetwear
- NEW: Vintage Levi's 501 Jeans — Medium Wash
- w_003: White ribbed tank top
- w_005: Black cropped zip hoodie
- w_010: Black crossbody bag
Vibe: A relaxed, effortless everyday streetwear look combining classic denim and sporty layers.

Outfit 2: Vintage Double Denim
- NEW: Vintage Levi's 501 Jeans — Medium Wash
- w_003: White ribbed tank top
- w_006: Vintage black denim jacket
- w_009: Brown leather belt
Vibe: An easy monochrome-contrast denim outfit that leans into retro textures and timeless staples.

Missing: shoes

  Fit card: Scored these Vintage Levi's 501 Jeans on Depop for $38.0, and they are already my go-to for effortless everyday streetwear paired with a white ribbed tank top, black cropped zip hoodie, and black crossbody bag. For a more retro vibe, I also love styling them as a double denim look with a white ribbed tank top, vintage black denim jacket, and brown leather belt.

  Note:     Your wardrobe has no shoes, so the outfit may be incomplete. Add some with: python app.py wardrobe add

2 model calls this session, 1061 prompt + 244 output tokens
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
Vibe: Effortless, everyday streetwear that plays with proportions and classic denim.

Outfit 2: Vintage Double Denim
- NEW: Vintage Levi's 501 Jeans — Medium Wash
- w_004: Oversized grey crewneck sweatshirt
- w_006: Vintage black denim jacket
- w_009: Brown leather belt
Vibe: A cozy, textured layered look with a retro edge.

Missing: shoes
```


<details><summary>ask: <code>python app.py ask 'vintage levis jeans'</code> → exit 0, 5.9 s</summary>

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
      out: Scored these Vintage Levi's 501 Jeans on Depop for $38.0! I threw them on with a white ribbed tank top, black …

  Found:    Vintage Levi's 501 Jeans — Medium Wash — $38.0 on depop

  Outfit:   Outfit 1: Casual Streetwear
- NEW: Vintage Levi's 501 Jeans — Medium Wash
- w_003: White ribbed tank top
- w_005: Black cropped zip hoodie
- w_010: Black crossbody bag
Vibe: Effortless, everyday streetwear that plays with proportions and classic denim.

Outfit 2: Vintage Double Denim
- NEW: Vintage Levi's 501 Jeans — Medium Wash
- w_004: Oversized grey crewneck sweatshirt
- w_006: Vintage black denim jacket
- w_009: Brown leather belt
Vibe: A cozy, textured layered look with a retro edge.

Missing: shoes

  Fit card: Scored these Vintage Levi's 501 Jeans on Depop for $38.0! I threw them on with a white ribbed tank top, black cropped zip hoodie, and black crossbody bag for an effortless, everyday streetwear vibe that plays with proportions. I'm also loving how they look with an oversized grey crewneck sweatshirt, vintage black denim jacket, and brown leather belt for a cozy, textured layered look with a retro edge.

  Note:     Your wardrobe has no shoes, so the outfit may be incomplete. Add some with: python app.py wardrobe add

2 model calls this session, 1057 prompt + 246 output tokens
```

</details>

### Criterion 2, run 3

**setup: demo without shoes**

- wardrobe IDs loaded:

```
["w_001", "w_002", "w_003", "w_004", "w_005", "w_006", "w_007", "w_009", "w_010"]
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

<details><summary>remove w_007: <code>python app.py wardrobe remove w_007</code> → exit 1, 0.1 s</summary>

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
Remove this item? (y/n): 
PermissionError: [WinError 5] Access is denied: 'C:\\Users\\Antoine\\PersonalProjects&Learning\\CodePath\\ai201-project2-fitfindr-starter-v2026\\utils\\..\\data\\wardrobe.json.tmp' -> 'C:\\Users\\Antoine\\PersonalProjects&Learning\\CodePath\\ai201-project2-fitfindr-starter-v2026\\utils\\..\\data\\wardrobe.json'
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
["w_001", "w_003", "w_007", "w_002", "w_009"]
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
- w_007: Chunky white sneakers
Vibe: A classic streetwear combination utilizing contrasting denim washes and comfortable staples.

Outfit 2: Casual Prep
- NEW: Denim Jacket — Light Wash, Cropped
- w_002: Wide-leg khaki trousers
- w_003: White ribbed tank top
- w_009: Brown leather belt
- w_007: Chunky white sneakers
Vibe: An easy, balanced mix of relaxed tailoring and structured vintage outerwear.
```


<details><summary>ask: <code>python app.py ask 'denim jacket under $50'</code> → exit 0, 6.9 s</summary>

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
      out: [] (empty)
      →    wardrobe covers tops, bottoms and shoes
[4] suggest_outfit
      in:  dict with keys: selected_item, wardrobe, missing_categories, feedback
      out: Outfit 1: Double Denim - NEW: Denim Jacket — Light Wash, Cropped - w_001: Baggy straight-leg jeans, dark wash …
[5] check_grounding
      in:  dict with keys: cited
      out: True
      →    every piece is in the wardrobe
[6] create_fit_card
      in:  dict with keys: outfit_suggestion, selected_item
      out: Found this Wrangler denim jacket for $42 on Poshmark. It's an easy streetwear combination paired with a white …

  Found:    Denim Jacket — Light Wash, Cropped — $42.0 on poshmark

  Outfit:   Outfit 1: Double Denim
- NEW: Denim Jacket — Light Wash, Cropped
- w_001: Baggy straight-leg jeans, dark wash
- w_003: White ribbed tank top
- w_007: Chunky white sneakers
Vibe: A classic streetwear combination utilizing contrasting denim washes and comfortable staples.

Outfit 2: Casual Prep
- NEW: Denim Jacket — Light Wash, Cropped
- w_002: Wide-leg khaki trousers
- w_003: White ribbed tank top
- w_009: Brown leather belt
- w_007: Chunky white sneakers
Vibe: An easy, balanced mix of relaxed tailoring and structured vintage outerwear.

  Fit card: Found this Wrangler denim jacket for $42 on Poshmark. It's an easy streetwear combination paired with a white ribbed tank top, baggy straight-leg jeans, and chunky white sneakers. The light blue, cropped layer also balances wide-leg khaki trousers and a brown leather belt for a casual prep vibe.

2 model calls this session, 1017 prompt + 223 output tokens
```

</details>

**trial 2**

- query: `denim jacket under $50`
- status / error: `ok / None`
- grounding check verdict (code's, not yours): `True`
- grounding retries: `0`
- IDs cited:

```
["w_001", "w_003", "w_007", "w_002", "w_009", "w_010"]
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
- w_007: Chunky white sneakers
Vibe: High-contrast textures create an effortlessly cool streetwear look.

Outfit 2: Neutral Balance
- NEW: Denim Jacket — Light Wash, Cropped
- w_002: Wide-leg khaki trousers
- w_003: White ribbed tank top
- w_009: Brown leather belt
- w_010: Black crossbody bag
Vibe: Classic earth tones ground the lightweight vintage wash for everyday wear.
```


<details><summary>ask: <code>python app.py ask 'denim jacket under $50'</code> → exit 0, 5.6 s</summary>

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
      out: [] (empty)
      →    wardrobe covers tops, bottoms and shoes
[4] suggest_outfit
      in:  dict with keys: selected_item, wardrobe, missing_categories, feedback
      out: Outfit 1: Double Denim - NEW: Denim Jacket — Light Wash, Cropped - w_001: Baggy straight-leg jeans, dark wash …
[5] check_grounding
      in:  dict with keys: cited
      out: True
      →    every piece is in the wardrobe
[6] create_fit_card
      in:  dict with keys: outfit_suggestion, selected_item
      out: Scored this vintage Wrangler cropped denim jacket for $42 on Poshmark. It has great structured shoulders and m…

  Found:    Denim Jacket — Light Wash, Cropped — $42.0 on poshmark

  Outfit:   Outfit 1: Double Denim
- NEW: Denim Jacket — Light Wash, Cropped
- w_001: Baggy straight-leg jeans, dark wash
- w_003: White ribbed tank top
- w_007: Chunky white sneakers
Vibe: High-contrast textures create an effortlessly cool streetwear look.

Outfit 2: Neutral Balance
- NEW: Denim Jacket — Light Wash, Cropped
- w_002: Wide-leg khaki trousers
- w_003: White ribbed tank top
- w_009: Brown leather belt
- w_010: Black crossbody bag
Vibe: Classic earth tones ground the lightweight vintage wash for everyday wear.

  Fit card: Scored this vintage Wrangler cropped denim jacket for $42 on Poshmark. It has great structured shoulders and makes the ultimate blank canvas. Paired it with baggy straight-leg jeans, a white ribbed tank top, and chunky white sneakers for a classic streetwear vibe.

2 model calls this session, 1014 prompt + 211 output tokens
```

</details>

**trial 3**

- query: `denim jacket under $50`
- status / error: `ok / None`
- grounding check verdict (code's, not yours): `True`
- grounding retries: `0`
- IDs cited:

```
["w_001", "w_003", "w_007", "w_002", "w_009", "w_010"]
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
- w_007: Chunky white sneakers
Vibe: A contrasting Canadian tuxedo with a fresh, streetwear-inspired color break.

Outfit 2: Khaki Contrast
- NEW: Denim Jacket — Light Wash, Cropped
- w_002: Wide-leg khaki trousers
- w_003: White ribbed tank top
- w_009: Brown leather belt
- w_010: Black crossbody bag
Vibe: An easy, balanced mix of classic structure and relaxed earth tones.
```


<details><summary>ask: <code>python app.py ask 'denim jacket under $50'</code> → exit 0, 6.3 s</summary>

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
      out: [] (empty)
      →    wardrobe covers tops, bottoms and shoes
[4] suggest_outfit
      in:  dict with keys: selected_item, wardrobe, missing_categories, feedback
      out: Outfit 1: Double Denim - NEW: Denim Jacket — Light Wash, Cropped - w_001: Baggy straight-leg jeans, dark wash …
[5] check_grounding
      in:  dict with keys: cited
      out: True
      →    every piece is in the wardrobe
[6] create_fit_card
      in:  dict with keys: outfit_suggestion, selected_item
      out: Scored this Wrangler denim jacket for $42.0 on Poshmark and I'm obsessed with the structured shoulders. I pair…

  Found:    Denim Jacket — Light Wash, Cropped — $42.0 on poshmark

  Outfit:   Outfit 1: Double Denim
- NEW: Denim Jacket — Light Wash, Cropped
- w_001: Baggy straight-leg jeans, dark wash
- w_003: White ribbed tank top
- w_007: Chunky white sneakers
Vibe: A contrasting Canadian tuxedo with a fresh, streetwear-inspired color break.

Outfit 2: Khaki Contrast
- NEW: Denim Jacket — Light Wash, Cropped
- w_002: Wide-leg khaki trousers
- w_003: White ribbed tank top
- w_009: Brown leather belt
- w_010: Black crossbody bag
Vibe: An easy, balanced mix of classic structure and relaxed earth tones.

  Fit card: Scored this Wrangler denim jacket for $42.0 on Poshmark and I'm obsessed with the structured shoulders. I paired it with baggy straight-leg jeans, a white ribbed tank top, and chunky white sneakers for a double denim streetwear vibe. Such a good vintage find!

2 model calls this session, 1019 prompt + 220 output tokens
```

</details>

**trial 4**

- query: `vintage levis jeans`
- status / error: `ok / None`
- grounding check verdict (code's, not yours): `True`
- grounding retries: `0`
- IDs cited:

```
["w_003", "w_006", "w_007", "w_004", "w_010"]
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
- w_007: Chunky white sneakers
Vibe: A classic, effortless everyday look built around timeless denim textures.

Outfit 2: Cozy Off-Duty
- NEW: Vintage Levi's 501 Jeans — Medium Wash
- w_004: Oversized grey crewneck sweatshirt
- w_007: Chunky white sneakers
- w_010: Black crossbody bag
Vibe: An easy, relaxed combination that balances oversized comfort with structured vintage jeans.
```


<details><summary>ask: <code>python app.py ask 'vintage levis jeans'</code> → exit 0, 6.4 s</summary>

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
      out: [] (empty)
      →    wardrobe covers tops, bottoms and shoes
[4] suggest_outfit
      in:  dict with keys: selected_item, wardrobe, missing_categories, feedback
      out: Outfit 1: Casual Streetwear - NEW: Vintage Levi's 501 Jeans — Medium Wash - w_003: White ribbed tank top - w_0…
[5] check_grounding
      in:  dict with keys: cited
      out: True
      →    every piece is in the wardrobe
[6] create_fit_card
      in:  dict with keys: outfit_suggestion, selected_item
      out: Scored these vintage Levi's 501 jeans for $38 on depop, and I’m obsessed with the light fading at the knees. T…

  Found:    Vintage Levi's 501 Jeans — Medium Wash — $38.0 on depop

  Outfit:   Outfit 1: Casual Streetwear
- NEW: Vintage Levi's 501 Jeans — Medium Wash
- w_003: White ribbed tank top
- w_006: Vintage black denim jacket
- w_007: Chunky white sneakers
Vibe: A classic, effortless everyday look built around timeless denim textures.

Outfit 2: Cozy Off-Duty
- NEW: Vintage Levi's 501 Jeans — Medium Wash
- w_004: Oversized grey crewneck sweatshirt
- w_007: Chunky white sneakers
- w_010: Black crossbody bag
Vibe: An easy, relaxed combination that balances oversized comfort with structured vintage jeans.

  Fit card: Scored these vintage Levi's 501 jeans for $38 on depop, and I’m obsessed with the light fading at the knees. They look so good thrown on with a white ribbed tank top, vintage black denim jacket, and chunky white sneakers for an effortless streetwear vibe. Later I'll probably swap the jacket for an oversized grey crewneck sweatshirt and add a black crossbody bag when I want that cozy off-duty look.

2 model calls this session, 1049 prompt + 247 output tokens
```

</details>

**trial 5**

- query: `vintage levis jeans`
- status / error: `ok / None`
- grounding check verdict (code's, not yours): `True`
- grounding retries: `0`
- IDs cited:

```
["w_003", "w_005", "w_007", "w_004", "w_006"]
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
- w_007: Chunky white sneakers
Vibe: This laid-back ensemble highlights classic denim with comfortable, sporty basics.

Outfit 2: Double Denim
- NEW: Vintage Levi's 501 Jeans — Medium Wash
- w_004: Oversized grey crewneck sweatshirt
- w_006: Vintage black denim jacket
- w_007: Chunky white sneakers
Vibe: A textured monochrome layering approach that keeps the vintage aesthetic front and center.
```


<details><summary>ask: <code>python app.py ask 'vintage levis jeans'</code> → exit 0, 5.8 s</summary>

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
      out: [] (empty)
      →    wardrobe covers tops, bottoms and shoes
[4] suggest_outfit
      in:  dict with keys: selected_item, wardrobe, missing_categories, feedback
      out: Outfit 1: Casual Streetwear - NEW: Vintage Levi's 501 Jeans — Medium Wash - w_003: White ribbed tank top - w_0…
[5] check_grounding
      in:  dict with keys: cited
      out: True
      →    every piece is in the wardrobe
[6] create_fit_card
      in:  dict with keys: outfit_suggestion, selected_item
      out: Scored these amazing vintage Levi's 501 jeans on Depop for $38, and they have the best light fading at the kne…

  Found:    Vintage Levi's 501 Jeans — Medium Wash — $38.0 on depop

  Outfit:   Outfit 1: Casual Streetwear
- NEW: Vintage Levi's 501 Jeans — Medium Wash
- w_003: White ribbed tank top
- w_005: Black cropped zip hoodie
- w_007: Chunky white sneakers
Vibe: This laid-back ensemble highlights classic denim with comfortable, sporty basics.

Outfit 2: Double Denim
- NEW: Vintage Levi's 501 Jeans — Medium Wash
- w_004: Oversized grey crewneck sweatshirt
- w_006: Vintage black denim jacket
- w_007: Chunky white sneakers
Vibe: A textured monochrome layering approach that keeps the vintage aesthetic front and center.

  Fit card: Scored these amazing vintage Levi's 501 jeans on Depop for $38, and they have the best light fading at the knees. I paired them with a white ribbed tank top, black cropped zip hoodie, and chunky white sneakers for a laid-back streetwear look.

2 model calls this session, 1050 prompt + 215 output tokens
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

</details>

**trial 2**

- empty-wardrobe note shown: `True`
- `w_` IDs in the output: `False`
- fit card produced: `True`
- traceback: `False`
- exit code: `0`

<details><summary>ask: <code>python app.py ask 'denim jacket under $50' --empty-wardrobe</code> → exit 0, 4.8 s</summary>

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
      out: Outfit 1: Layer it over a black ribbed turtleneck bodysuit, paired with olive green wide-leg trousers and chun…
[4] check_grounding
      in:  dict with keys: cited
      →    empty wardrobe: general advice isn't meant to be grounded
[5] create_fit_card
      in:  dict with keys: outfit_suggestion, selected_item
      out: Scored this Wrangler denim jacket for $42 on Poshmark and I am so obsessed with the structured shoulders and l…

  Found:    Denim Jacket — Light Wash, Cropped — $42.0 on poshmark

  Outfit:   Outfit 1: Layer it over a black ribbed turtleneck bodysuit, paired with olive green wide-leg trousers and chunky black loafers. 
Vibe: 90s model-off-duty meets retro prep. 

Outfit 2: Throw it on over a black cotton baby tee, a slip skirt in leopard print or satin black, and beat-up white canvas sneakers. 
Vibe: Effortless, grungy street style.

  Fit card: Scored this Wrangler denim jacket for $42 on Poshmark and I am so obsessed with the structured shoulders and light wash. It looks incredible thrown over a black ribbed turtleneck bodysuit and olive green wide-leg trousers with chunky black loafers for that ultimate 90s model-off-duty vibe. It’s also giving effortless, grungy street style when I wear it with a black cotton baby tee, a slip skirt, and beat-up white canvas sneakers.

  Note:     Your wardrobe is empty, so these are general styling ideas. Add your clothes with: python app.py wardrobe add

2 model calls this session, 529 prompt + 185 output tokens
```

</details>

**trial 3**

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
      out: Look 1: Throw it over a black ribbed midi dress with chunky black boots and a canvas tote.   Vibe: Edgy meets …
[4] check_grounding
      in:  dict with keys: cited
      →    empty wardrobe: general advice isn't meant to be grounded
[5] create_fit_card
      in:  dict with keys: outfit_suggestion, selected_item
      out: Snagged this Wrangler denim jacket on Poshmark for $42, and it's the ultimate blank canvas for 90s streetwear.…

  Found:    Denim Jacket — Light Wash, Cropped — $42.0 on poshmark

  Outfit:   Look 1: Throw it over a black ribbed midi dress with chunky black boots and a canvas tote. 

Vibe: Edgy meets effortless. The cropped cut balances the longer hemline of the dress.

Look 2: Pair it with wide-leg beige cargo trousers, a tight white baby tee, and retro sneakers. 

Vibe: 90s streetwear. Double denim is cool, but mixing textures keeps the look grounded and easy to wear daily.

  Fit card: Snagged this Wrangler denim jacket on Poshmark for $42, and it's the ultimate blank canvas for 90s streetwear. I'm obsessed with throwing it over a black ribbed midi dress with chunky black boots and a canvas tote for an edgy yet effortless vibe. It also looks so good paired with wide-leg beige cargo trousers, a tight white baby tee, and retro sneakers.

  Note:     Your wardrobe is empty, so these are general styling ideas. Add your clothes with: python app.py wardrobe add

2 model calls this session, 536 prompt + 180 output tokens
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
      out: Look 1: Throw it over a black ribbed midi dress with chunky black boots and a canvas tote.  Vibe: Edgy meets e…
[4] check_grounding
      in:  dict with keys: cited
      →    empty wardrobe: general advice isn't meant to be grounded
[5] create_fit_card
      in:  dict with keys: outfit_suggestion, selected_item
      out: Scored this Wrangler denim jacket for $42 on Poshmark and I’m obsessed. It's the ultimate blank canvas with gr…

  Found:    Denim Jacket — Light Wash, Cropped — $42.0 on poshmark

  Outfit:   Look 1: Throw it over a black ribbed midi dress with chunky black boots and a canvas tote. 
Vibe: Edgy meets effortless. The cropped cut balances the longer hemline of the dress for an easy weekend look.

Look 2: Pair it with wide-leg beige trousers, a fitted white baby tee, and retro sneakers. 
Vibe: Casual streetwear. The light wash denim and neutral pants create a clean, balanced palette that feels pulled-together without trying too hard.

  Fit card: Scored this Wrangler denim jacket for $42 on Poshmark and I’m obsessed. It's the ultimate blank canvas with great structured shoulders, so I threw it over a black ribbed midi dress with chunky black boots for an edgy, effortless weekend vibe. Later, I’ll pair it with wide-leg beige trousers, a fitted white baby tee, and retro sneakers for some casual streetwear energy.

  Note:     Your wardrobe is empty, so these are general styling ideas. Add your clothes with: python app.py wardrobe add

2 model calls this session, 542 prompt + 186 output tokens
```

</details>

**trial 5**

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
      out: Outfit 1: Layer it over a black ribbed turtleneck bodysuit with high-waisted wide-leg trousers and retro white…
[4] check_grounding
      in:  dict with keys: cited
      →    empty wardrobe: general advice isn't meant to be grounded
[5] create_fit_card
      in:  dict with keys: outfit_suggestion, selected_item
      out: Scored this light wash Wrangler denim jacket on Poshmark for $42 and I'm obsessed with the structured shoulder…

  Found:    Denim Jacket — Light Wash, Cropped — $42.0 on poshmark

  Outfit:   Outfit 1: Layer it over a black ribbed turtleneck bodysuit with high-waisted wide-leg trousers and retro white sneakers. Add a small black shoulder bag. 
Vibe: Effortless 90s model-off-duty.

Outfit 2: Throw it on over a floral midi slip dress in a dark or muted print, paired with chunky black combat boots and layered silver necklaces. 
Vibe: Edgy vintage romantic.

  Fit card: Scored this light wash Wrangler denim jacket on Poshmark for $42 and I'm obsessed with the structured shoulders. It gives such effortless 90s model-off-duty energy when I layer it over a black ribbed turtleneck bodysuit, high-waisted wide-leg trousers, retro white sneakers, and a small black shoulder bag. I'm also loving it for an edgy vintage romantic vibe thrown over a floral midi slip dress, chunky black combat boots, and layered silver necklaces.

  Note:     Your wardrobe is empty, so these are general styling ideas. Add your clothes with: python app.py wardrobe add

2 model calls this session, 531 prompt + 193 output tokens
```

</details>

### Criterion 3, run 2

**trial 1**

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
      out: Outfit 1: Layer it over a black ribbed turtleneck bodysuit with high-waisted wide-leg black trousers and chunk…
[4] check_grounding
      in:  dict with keys: cited
      →    empty wardrobe: general advice isn't meant to be grounded
[5] create_fit_card
      in:  dict with keys: outfit_suggestion, selected_item
      out: Scored this Wrangler denim jacket for $42.0 on Poshmark, and it’s giving such a cool 90s edge. For an edgy, po…

  Found:    Denim Jacket — Light Wash, Cropped — $42.0 on poshmark

  Outfit:   Outfit 1: Layer it over a black ribbed turtleneck bodysuit with high-waisted wide-leg black trousers and chunky black loafers. Add a silver chain necklace. 
Vibe: Edgy, polished casual with a retro 90s edge.

Outfit 2: Throw it on over an oversized white cotton poplin button-down worn loose as a mini dress, paired with knee-high leather boots and a simple canvas tote bag. 
Vibe: Effortless, downtown-cool streetwear.

  Fit card: Scored this Wrangler denim jacket for $42.0 on Poshmark, and it’s giving such a cool 90s edge. For an edgy, polished casual look, I layered it over a bodysuit, trousers, and loafers with a silver chain necklace. It also works as effortless streetwear thrown over a button-down with boots and a tote bag.

  Note:     Your wardrobe is empty, so these are general styling ideas. Add your clothes with: python app.py wardrobe add

2 model calls this session, 543 prompt + 179 output tokens
```

</details>

**trial 2**

- empty-wardrobe note shown: `True`
- `w_` IDs in the output: `False`
- fit card produced: `True`
- traceback: `False`
- exit code: `0`

<details><summary>ask: <code>python app.py ask 'denim jacket under $50' --empty-wardrobe</code> → exit 0, 4.8 s</summary>

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
      out: **Look 1: Off-Duty Model** Layer the jacket over a fitted black ribbed tank and high-waisted wide-leg black tr…
[4] check_grounding
      in:  dict with keys: cited
      →    empty wardrobe: general advice isn't meant to be grounded
[5] create_fit_card
      in:  dict with keys: outfit_suggestion, selected_item
      out: Scored this Wrangler denim jacket for $42.0 on poshmark and it’s the ultimate blank canvas. I love pairing the…

  Found:    Denim Jacket — Light Wash, Cropped — $42.0 on poshmark

  Outfit:   **Look 1: Off-Duty Model**
Layer the jacket over a fitted black ribbed tank and high-waisted wide-leg black trousers. Finish with chunky black loafers and a canvas tote. 
*Vibe:* Effortless, structured streetwear. 

**Look 2: Weekend Brunch**
Throw it on over an olive green slip dress in satin or cotton. Add retro white sneakers and a simple canvas shoulder bag. 
*Vibe:* Sweet yet casual high-low contrast.

  Fit card: Scored this Wrangler denim jacket for $42.0 on poshmark and it’s the ultimate blank canvas. I love pairing the structured streetwear vibe with a fitted black ribbed tank, high-waisted wide-leg black trousers, chunky black loafers, and a canvas tote for an effortless look. It's also so cute thrown over an olive green slip dress with retro white sneakers and a simple canvas shoulder bag for weekend brunch!

  Note:     Your wardrobe is empty, so these are general styling ideas. Add your clothes with: python app.py wardrobe add

2 model calls this session, 542 prompt + 191 output tokens
```

</details>

**trial 3**

- empty-wardrobe note shown: `True`
- `w_` IDs in the output: `False`
- fit card produced: `True`
- traceback: `False`
- exit code: `0`

<details><summary>ask: <code>python app.py ask 'denim jacket under $50' --empty-wardrobe</code> → exit 0, 5.4 s</summary>

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
      out: Grab it—that structured shoulder is everything.   **Outfit 1: Off-Duty Streetwear** Layer the jacket over a ba…
[4] check_grounding
      in:  dict with keys: cited
      →    empty wardrobe: general advice isn't meant to be grounded
[5] create_fit_card
      in:  dict with keys: outfit_suggestion, selected_item
      out: Scored this Wrangler denim jacket for $42.0 on Poshmark, and that structured shoulder is everything. For an ef…

  Found:    Denim Jacket — Light Wash, Cropped — $42.0 on poshmark

  Outfit:   Grab it—that structured shoulder is everything. 

**Outfit 1: Off-Duty Streetwear**
Layer the jacket over a basic black baby tee, high-waisted wide-leg black trousers, and retro white sneakers. Add a canvas tote and silver hoop earrings. 
*Vibe:* Effortless, cool-girl off-duty.

**Outfit 2: Retro Casual**
Throw it over a ribbed olive green tank top tucked into a black midi slip skirt. Finish with chunky black platform loafers and a shoulder bag. 
*Vibe:* 90s indie-sleaze meets everyday chic. 

Both looks let the vintage Wrangler cut stand out without trying too hard.

  Fit card: Scored this Wrangler denim jacket for $42.0 on Poshmark, and that structured shoulder is everything. For an effortless, cool-girl off-duty look, I layered it over a basic black baby tee, high-waisted wide-leg black trousers, and retro white sneakers. It's giving 90s indie-sleaze meets everyday chic when I throw it over a ribbed olive green tank top tucked into a black midi slip skirt with chunky black platform loafers.

  Note:     Your wardrobe is empty, so these are general styling ideas. Add your clothes with: python app.py wardrobe add

2 model calls this session, 584 prompt + 245 output tokens
```

</details>

**trial 4**

- empty-wardrobe note shown: `True`
- `w_` IDs in the output: `False`
- fit card produced: `True`
- traceback: `False`
- exit code: `0`

<details><summary>ask: <code>python app.py ask 'denim jacket under $50' --empty-wardrobe</code> → exit 0, 4.8 s</summary>

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
      out: **Outfit 1: Effortless Off-Duty** Layer the jacket over a basic black baby tee and olive green cargo pants. Fi…
[4] check_grounding
      in:  dict with keys: cited
      →    empty wardrobe: general advice isn't meant to be grounded
[5] create_fit_card
      in:  dict with keys: outfit_suggestion, selected_item
      out: Scored this Wrangler denim jacket for $42.0 on Poshmark and I'm obsessed with the structured shoulders. It loo…

  Found:    Denim Jacket — Light Wash, Cropped — $42.0 on poshmark

  Outfit:   **Outfit 1: Effortless Off-Duty**
Layer the jacket over a basic black baby tee and olive green cargo pants. Finish with chunky white sneakers and a canvas tote. 
*Vibe:* 90s streetwear. Cool, casual, and easy to throw together for running errands.

**Outfit 2: High-Low Contrast**
Wear the cropped denim over a black ribbed slip dress that hits at the midi length. Add beat-up canvas low-top sneakers and a simple leather shoulder bag. 
*Vibe:* Downtown indie-sleaze. It balances the rugged, structured shoulders of the jacket with a sleek, feminine silhouette.

  Fit card: Scored this Wrangler denim jacket for $42.0 on Poshmark and I'm obsessed with the structured shoulders. It looks so good layered over a basic black baby tee and olive green cargo pants for that 90s streetwear vibe while running errands.

  Note:     Your wardrobe is empty, so these are general styling ideas. Add your clothes with: python app.py wardrobe add

2 model calls this session, 575 prompt + 190 output tokens
```

</details>

**trial 5**

- empty-wardrobe note shown: `True`
- `w_` IDs in the output: `False`
- fit card produced: `True`
- traceback: `False`
- exit code: `0`

<details><summary>ask: <code>python app.py ask 'denim jacket under $50' --empty-wardrobe</code> → exit 0, 4.8 s</summary>

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
      out: Look 1: Throw it over a black slip dress with chunky black boots. Add a silver chain necklace.  Vibe: 90s indi…
[4] check_grounding
      in:  dict with keys: cited
      →    empty wardrobe: general advice isn't meant to be grounded
[5] create_fit_card
      in:  dict with keys: outfit_suggestion, selected_item
      out: Scored this Wrangler denim jacket for $42.0 on poshmark, and it’s the ultimate blank canvas for custom patches…

  Found:    Denim Jacket — Light Wash, Cropped — $42.0 on poshmark

  Outfit:   Look 1: Throw it over a black slip dress with chunky black boots. Add a silver chain necklace. 
Vibe: 90s indie-sleaze meets romantic. Effortless, edgy date-night energy.

Look 2: Pair it with wide-leg beige trousers, a fitted white baby tee, and retro canvas sneakers. 
Vibe: Casual streetwear. Clean, sporty, and perfect for weekend errands or coffee runs.

  Fit card: Scored this Wrangler denim jacket for $42.0 on poshmark, and it’s the ultimate blank canvas for custom patches or pins. I love styling the light blue outerwear over a black slip dress with chunky black boots and a silver chain necklace for that 90s indie-sleaze meets romantic date-night vibe. It’s also just as good thrown over wide-leg beige trousers, a fitted white baby tee, and retro canvas sneakers for easy weekend streetwear errands.

  Note:     Your wardrobe is empty, so these are general styling ideas. Add your clothes with: python app.py wardrobe add

2 model calls this session, 532 prompt + 192 output tokens
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
      out: Outfit 1: Layer it over a black ribbed turtleneck bodysuit with high-waisted wide-leg black trousers and chunk…
[4] check_grounding
      in:  dict with keys: cited
      →    empty wardrobe: general advice isn't meant to be grounded
[5] create_fit_card
      in:  dict with keys: outfit_suggestion, selected_item
      out: Scored this Wrangler denim jacket for $42 on Poshmark, and it’s giving major edgy, polished downtown chic when…

  Found:    Denim Jacket — Light Wash, Cropped — $42.0 on poshmark

  Outfit:   Outfit 1: Layer it over a black ribbed turtleneck bodysuit with high-waisted wide-leg black trousers and chunky black loafers. Add silver hoop earrings. 
Vibe: Edgy, polished downtown chic.

Outfit 2: Throw it on over a vintage floral midi dress paired with beat-up canvas high-top sneakers and a canvas tote bag. 
Vibe: Effortless 90s indie-sleaze.

  Fit card: Scored this Wrangler denim jacket for $42 on Poshmark, and it’s giving major edgy, polished downtown chic when layered over a black ribbed turtleneck bodysuit, high-waisted wide-leg black trousers, chunky black loafers, and silver hoop earrings. For an effortless 90s indie-sleaze vibe, I also love throwing it on over a vintage floral midi dress paired with beat-up canvas high-top sneakers and a canvas tote bag. This light wash, cropped beauty with great structured shoulders is the ultimate blank canvas!

  Note:     Your wardrobe is empty, so these are general styling ideas. Add your clothes with: python app.py wardrobe add

2 model calls this session, 529 prompt + 201 output tokens
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
      out: Here are two easy, wearable ways to style your cropped Wrangler jacket:  1. **The Model-Off-Duty Look**: Layer…
[4] check_grounding
      in:  dict with keys: cited
      →    empty wardrobe: general advice isn't meant to be grounded
[5] create_fit_card
      in:  dict with keys: outfit_suggestion, selected_item
      out: Scored this Wrangler cropped denim jacket for $42.0 on Poshmark and it is such a classic streetwear find. I'm …

  Found:    Denim Jacket — Light Wash, Cropped — $42.0 on poshmark

  Outfit:   Here are two easy, wearable ways to style your cropped Wrangler jacket:

1. **The Model-Off-Duty Look**: Layer the jacket over a black fitted ribbed tank, paired with high-waisted wide-leg black trousers and chunky white sneakers. Finish with silver hoop earrings. 
*Vibe:* Effortless, cool, and downtown-chic. 

2. **The Sweet-and-Tough Contrast**: Throw the jacket over a black floral midi slip dress, and add beat-up canvas low-top sneakers or lug-sole ankle boots. 
*Vibe:* Edgy romantic, perfect for weekend brunching or casual dates. 

Both are simple to throw together with basics you likely already own!

  Fit card: Scored this Wrangler cropped denim jacket for $42.0 on Poshmark and it is such a classic streetwear find. I'm obsessed with throwing it over a black floral midi slip dress with beat-up canvas low-top sneakers for that edgy romantic vibe. It’s a total blank canvas with great structured shoulders, so I can't wait to keep styling it.

  Note:     Your wardrobe is empty, so these are general styling ideas. Add your clothes with: python app.py wardrobe add

2 model calls this session, 589 prompt + 228 output tokens
```

</details>

**trial 3**

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
      out: **Outfit 1: Casual Streetwear** Layer the cropped jacket over a black fitted baby tee and high-waisted olive g…
[4] check_grounding
      in:  dict with keys: cited
      →    empty wardrobe: general advice isn't meant to be grounded
[5] create_fit_card
      in:  dict with keys: outfit_suggestion, selected_item
      out: Scored this Wrangler cropped denim jacket on Poshmark for $42, and it's the ultimate blank canvas with great s…

  Found:    Denim Jacket — Light Wash, Cropped — $42.0 on poshmark

  Outfit:   **Outfit 1: Casual Streetwear**
Layer the cropped jacket over a black fitted baby tee and high-waisted olive green cargo pants. Finish with chunky white sneakers and a canvas tote. 
*Vibe:* Easy, everyday cool with a slight 90s edge.

**Outfit 2: High-Low Contrast**
Throw the denim jacket over a slip dress in black or a muted floral print. Pair with black ankle boots and a minimalist leather shoulder bag. 
*Vibe:* Effortless juxtaposition of rugged denim and feminine romance.

  Fit card: Scored this Wrangler cropped denim jacket on Poshmark for $42, and it's the ultimate blank canvas with great structured shoulders. I layered it over a baby tee and cargo pants with chunky sneakers and a tote for an easy, everyday cool streetwear vibe with a slight 90s edge. It also looks so good thrown over a slip dress and ankle boots for an effortless juxtaposition of rugged denim and feminine romance.

  Note:     Your wardrobe is empty, so these are general styling ideas. Add your clothes with: python app.py wardrobe add

2 model calls this session, 554 prompt + 201 output tokens
```

</details>

**trial 4**

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
      out: Outfit 1: Layer the cropped jacket over a black ribbed tank top with high-waisted olive green cargo pants and …
[4] check_grounding
      in:  dict with keys: cited
      →    empty wardrobe: general advice isn't meant to be grounded
[5] create_fit_card
      in:  dict with keys: outfit_suggestion, selected_item
      out: Scored this Wrangler denim jacket with structured shoulders for $42 on Poshmark. It's a blank canvas with no p…

  Found:    Denim Jacket — Light Wash, Cropped — $42.0 on poshmark

  Outfit:   Outfit 1: Layer the cropped jacket over a black ribbed tank top with high-waisted olive green cargo pants and chunky black loafers. 
Vibe: 90s streetwear.

Outfit 2: Throw it on over a black midi slip dress paired with classic white canvas sneakers and a canvas tote bag. 
Vibe: Effortless casual-chic.

  Fit card: Scored this Wrangler denim jacket with structured shoulders for $42 on Poshmark. It's a blank canvas with no patches or pins, so I've been styling the cropped light wash piece two ways for 90s streetwear and effortless casual-chic vibes. First I layered it over a black ribbed tank top with high-waisted olive green cargo pants and chunky black loafers, and next I threw it on over a black midi slip dress paired with classic white canvas sneakers and a canvas tote bag.

  Note:     Your wardrobe is empty, so these are general styling ideas. Add your clothes with: python app.py wardrobe add

2 model calls this session, 515 prompt + 180 output tokens
```

</details>

**trial 5**

- empty-wardrobe note shown: `True`
- `w_` IDs in the output: `False`
- fit card produced: `True`
- traceback: `False`
- exit code: `0`

<details><summary>ask: <code>python app.py ask 'denim jacket under $50' --empty-wardrobe</code> → exit 0, 5.4 s</summary>

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
      out: **Outfit 1: Off-Duty Cool** Layer the cropped jacket over a plain white crewneck tee and black high-waisted wi…
[4] check_grounding
      in:  dict with keys: cited
      →    empty wardrobe: general advice isn't meant to be grounded
[5] create_fit_card
      in:  dict with keys: outfit_suggestion, selected_item
      out: Scored this vintage Wrangler denim jacket on Poshmark for $42, and it’s the ultimate blank canvas with great s…

  Found:    Denim Jacket — Light Wash, Cropped — $42.0 on poshmark

  Outfit:   **Outfit 1: Off-Duty Cool**
Layer the cropped jacket over a plain white crewneck tee and black high-waisted wide-leg trousers. Finish with canvas low-top sneakers and a canvas tote bag. 
*Vibe:* Effortless streetwear. The structured shoulders and light wash pop against the dark trousers for an easy, balanced daily look.

**Outfit 2: Retro Casual**
Pair it with a ribbed olive green tank top, a black pleated tennis skirt, and chunky retro running sneakers with white crew socks. 
*Vibe:* Sporty vintage. The boxy Wrangler fit balances the feminine skirt while leaning into nostalgic '90s campus style.

  Fit card: Scored this vintage Wrangler denim jacket on Poshmark for $42, and it’s the ultimate blank canvas with great structured shoulders. I layered the light wash cropped outerwear over a plain white crewneck tee and black high-waisted wide-leg trousers, finishing with canvas low-top sneakers and a canvas tote bag for effortless streetwear.

  Note:     Your wardrobe is empty, so these are general styling ideas. Add your clothes with: python app.py wardrobe add

2 model calls this session, 580 prompt + 211 output tokens
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

**trial 3**

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

### Criterion 4, run 2

**trial 1**

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

**trial 2**

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

**trial 3**

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

### Criterion 4, run 3

**trial 1**

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

**trial 4**

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

**trial 5**

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

## Capstone criterion 5: Validation and normalization when adding items

**Target:** 18/18 cases

| Trial | Run 1 | Run 2 | Run 3 |
|---|---|---|---|
| case A | PASS | PASS | FAIL |
| case B | PASS | PASS | PASS |
| case C | PASS | PASS | PASS |
| case D | PASS | PASS | PASS |
| case E | PASS | PASS | PASS |
| case F | PASS | PASS | PASS |

**Verdict:** 17 / 18

**Run 3, case A failed.** A valid item should have been saved, but `wardrobe add` exited 1 with `PermissionError: [WinError 5] Access is denied` while renaming `wardrobe.json.tmp` over `wardrobe.json`. Nothing was saved, and neither `Added:` nor `Not saved:` was shown. It is the same crash that voided criterion 2's run 3: the atomic save in `utils/wardrobe_store.py` (`os.replace`) fails when another process has `wardrobe.json` open at that moment (on Windows, usually antivirus or the search indexer scanning the file just written). Run 3's case F got `w_011` instead of `w_012` as a result.

### Criterion 5, run 1

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

<details><summary>add: <code>python app.py wardrobe add</code> → exit 0, 0.2 s</summary>

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
- `Added:` shown: `False`
- wardrobe.json unchanged: `True`
- stored item: `None`

<details><summary>add: <code>python app.py wardrobe add</code> → exit 1, 0.2 s</summary>

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
Name: Category (tops, bottoms, outerwear, shoes, accessories): Colors (comma-separated): Style tags (comma-separated, optional): Notes (optional): 
PermissionError: [WinError 5] Access is denied: 'C:\\Users\\Antoine\\PersonalProjects&Learning\\CodePath\\ai201-project2-fitfindr-starter-v2026\\utils\\..\\data\\wardrobe.json.tmp' -> 'C:\\Users\\Antoine\\PersonalProjects&Learning\\CodePath\\ai201-project2-fitfindr-starter-v2026\\utils\\..\\data\\wardrobe.json'
```

</details>

**case B**

- input: `whitespace-only name`
- `Not saved:` shown: `True`
- `Added:` shown: `False`
- wardrobe.json unchanged: `True`
- stored item: `None`

<details><summary>add: <code>python app.py wardrobe add</code> → exit 0, 0.2 s</summary>

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
{"name": "Plain Hat", "category": "accessories", "colors": ["black"], "style_tags": [], "notes": null, "id": "w_011"}
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
  w_011  Plain Hat
        category:   accessories
        colors:     black
        style tags: -
        notes:      -
```

</details>

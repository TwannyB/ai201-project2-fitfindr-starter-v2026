import os
import json
import re
import time
from utils.data_loader import get_example_wardrobe, load_wardrobe_schema
from typing import Optional

CATEGORIES = ("tops", "bottoms", "outerwear", "shoes", "accessories")

WARDROBE_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "wardrobe.json")

def load_wardrobe() -> dict:
    """
    Load the current wardrobe from the wardrobe.json file.

    If the file is missing, we want it to be created from the example wardrobe, saved, and returned
    
    If the file is present, we want to load it and return it
    
    If the file is present but invalid, we want to raise an error

    Returns:
        A dictionary representing the current wardrobe, including a list of items and the next available ID.
    """
    path = WARDROBE_PATH
    if not os.path.exists(path):
        # If the file doesn't exist, create it from the example wardrobe and save it
        example_wardrobe = get_example_wardrobe()
        example_wardrobe["next_id"] = len(example_wardrobe["items"]) + 1  # Set next_id based on the number of items
        example_wardrobe["user_id"] = "demo_user"  # Add a user_id field to the example wardrobe
        save_wardrobe(example_wardrobe, path)
        return example_wardrobe
        
    with open(path, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError as e:
            raise ValueError(
                f"Error loading wardrobe from {os.path.normpath(path)}: {e}. "
                "Fix it, or delete it to reset to the example wardrobe."
            ) from e
        

def validate_item(item: dict) -> list[str]:
    """
    Validates a wardrobe item against the schema when adding items to a wardrobe.
    
    Args:
        item: A dictionary representing a wardrobe item.
    
    Returns:
        A list of error messages. If the list is empty, the item is valid.
    """
    schema = load_wardrobe_schema()["schema"]["items"][0]
    errors = []

    
    for schema_field, rules in schema.items():
        if schema_field == "notes":
            continue # Notes are optional
        if schema_field not in item:
            errors.append(f'Item is missing required field: {schema_field}')

    for field in item:
        if field not in schema:
            errors.append(f'Item has unknown field "{field}". Allowed fields: {", ".join(schema)}.')

    for field, value in item.items():
        if field == "id":
            if not isinstance(value, str):
                errors.append('Item field "id" must be a string.')
            elif not re.fullmatch(r"w_\d{3}", value):
                # Outfits cite pieces by this ID and the grounding check only
                # recognises w_NNN, so any other shape could never be grounded.
                errors.append(f'Item field "id" must look like w_001 (got {value!r}).')
        if field == "name":
            if not isinstance(value, str):
                errors.append('Item field "name" must be a string.')
            elif not value.strip():
                errors.append('Item field "name" cannot be empty.')
            elif len(value) > 100:
                errors.append('Item field "name" cannot exceed 100 characters.')
        if field == "category" and value not in CATEGORIES:
            errors.append(f'Item field "category" must be one of: {", ".join(CATEGORIES)}.')
        if field == "colors":
            if not isinstance(value, list) or not all(isinstance(color, str) for color in value):
                errors.append('Item field "colors" must be a list of strings.')
            elif len(value) == 0:
                errors.append('Item field "colors" must contain at least one color.')
        if field == "style_tags":
            if not isinstance(value, list) or not all(isinstance(tag, str) for tag in value):
                errors.append('Item field "style_tags" must be a list of strings.')
        if field == "notes" and not isinstance(value, str) and not isinstance(value, type(None)):
            errors.append('Item field "notes" must be a string or null.')
    
    return errors

# A wardrobe sent with a request goes straight into the model's prompt, so cap
# its size: it bounds prompt length (and cost) for a public endpoint. Real
# wardrobes in this project are around ten items.
MAX_REQUEST_ITEMS = 50


def validate_wardrobe(wardrobe) -> tuple[dict | None, list[str]]:
    """
    Check a whole wardrobe that didn't come from the store, e.g. one sent to
    serve.py's /ask. Each item gets the same checks as add_item, plus checks
    only a whole wardrobe can fail: its shape, its size, and duplicate IDs.

    Returns:
        (normalized wardrobe {"items": [...]}, []) when valid, or
        (None, errors) with every problem found, each naming the item.
    """
    if not isinstance(wardrobe, dict):
        return None, ['"wardrobe" must be an object like {"items": [...]}.']
    items = wardrobe.get("items")
    if not isinstance(items, list):
        return None, ['"wardrobe" must have an "items" list.']
    if len(items) > MAX_REQUEST_ITEMS:
        return None, [f'"wardrobe" can have at most {MAX_REQUEST_ITEMS} items (got {len(items)}).']

    errors, normalized, seen = [], [], set()
    for index, item in enumerate(items, 1):
        if not isinstance(item, dict):
            errors.append(f"Item {index}: must be an object.")
            continue
        clean = normalize_item(item)
        errors += [f"Item {index}: {e}" for e in validate_item(clean)]
        item_id = clean.get("id")
        if isinstance(item_id, str):
            if item_id in seen:
                errors.append(f"Item {index}: duplicate id {item_id}.")
            seen.add(item_id)
        normalized.append(clean)

    if errors:
        return None, errors
    return {"items": normalized}, []


def normalize_item(item: dict) -> dict:
    """
    Normalizes a wardrobe item to ensure consistent formatting.

    Args:
        item: A dictionary representing a wardrobe item.

    Returns:
        A normalized wardrobe item dictionary. (Colors and style_tags deduped and lowercased, strings stripped of whitespace.)
    """
    normalized_item = item.copy()

    # Normalize string fields
    for field in ["name", "category", "notes"]:
        if field in normalized_item and isinstance(normalized_item[field], str):
            normalized_item[field] = normalized_item[field].strip()
            if field == "category":
                normalized_item[field] = normalized_item[field].lower()

    # Normalize list fields
    for field in ["colors", "style_tags"]:
        if field in normalized_item and isinstance(normalized_item[field], list):
            # Only clean up strings; leave anything else as-is so validate_item can reject it
            normalized_item[field] = [tag.strip().lower() if isinstance(tag, str) else tag for tag in normalized_item[field]]
            # Drop blank entries, e.g. from "red, ,blue" or an empty answer
            normalized_item[field] = [tag for tag in normalized_item[field] if tag != ""]
            # Remove duplicates while preserving order
            normalized_item[field] = list(dict.fromkeys(normalized_item[field]))

    return normalized_item

def save_wardrobe(wardrobe: dict, path: Optional[str] = None) -> None:
    """
    Saves a wardrobe dictionary to a JSON file.

    Args:
        wardrobe: A dictionary representing the wardrobe to save.
        path: The file path where the wardrobe should be saved.
    """
    # If no path is provided, use the default WARDROBE_PATH
    if path is None:
        path = WARDROBE_PATH
    # Use a temporary file to ensure atomic writes; we use a .tmp extension to indicate it's temporary
    tmp = path + ".tmp"

    # Write the wardrobe to a temporary file
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(wardrobe, f, indent=2)
    # Rename the temporary file to the target path, replacing the old file.
    # Atomic, so a crash never leaves a half-written wardrobe. On Windows the
    # rename fails with PermissionError while another process (antivirus, the
    # search indexer) briefly has wardrobe.json open; the capstone "before"
    # run hit this 2 times in 51 saves. The lock clears within
    # milliseconds, so retry a few times before giving up.
    for attempt in range(_REPLACE_ATTEMPTS):
        try:
            os.replace(tmp, path)
            return
        except PermissionError:
            if attempt == _REPLACE_ATTEMPTS - 1:
                raise  # still locked after ~1.5 s: a real problem, report it
            time.sleep(_REPLACE_WAIT_SECONDS * (attempt + 1))


# save_wardrobe's retry: waits 0.1, 0.2, ... 0.5 s between attempts (1.5 s total).
_REPLACE_ATTEMPTS = 6
_REPLACE_WAIT_SECONDS = 0.1



def add_item(fields: dict) -> tuple[dict | None, list[str]]:
    """
    Adds a new item to the wardrobe after validation and normalization.

    Args:
        fields: A dictionary containing the fields of the new wardrobe item.
    """

    wardrobe = load_wardrobe()


    item = fields.copy()
    item["id"] = f"w_{wardrobe['next_id']:03d}"  # Generate a new ID based on next_id

    normalized_item = normalize_item(item)

    errors = validate_item(normalized_item)
    if errors:
        return None, errors

    wardrobe["items"].append(normalized_item)
    wardrobe["next_id"] += 1

    save_wardrobe(wardrobe)

    return normalized_item, []

def get_item(item_id: str) -> dict | None:
    """Return the saved item with this ID, or None if there isn't one."""
    for item in load_wardrobe()["items"]:
        if item["id"] == item_id:
            return item
    return None

def update_item(item_id: str, changes: dict) -> tuple[dict | None, list[str]]:
    """
    Updates fields on an existing item after validation and normalization.

    Args:
        item_id: The ID of the item to edit.
        changes: The fields to change. The ID itself can't be changed.

    Returns:
        (updated item, []) on success, or (None, errors) if the item doesn't
        exist or the edited item fails validation. Nothing is saved on failure.
    """
    if "id" in changes:
        return None, ['Item field "id" cannot be changed.']

    wardrobe = load_wardrobe()
    for index, item in enumerate(wardrobe["items"]):
        if item["id"] == item_id:
            break
    else:
        return None, [f"No item with ID {item_id}."]

    updated = normalize_item({**item, **changes})
    errors = validate_item(updated)
    if errors:
        return None, errors

    wardrobe["items"][index] = updated
    save_wardrobe(wardrobe)
    return updated, []

def remove_item(item_id: str) -> dict | None:
    """
    Removes an item from the wardrobe by its ID.

    Args:
        item_id: The ID of the item to remove.

    Returns:
        The removed item, or None if no item has that ID. next_id is not
        lowered, so the ID is never handed out again.
    """
    wardrobe = load_wardrobe()

    for item in wardrobe["items"]:
        if item["id"] == item_id:
            break
    else:
        return None  # Item not found

    wardrobe["items"] = [i for i in wardrobe["items"] if i["id"] != item_id]
    save_wardrobe(wardrobe)

    return item

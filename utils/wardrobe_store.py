import os
import json
from utils.data_loader import get_example_wardrobe, load_wardrobe_schema
from typing import Optional

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

    for field, value in item.items():
        if field == "id" and not isinstance(value, str):
            errors.append('Item field "id" must be a string.')
        if field == "name":
            if not isinstance(value, str):
                errors.append('Item field "name" must be a string.')
            elif not value.strip():
                errors.append('Item field "name" cannot be empty.')
            elif len(value) > 100:
                errors.append('Item field "name" cannot exceed 100 characters.')
        if field == "category" and value not in ["tops", "bottoms", "outerwear", "shoes", "accessories"]:
            errors.append('Item field "category" must be one of: tops, bottoms, outerwear, shoes, accessories.')
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
    # Rename the temporary file to the target path, replacing the old file
    os.replace(tmp, path)  # Atomic replace to avoid partial writes

    

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

def remove_item(item_id: str) -> bool:
    """
    Removes an item from the wardrobe by its ID.

    Args:
        item_id: The ID of the item to remove.
    """
    wardrobe = load_wardrobe()

    original_count = len(wardrobe["items"])
    wardrobe["items"] = [item for item in wardrobe["items"] if item["id"] != item_id]

    if len(wardrobe["items"]) == original_count:
        return False  # Item not found

    save_wardrobe(wardrobe)

    return True
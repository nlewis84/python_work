from pathlib import Path
import json


def get_favorite_number(path):
    """Get the user's favorite number."""
    if path.exists():
        contents = path.read_text()
        favorite_number = json.loads(contents)
        return favorite_number
    else:
        return None


print(get_favorite_number(Path("chapter-10/favorite_number.json")))

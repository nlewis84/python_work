from pathlib import Path
import json

path = Path("chapter-10/username.json")
contents = path.read_text()
username = json.loads(contents)

print(f"Welcome back, {username}!")
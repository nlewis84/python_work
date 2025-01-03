from pathlib import Path
import json

path = Path("chapter-10/numbers.json")
contents = path.read_text()
numbers = json.loads(contents)

print(numbers)

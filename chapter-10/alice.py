from pathlib import Path

path = Path("chapter-10/alice.txt")

try:
    contents = path.read_text(encoding="utf-8")
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")

from pathlib import Path

contents = "I love programming.\n"
contents += "I love creating new games.\n"
contents += "I love solving problems.\n"

file_path = Path("chapter-10/programming.txt")

file_path.write_text(contents)

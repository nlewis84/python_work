from pathlib import Path

file_path = Path("chapter-10/cthulhu.txt")

try:
    contents = file_path.read_text(encoding="utf-8")
except FileNotFoundError:
    print(f"Sorry, the file {file_path} does not exist.")
else:
    words = contents.split()
    word_count = len(words)
    print(f"The file {file_path} has about {word_count} words.")

    # count the number of times a word appears
    word = "cyclopean"
    word_search = contents.lower().count(word.lower())

    print(f"{word} appears {word_search} times!")

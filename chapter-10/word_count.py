from pathlib import Path


def count_words(path):
    """Count the number of words in a file."""
    try:
        contents = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        word_count = len(words)
        print(f"The file {path} has about {word_count} words.")


filenames = [
    "chapter-10/alice.txt",
    "chapter-10/siddhartha.txt",
    "chapter-10/cthulhu.txt",
    "chapter-10/moby_dick.txt",
]

for filename in filenames:
    path = Path(filename)
    count_words(path)

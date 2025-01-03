from pathlib import Path

# read from cats.txt and dogs.txt
cats_path = Path("chapter-10/cats.txt")
dogs_path = Path("chapter-10/dogs.txt")

try:
    cats = cats_path.read_text()
    dogs = dogs_path.read_text()
except FileNotFoundError:
    pass
else:
    print(cats)
    print(dogs)
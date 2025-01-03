from pathlib import Path

file_path = Path("chapter-10/pi_digits.txt")
contents = file_path.read_text()

lines = contents.splitlines()
for line in lines:
    print(line)

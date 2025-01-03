from pathlib import Path

file_path = Path("chapter-10/learning_python.txt")
contents = file_path.read_text()
print(contents)

print("\nReading the file line by line:")

for line in contents.splitlines():
    print(line)

print("\nReading the file line by line and replacing 'Python' with 'Ruby':")

for line in contents.splitlines():
    print(line.replace("Python", "Ruby"))
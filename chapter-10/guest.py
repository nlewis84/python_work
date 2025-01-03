from pathlib import Path

file_path = Path("chapter-10/guest.txt")
guest = input("Enter your name: ")

file_path.write_text(guest)
from pathlib import Path

file_path = Path("chapter-10/guest_book.txt")

while True:
    guest = input("Enter your name: ")
    guests = []

    if file_path.exists():
        contents = file_path.read_text()
        guests = contents.splitlines()
        
    guests.append(guest)
    file_path.write_text("\n".join(guests))

    print("Hello, " + guest + "! You have been added to the guest book.")
    print("Guests so far:")
    print("\n".join(guests))

    another = input("Would you like to add another guest? (y/n) ")
    if another.lower() != "y":
        break

print("Goodbye!")



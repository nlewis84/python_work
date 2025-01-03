from pathlib import Path
import json

def ask_favorite_number():
    """Ask the user for their favorite number."""
    filename = Path("chapter-10/favorite_number.json")
    message = "What is your favorite number? "

    try:
        favorite_number = int(input(message))
    except ValueError:
        print("Please enter a number.")
    else:
        with filename.open(mode="w") as file:
            json.dump(favorite_number, file)
            print("Favorite number saved!")

ask_favorite_number()
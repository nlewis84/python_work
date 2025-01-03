from pathlib import Path
import json


def get_stored_user(path):
    """Get the stored user information if available."""
    try:
        if path.exists():
            with path.open("r") as file:
                user = json.load(file)
                return user
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error reading file: {e}")
    return None


def get_new_user(path):
    """Get a new username, age, and favorite number, and save it."""
    username = input("What is your name? ")
    age = input("How old are you? ")
    favorite_number = input("What is your favorite number? ")
    user_info = {"username": username, "age": age, "favorite_number": favorite_number}

    try:
        with path.open("w") as file:
            json.dump(user_info, file)
    except Exception as e:
        print(f"Error saving user data: {e}")
        return None

    return user_info


def greet_user():
    """Greet the user by name."""
    path = Path("chapter-10/username.json")
    user = get_stored_user(path)

    if user:
        confirmation = input(f"Is {user['username']} you? (yes/no) ")
        if confirmation.lower() == "yes":
            print(f"Welcome back, {user['username']}!")
        else:
            user = get_new_user(path)
            if user:
                print(f"We'll remember you when you come back, {user['username']}!")
    else:
        user = get_new_user(path)
        if user:
            print(f"We'll remember you when you come back, {user['username']}!")


greet_user()

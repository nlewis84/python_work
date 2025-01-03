# prompt = "If you tell us who you are, we can personalize the messages you see."
# prompt += "\nWhat is your first name? "
# name = input(prompt)
# print(f"Hello, {name}!")

# age = input("How old are you? ")
# age = int(age)
# if age >= 18:
#     print("You are an adult.")
# else:
#     print("You are a minor.")


def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")


greet_user("jesse")
greet_user("sarah")

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    first_name = input("First name: ")
    if first_name == 'q':
        break

    last_name = input("Last name: ")
    if last_name == 'q':
        break

    formatted_name = get_formatted_name(first_name, last_name)

    print(f"\nHello, {formatted_name}!")



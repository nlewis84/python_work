def make_shirt(size, message):
    print(f"\nYour shirt size is {size} and the message is '{message}'.")


make_shirt("large", "I love Python!")
make_shirt(size="medium", message="I love Python!")
make_shirt(message="I love Python!", size="small")
make_shirt("small", "I love Python!")
make_shirt("medium", "I love Python!")
make_shirt("large", "I love Python!")


def make_shirt(size="large", message="I love Python!"):
    print(f"\nYour shirt size is {size} and the message is '{message}'.")


make_shirt()
make_shirt(size="medium")
make_shirt(size="small", message="I love Python!")

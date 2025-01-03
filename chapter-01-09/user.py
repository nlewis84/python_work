# user_0 = {
#     "username": "efermi",
#     "first": "enrico",
#     "last": "fermi",
# }

# for key, value in user_0.items():
#     print(f"\nKey: {key}")
#     print(f"Value: {value}")


class User:
    """A simple attempt to model a user."""

    def __init__(self, username, first_name, last_name):
        """Initialize the user."""
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        """Display a summary of the user's information."""
        print(f"\n{self.first_name} {self.last_name}")
        print(f"  Username: {self.username}")

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print(f"\nWelcome back, {self.username}!")

    def increment_login_attempts(self):
        """Increment the value of login_attempts."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login_attempts to 0."""
        self.login_attempts = 0


# user_1 = User("efermi", "enrico", "fermi")
# user_1.describe_user()
# user_1.greet_user()
# user_1.increment_login_attempts()
# user_1.increment_login_attempts()
# user_1.increment_login_attempts()
# print(f"Login attempts: {user_1.login_attempts}")
# user_1.reset_login_attempts()
# print(f"Login attempts: {user_1.login_attempts}")

# user_2 = User("mcurie", "marie", "curie")
# user_2.describe_user()
# user_2.greet_user()

# user_3 = User("alovelace", "ada", "lovelace")
# user_3.describe_user()
# user_3.greet_user()


class Admin(User):
    """A simple model of an admin user."""
    
    def __init__(self, username, first_name, last_name):
        """Initialize the admin."""
        super().__init__(username, first_name, last_name)
        self.privileges = Privileges()

    def show_privileges(self):
        """Display the privileges this admin has."""
        print("\nPrivileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

    def describe_user(self):
        """Display a summary of the user's information."""
        print(f"\nAdmin: {self.first_name} {self.last_name}")
        print(f"  Username: {self.username}")

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print(f"\nWelcome back, Admin {self.username}!")

class Privileges:
    """A class to store an admin's privileges."""

    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        """Display the privileges this admin has."""
        print("\nPrivileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

# admin = Admin("alovelace", "ada", "lovelace")
# admin.describe_user()
# admin.privileges = [
#     "can add post",
#     "can delete post",
#     "can ban user",
# ]
# admin.show_privileges()

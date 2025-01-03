from user import User


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

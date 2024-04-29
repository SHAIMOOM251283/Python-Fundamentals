class User:
    """A simple attempt to model user."""

    def __init__(self, first_name, last_name, username, actions=[]):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.actions = actions

    def describe_user(self):
        """Brief description of user."""
        description = f"First Name: {self.first_name}\nLast Name: {self.last_name}\nUsername: {self.username}"
        return description

    def greet_user(self):
        """Greet User."""
        print(f"Bonjour {self.username}!")
    
    def display_actions(self):
        """Define Actions"""
        print(f"Dear {self.username}, enjoy: ")
        for action in self.actions:
            print("-", action)

class Privileges:
    """A simple attempt to model privileges for admin."""

    def __init__(self, privileges=[]):
        """Initialize privileges"""
        self.privileges = privileges
    
    def show_privileges(self):
        """Show admin privileges."""
        print("Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

class Admin(User):
    """A simple attempt to model admin."""

    def __init__(self, first_name, last_name, username, privileges=[]):
        """
        Initialize attributes of the parent class.
        Initialize attributes specific to admin.
        """
        super().__init__(first_name, last_name, username)
        self.privileges = Privileges(privileges)
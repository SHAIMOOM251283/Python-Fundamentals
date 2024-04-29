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
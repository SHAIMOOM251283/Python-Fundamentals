class User:
    """A simple attempt to print user information."""

    def __init__(self, first_name, last_name, username, *actions):
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

# List to hold instances of User class
users = []

# Input loop
while True:
    first_name = input("\nEnter First Name: ").title()
    last_name = input("Enter Last Name: ").title()
    username = input("Enter Username: ").upper()
    actions = input("Enter Actions (separated by comma): ").split(", ")
    user_info = User(first_name, last_name, username, *actions)
    users.append(user_info)

    repeat = input("\nDo you want to add another user? (yes/no): ")
    if repeat.lower() != 'yes':
        break

print("\n---- User Profile ----")
# Displaying userss and their details
for user in users:
    print("\n")
    print(user.describe_user())
    user.greet_user()
    user.display_actions()

print("\n")

    
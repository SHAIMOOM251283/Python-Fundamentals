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
    
    def show_privileges(self):
        """Show user's privileges."""
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
        self.privileges = privileges
    
# List to hold instances of User class
users = []

# Input loop
while True:
    first_name = input("\nEnter First Name: ").title()
    last_name = input("Enter Last Name: ").title()
    username = input("Enter Username: ").upper()
    action = input("Enter Actions (seperated by comma): ").split(", ")
    user_info = User(first_name, last_name, username, action)
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

# List to hold instances of Admin class
administrators = []

# Input Loop
while True:
    first_name = input("\nEnter Admin First Name: ").title()
    last_name = input("Enter Admin Last Name: ").title()
    username = input("Enter Admin Username: ").upper()
    privileges = input("Enter Privileges (separated by comma): ").split(", ")
    admin_info = Admin(first_name, last_name, username, privileges)
    administrators.append(admin_info)

    repeat = input("\nDo you want to add another admin? (yes/no): ")
    if repeat.lower() != 'yes':
        break

print("\n--- Admin Profile ---")
for admin in administrators:
    print("\n")
    print(admin.describe_user())
    admin.greet_user()
    admin.show_privileges()

print("\n")

    
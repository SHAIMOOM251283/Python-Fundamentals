class User:
    """A simple attempt to model user."""

    def __init__(self, first_name, last_name, username):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.privilges = []
    
    def describe_user(self):
        """Brief description of user."""
        description = f"First Name: {self.first_name}\nLast Name: {self.last_name}\nUsername: {self.username}"
        return description.title()

    def greet_user(self):
        """Greet User."""
        print(f"Bonjour {(self.username).upper()}!")
    
    def show_privileges(self):
        """Show user's privileges."""
        print("Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")
    
class Admin(User):
    """Represents an admin user."""

    def __init__(self, first_name, last_name, username):
        super().__init__(first_name, last_name, username)
        self.privileges = ["can add post", "can delete post", "can ban user"]
    
user = User('jack', 'son', 'jackson')
print(user.describe_user())
user.greet_user()

print("\n")

admin = Admin('lonesome', 'crow', 'frgtod')
print(admin.describe_user())
admin.greet_user()
admin.show_privileges()
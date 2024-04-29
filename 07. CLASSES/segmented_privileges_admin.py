from segmented_user import User

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
class User:
    """A simple attempt to print user information."""

    def __init__(self, first_name, last_name, age, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
    
    def describe_user(self):
        """Brief description of user."""
        print(f"FIrst Name : {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Sex: {self.sex}")

    def greet_user(self):
        """Greet User."""
        print(f"Bonjour {self.first_name} {self.last_name}!") 

# List to hold instances of User class
users = []

# Input loop
while True:
    first_name = input("\nEnter First Name: ").title()
    last_name = input("Enter Last NAme: ").title()
    age = input("Enter Age: ")
    sex = input("Enter Sex: ")
    user_info = User(first_name, last_name, age, sex)
    users.append(user_info)

    repeat = input("\nDo you want to add another user? (yes/no): ")
    if repeat.lower() != 'yes':
        break

print("\n---- User Profile ----")
# Displaying userss and their details
for user in users:
    print("\n")
    user.describe_user()
    user.greet_user()

print("\n")

    
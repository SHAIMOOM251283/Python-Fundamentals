from unit_user_privileges import *

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
    admin.privileges.show_privileges()

print("\n")
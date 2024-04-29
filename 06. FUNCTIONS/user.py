def build_profile(**user_info):
    """Build a dictionary containing everything we know about a user."""
    return user_info

user_profile = {}

while True:
    print("Enter user information (or type 'done' to finish):")
    key = input("Enter key: ")
    if key.lower() == 'done':
        break
    value = input("Enter value: ")
    user_profile[key] = value

print("User profile:")
print(user_profile)

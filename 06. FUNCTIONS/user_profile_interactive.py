def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = {}
first_name = input("Enter first name: ").title()
last_name = input("Enter last name: ").title()

while True:
    key = input("Enter a piece of information (or type 'done' to finish): ")
    if key.lower() == 'done':
        break
    value = input(f"Enter the value for {key}: ")
    user_profile[key] = value

user_profile = build_profile(first_name, last_name, **user_profile)

print(("\n--- User Profile ---"))
print(f"\n{user_profile}")

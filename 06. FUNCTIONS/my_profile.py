def build_my_profile(first, last, **info):
    """Build a dictionary containing my info"""
    info['first_name'] = first
    info['last_name'] = last
    return info


my_profile = {}

first_name = input("Enter First Name: ").title()
last_name = input("Enter Last Name: ").title()

while True:
    print("Enter a piece of information (or type 'done' to finish)")
    key = input("Enter key: ")
    if key.lower() == 'done':
        break
    value = input(f"Enter the value for {key}: ")
    my_profile[key] = value

my_profile = build_my_profile(first_name, last_name, **my_profile)

print(("\n--- My Profile ---"))
print(f"\n{my_profile}")

def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(f"\n{msg}")

usernames = []

while True:
    usernames.append(input("\nEnter Name: "))

    repeat = input("\nDo you want to enter more names? (yes/no): ").lower()

    if repeat != 'yes':
        break

print("\n--- Greetings ---")
greet_users(usernames)

from pathlib import Path
import json


def get_stored_username(path):
    """Get stored username if available."""
    if path.exists():
        username = json.loads(path.read_text())
        return username
    else:
        return None


def get_new_username(path):
    """Prompt for a new username."""
    username = input("\nEnter Name: ").title()
    path.write_text(json.dumps(username))
    return username


def greet_user():
    """Greet the user by name."""
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        print(f"Is {username} your correct username?")
        response = input("\nEnter yes/no: ")
        if response.lower() != 'yes':
            username = get_new_username(path)
            print(f"\nWe'll remember you when you come back, {username}!")
        else:
            print(f"\nWelcome back, {username}!")

greet_user()

print("\n")

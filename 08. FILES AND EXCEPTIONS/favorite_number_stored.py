from pathlib import Path
import json


def get_stored_number(path):
    """Get stored username if available."""
    if path.exists():
        number = json.loads(path.read_text())
        return number
    else:
        return None


def get_new_number(path):
    """Prompt for a new username."""
    number = input("Enter Number: ")
    path.write_text(json.dumps(number))
    return number


def show_number():
    """Greet the user by name."""
    path = Path('fav_number.json')
    number = get_stored_number(path)
    if number:
        print(f"\nYour favorite number is, {number}!")
    else:
        number = get_new_number(path)
        print(f"\nYour favorite number, '{number}', has been saved!")


show_number()

print("\n")

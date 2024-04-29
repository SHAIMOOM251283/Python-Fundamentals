from pathlib import Path
import json


def get_stored_info(path):
    """Get stored info if available."""
    if path.exists():
        info = json.loads(path.read_text())
        return info
    else:
        return None

def get_new_info(path):
    """Prompt for new info."""
    info = []
    name = input("\nEnter Name: ").title()
    genre = input("\nEnter Genre: ").title()
    instrument = input("\nEnter Instrument: ").title()
    user = {
        "name": name,
        "genre": genre,
        "instrument": instrument
    }
    info.append(user)
    path.write_text(json.dumps(info))
    return info

def show_info():
    """Show info."""
    path = Path('musician.json')
    info = get_stored_info(path)
    if info:
        print("---User Info---")
        for user in info:
            print(f"Name: {user['name']}")
            print(f"Genre: {user['genre']}")
            print(f"Instrument: {user['instrument']}")
            print()
    else:
        info = get_new_info(path)
        name = info[0]["name"]
        print(f"\nYou data has been saved, {name}.")

show_info()

print("\n")


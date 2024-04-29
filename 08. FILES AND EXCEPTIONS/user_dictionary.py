from pathlib import Path
import json

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

Path('user.json').write_text(json.dumps(user))

print(f"\nUser Info: {json.loads(Path('user.json').read_text())}")

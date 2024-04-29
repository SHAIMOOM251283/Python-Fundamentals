from pathlib import Path
import json

username = input("Enter Name: ").title()

#path = Path('username.json')
#contents = json.dumps(username)
#path.write_text(contents)

Path('username.json').write_text(json.dumps(username))

print(f"\nWe'll remember you when you come back, {username}!")
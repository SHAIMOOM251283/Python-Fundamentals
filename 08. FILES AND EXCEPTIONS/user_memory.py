from pathlib import Path
import json

if Path('username.json').exists():
    print(f"Welcome back, {json.loads(Path('username.json').read_text())}!")

else:
    username = input("Enter Name: ").title()
    Path('username.json').write_text(json.dumps(username))
    print(f"\nWe'll remember you when you come back, {username}!")

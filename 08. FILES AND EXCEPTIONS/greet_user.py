from pathlib import Path
import json

#path = Path('username.json')
#contents = path.read_text()
#username = json.loads(contents)
#print(f"Welcome back, {username}!")

print(f"Welcome back, {json.loads(Path('username.json').read_text())}!")


from pathlib import Path
import json

print(f"\nI know your favorite number! It is: {json.loads(Path('favorite_number.json').read_text())}")

print("\n")
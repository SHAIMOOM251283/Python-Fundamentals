from pathlib import Path
import json

numbers = [2, 4, 8, 16, 32, 64]

Path('geometric_sequence.json').write_text(json.dumps(numbers))

print("FILE CREATED!")

print("\n")

print(json.loads(Path('geometric_sequence.json').read_text()))
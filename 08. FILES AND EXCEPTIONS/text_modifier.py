from pathlib import Path

print("---INTRDUCING C---")

lines = Path('learning_python.txt').read_text()

new = lines.replace('Python', 'C').splitlines()

for line in new:
    print(f"\n{line}")


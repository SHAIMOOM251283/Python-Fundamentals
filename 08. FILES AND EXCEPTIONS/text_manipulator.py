from pathlib import Path

print("---INTRDUCING C---")

[print(f"\n{line}") for line in Path('learning_python.txt').read_text().replace('Python', 'C').splitlines()]

print("\n")

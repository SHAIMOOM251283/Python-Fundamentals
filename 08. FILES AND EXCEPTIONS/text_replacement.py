from pathlib import Path

print("---INTRODUCING C---")

print("\n")

lines = Path('learning_python.txt').read_text()

new = lines.replace('Python', 'C')

print(new)

print("\n")
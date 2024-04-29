from pathlib import Path

print("---INTRODUCING PYTHON---")
[print(f"\n{line}") for line in Path('learning_python.txt').read_text().splitlines()]
print("\n")
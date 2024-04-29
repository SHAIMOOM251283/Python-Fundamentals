from pathlib import Path

print("---INTRODUCING PYTHON---")
for line in Path('learning_python.txt').read_text().splitlines():
    print(f"\n{line}")

print("\n")

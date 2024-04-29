from pathlib import Path

path = Path('pi_digits.txt')

print(path.read_text().rstrip())
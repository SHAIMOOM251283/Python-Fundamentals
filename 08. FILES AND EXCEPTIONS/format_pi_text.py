from pathlib import Path

print(Path('pi_digits.txt').read_text().rstrip())
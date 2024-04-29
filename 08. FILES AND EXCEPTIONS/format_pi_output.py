from pathlib import Path

path = Path('pi_digits.txt').read_text().rstrip().splitlines()

for line in path:
    print(line)
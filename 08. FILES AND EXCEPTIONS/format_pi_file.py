from pathlib import Path

[print(line) for line in Path('pi_digits.txt').read_text().rstrip().splitlines()]
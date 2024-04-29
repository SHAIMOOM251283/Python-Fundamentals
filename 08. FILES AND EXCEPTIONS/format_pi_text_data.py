from pathlib import Path

lines = Path('pi_digits.txt').read_text().rstrip().splitlines()

pi_string = ''

for line in lines:
    pi_string += line.lstrip()

print(f"{pi_string[:52]}...")
print(len(pi_string))

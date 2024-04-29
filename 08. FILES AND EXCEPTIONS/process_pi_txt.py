from pathlib import Path

lines = Path('pi_digits.txt').read_text().rstrip().splitlines()
pi_string = ''
for line in lines:
    # pi_string += line
    pi_string += line.lstrip()
print(pi_string)
print(len(pi_string))
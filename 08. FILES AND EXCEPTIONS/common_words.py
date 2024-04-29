from pathlib import Path

filenames = ['alice.txt', 'little_women.txt', 'moby_dick.txt']

print("---WORD OCCURRENCES---")
for filename in filenames:
    file_path = Path(filename)
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read().lower()  # Read content and convert to lowercase for case-insensitive matching
            occurrences = content.count('the ')  # Count occurrences of 'the'
            print(f"\nIn '{filename}', 'the' appears {occurrences} times.")
    except FileNotFoundError:
        pass

print("\n")
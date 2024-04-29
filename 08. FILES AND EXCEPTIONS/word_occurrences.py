from pathlib import Path

filenames = ['alice.txt', 'little_women.txt', 'moby_dick.txt']

word = input("Enter Word: ")

print("---WORD OCCURRENCES---")
for filename in filenames:
    try:
        occurrences = Path(filename).read_text(encoding='utf 8').lower().count(word)
        print(f"\nIn '{filename}', '{word}' appears {occurrences} times.")
    except FileNotFoundError:
        pass

print("\n")
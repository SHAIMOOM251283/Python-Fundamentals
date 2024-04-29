from pathlib import Path

filenames = ['alice.txt', 'little_women.txt', 'moby_dick.txt']
word = input("Enter Word: ")

def word_count(path):
    try:
        occurrences = path.read_text(encoding='utf 8').lower().count(word)
        print(f"\nIn '{filename}', '{word}' appears {occurrences} times.")
    except ValueError:
        pass

print("---WORD OCCURRENCES---")
for filename in filenames:
    word_count(Path(filename))

print("\n")
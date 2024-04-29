from pathlib import Path

def count_words(path):
    """Count the approximate number of words in a file."""
    try:
        contents = path.read_text(encoding='utf-8')
    except (FileNotFoundError):
        with open('missing_files.txt', 'a', encoding='utf-8') as f:
            f.write(f"{path}\n")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt', 'jane_eyre.txt']

print("---WORD COUNT---")
for filename in filenames:
    path = Path(filename)
    count_words(path)
    
print("\n")
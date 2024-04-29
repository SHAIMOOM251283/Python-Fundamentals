from pathlib import Path

filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    file_path = Path(filename)
    print(f"\nContents of {filename}:")
    try:
        print(file_path.read_text().title())
    except FileNotFoundError:
        #print(f"Sorry, the file {file_path} does not exist.")
        pass

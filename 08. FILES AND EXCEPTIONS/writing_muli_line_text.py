from pathlib import Path

contents = "I love programming.\nI love creating new games.\nI also love working with data."

Path('multi_line.txt').write_text(contents)

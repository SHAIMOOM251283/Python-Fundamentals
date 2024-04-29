glossary = {
    'string': 'A sequence of characters, typically used to represent text.',
    'integer': 'A data type used to represent whole numbers without any decimal point.',
    'concatenation': 'The process of combining two or more strings into a single string.',
    'boolean': 'A data type that represents one of two possible values: True or False.',
    'slicing': 'A technique used to extract a portion of a sequence by specifying a start index and an end index.',
}

search_word = input("Enter Word: ")

if search_word in glossary:
    print(f"{search_word}: {glossary[search_word]}")
else:
    print(f"Definition for '{search_word}' not found in the glossary.")

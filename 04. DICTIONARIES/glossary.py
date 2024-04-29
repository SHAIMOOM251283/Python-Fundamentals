glossary = {
    'string': 'A sequence of characters, typically used to represent text.',
    'integer': 'A data type used to represent whole numbers without any decimal point.',
    'concatenation': 'The process of combining two or more strings into a single string.',
    'boolean': 'A data type that represents one of two possible values: True or False.',
    'slicing': 'A technique used to extract a portion of a sequence by specifying a start index and an end index.',
    }

print('string: ' + glossary['string'])
print('\ninteger: ' + glossary['integer'])
print('\nconcatenation: ' + glossary['concatenation'])
print('\nboolean: ' + glossary['boolean'])
print('\nslicing: ' + glossary['slicing'])

glossary['float'] = 'Decimal number with a fractional part.'
glossary['fstring'] = "String formatting method enabling variables and expressions to be embedded directly within strings for formatting."
glossary['list'] = 'Ordered collection of items.'
glossary['conditional statement'] = 'Code that executes based on conditions.'
glossary['dictionary'] = 'Data structure with key-value pairs.' 

print("\nThe following are the definitions of Python terms.")
for k, v in sorted(glossary.items()):
    print('\nWord: ' + k)
    print('Meaning: ' + v)

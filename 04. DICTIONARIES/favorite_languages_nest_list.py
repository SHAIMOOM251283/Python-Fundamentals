favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }

for n, l in sorted(favorite_languages.items()):
    print("\n" + n.title() + "'s favorite languages are:")
    for language in l:
        print("\t" + language.title())

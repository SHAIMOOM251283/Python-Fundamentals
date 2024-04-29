favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

friends = ['phil', 'sarah', 'mark', 'joe']

for name in sorted(friends):
    if name in favorite_languages:
        print('\n' + name.title() + ", thank you for taking the poll.")
    else:
        print('\n' + name.title() + ', please take the poll.')
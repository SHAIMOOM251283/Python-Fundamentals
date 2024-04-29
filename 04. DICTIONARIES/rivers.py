rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'mississippi': 'usa',
    }

for r, c in sorted(rivers.items()):
    if c.lower() == 'usa':
        print('The ' + r.title() + ' runs through ' + c.upper() + '.')
    else:
        print('The ' + r.title() + ' runs through ' + c.title() + '.')

print('\nThe following rivers have been mentioned:')
for r in sorted(rivers.keys()):
    print(r.title())

print("\nThe following countries have been mentioned:")
for c in sorted(rivers.values()):
    print(c.title())

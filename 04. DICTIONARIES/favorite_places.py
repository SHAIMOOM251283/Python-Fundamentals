favorite_places = {
    'jen': 'london',
    'sarah': 'tokyo',
    'edward': 'kyoto',
    'phil': 'osaka',
    }

for n, l in sorted(favorite_places.items()):
    print("\n" + n.title() + "'s favorite place is " + l.title() + '.')
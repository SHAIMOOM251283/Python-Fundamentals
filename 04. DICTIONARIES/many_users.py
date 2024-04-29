users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
    }

for u, v in users.items():
    print("\nUsername: " + u)

    full_name = v['first'] + " " + v['last']
    print("\tFull name: " + full_name.title())

    location = v['location']
    print("\tLocation: " + location.title())


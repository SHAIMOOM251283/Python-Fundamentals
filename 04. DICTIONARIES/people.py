people = {
    'jdaniels': {
        'first': 'jack',
        'last': 'daniels',
        'age': 40,
        'city': 'kyoto'
        },

    'cmorgan': {
        'first': 'captain',
        'last': 'morgan',
        'age': 50,
        'city': 'osaka'
        },
    
    'areyes': {
        'first': 'ancho',
        'last': 'reyes',
        'age': 55,
        'city': 'puebla city' 
        }
    }

for k, v in people.items():
    print('\nIndividual: ' + k)

    full_name = v['first'] + " " + v['last']
    print("\tFull name: " + full_name.title())

    age = v['age']
    print("\tAge: " + str(age))

    city = v['city']
    print('\tCity: ' + city.title())
          
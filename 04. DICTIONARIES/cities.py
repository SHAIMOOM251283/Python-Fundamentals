cities = {
    'kyoto': {
        'country': 'japan',
        'population': '1.457 million',
        'fact':'former capital',
        },
    
    'tokyo': {
        'country': 'japan',
        'population': '13.96 million',
        'fact':'capital',
        },
    
    'osaka': {
        'country': 'japan',
        'population': '2.691 million',
        'fact':'port city',
        },
    }

for k, v in sorted(cities.items()):
    print('\nName of city: ' + k.title())

    country = v['country']
    print('\tCountry: ' + country)

    population = v['population']
    print("\tPopulation: " + population)

    fact = v['fact']
    print('\tFact: ' + fact)



    
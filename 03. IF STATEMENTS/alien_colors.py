alien_colors = []

color = input('Enter Color: ')
alien_colors.append(color)

if 'green' in alien_colors:
    print('You earned 5 points.')
elif 'yellow' in alien_colors:
    print('You earned 10 points.')
elif 'red' in alien_colors:
    print('You earned 15 points.')
else:
    print('You earned 0 points.')

print('Adios!')

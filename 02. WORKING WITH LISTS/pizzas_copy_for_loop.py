my_pizzas = ['americana', 'four seasons', 'chicken supreme', 'pepperoni']
friend_pizzas = my_pizzas[:]

my_pizzas.append('sicilian')
friend_pizzas.append('chicago')

print('My favourite pizzas are:')
for pizza in my_pizzas:
    print(str(pizza).title())

print("\n")

print("My friend's favourite pizzas are:")
for friend in friend_pizzas:
    print(str(friend).title())

requested_toppings = []

topping = input('Enter Topping: ')
requested_toppings.append(topping)

topping = input('Enter Topping: ')
requested_toppings.append(topping)

topping = input('Enter Topping: ')
requested_toppings.append(topping)

print('\n')

if requested_toppings:
    for order in requested_toppings:
        if order == 'green peppers':
            print("Sorry, we are out of green peppers right now.")
        else:
            print('Adding ' + order + '.')
    print('\nFinished making your pizza.')

else:
    print('Are you sure you want plain pizza?')


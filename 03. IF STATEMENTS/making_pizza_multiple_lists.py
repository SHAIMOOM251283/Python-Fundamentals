available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = []

request = input('Enter Topping: ')
if request:
    requested_toppings.append(request)

request = input('Enter Topping: ')
if request:
    requested_toppings.append(request)

request = input('Enter Topping: ')
if request:
    requested_toppings.append(request)

print('\n')

if requested_toppings:
    for order in requested_toppings:
        if order in available_toppings:
            print('Adding ' + order + '.')
        else:
            print("Sorry, we don't have " + order + '.')
    print('\nFinished making your pizza.')

else:
    print('Are you sure you want plain pizza?')
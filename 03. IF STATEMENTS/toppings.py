requested_toppings = []

topping = input('Enter Topping Item: ')
requested_toppings.append(topping)

topping = input('Enter Topping Item: ')
requested_toppings.append(topping)

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
#elif 'pepperoni' in requested_toppings:
#    print('Adding pepperni.')
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
#elif 'extra cheese' in requested_toppings:
#    print('Adding extra cheese.')
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
 
print("\nFinished making your pizza!")

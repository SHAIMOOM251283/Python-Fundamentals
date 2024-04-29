def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print("\nMaking pizza with the f0llowing toppings:")
    for topping in toppings:
        print(f" - {topping}")

topping_list = []

while True:
    topping = input("\nEnter Topping (Enter 'done' to finish): ")

    if topping.lower() == 'done':
        break
    else:
        topping_list.append(topping)

make_pizza(*topping_list)

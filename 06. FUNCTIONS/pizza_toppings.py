def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print("\nToppings for the pizza:")
    for topping in toppings:
        print(f"-{topping}")

topping_list = []

while True:
    topping = input("\nEnter Topping/s: ")
    topping_list.append(topping)

    repeat = input("\nDo you want to enter more toppings? (yes/no): ").lower()

    if repeat != 'yes':
        break

make_pizza(*topping_list)


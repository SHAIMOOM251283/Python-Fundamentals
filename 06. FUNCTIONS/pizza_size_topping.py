def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

while True:
    size = input("\nEnter the size of the pizza (in inches): ")
    toppings = []
    print("\nEnter the toppings for the pizza (Enter 'done' when finished): ")
    while True:
        topping = input("Topping: ")
        if topping.lower() == 'done':
            break
        else:
            toppings.append(topping)
    
    make_pizza(size, *toppings)

    order_another = input("\nDo you want to order another pizza? (yes/no): ")
    if order_another.lower() != 'yes':
        break

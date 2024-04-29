def make_pizza(*toppings):
    """Pizza Topping."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza(input("\nEnter Topping: "))
make_pizza(input("\nEnter Topping: "), input("\nEnter Topping: "), input("\nEnter Topping: "))

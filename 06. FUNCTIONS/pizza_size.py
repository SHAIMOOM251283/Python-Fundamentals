def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza(input("\nEnter Size: "), (input("\nEnter Topping: ")))
make_pizza(input("\nEnter Size: "), (input("\nEnter Topping: ")),
           (input("\nEnter Topping: ")), (input("\nEnter Topping: ")))
# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

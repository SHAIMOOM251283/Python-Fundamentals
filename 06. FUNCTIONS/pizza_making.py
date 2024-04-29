#import pizza_module
#from pizza_module import make_pizza
#from pizza_module import make_pizza as mp
#import pizza_module as p
from pizza_module import *

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
    
    #pizza_module.make_pizza(size, *toppings)
    #make_pizza(size, *toppings)
    #mp(size, *toppings)
    #p.make_pizza(size, *toppings)
    make_pizza(size, *toppings)

    order_another = input("\nDo you want to order another pizza? (yes/no): ")
    if order_another.lower() != 'yes':
        break




from component_restaurant import Restaurant
from component_ice_cream_stand import IceCreamStand

# List to hold instances of Restaurant class
restaurants = []

# Input loop
while True:
    name = input("\nEnter Restaurant Name: ").title()
    cuisine = input("Enter Cuisine Type: ").title()
    served = int(input("Enter Number of Customers Served: "))  # Convert input to integer
    restaurant_info = Restaurant(name, cuisine, served)
    restaurants.append(restaurant_info)

    repeat = input("\nDo you want to add another restaurant? (yes/no): ")
    if repeat.lower() != 'yes':
        break

print("\n---- Restaurants ----")
# Displaying restaurants and their details
for restaurant in restaurants:
    print("\n")
    restaurant.describe_restaurant()
    restaurant.open_restaurant()
    restaurant.print_number_served()  # Corrected method name

    # Interactive part: set number served and increment number served
    new_number_served = int(input("Enter New Number of customers served: "))
    restaurant.set_number_served(new_number_served)

    increment_value = int(input("Enter the increment value: "))
    restaurant.increment_number_served(increment_value)

    restaurant.print_number_served()  # Print updated number served

# List to hold instances of IceCreamStand class
ice_cream_stands = []

# Input loop
while True:
    name = input("\nEnter Ice Cream Stand Name: ").title()
    flavors = input("Enter Flavor (separated by comma): ").split(", ")
    served = int(input("Enter Number of Ice Cream sold: "))  # Convert input to integer
    ice_cream_stand_info = IceCreamStand(name, *flavors, number_served=served)
    ice_cream_stands.append(ice_cream_stand_info)

    repeat = input("\nDo you want to add another ice cream stand? (yes/no): ")
    if repeat.lower() != 'yes':
        break

print("\n---- Ice Cream Stand ----")
# Displaying restaurants and their details
for stand in ice_cream_stands:
    print("\n")
    stand.describe_restaurant()
    stand.open_restaurant()
    stand.print_number_served()  # Corrected method name

    # Interactive part: set number served and increment number served
    new_number_served = int(input("Enter New Number of Ice Cream sold: "))
    stand.set_number_served(new_number_served)

    increment_value = int(input("Enter the increment value: "))
    stand.increment_number_served(increment_value)

    stand.print_number_served()  # Print updated number served

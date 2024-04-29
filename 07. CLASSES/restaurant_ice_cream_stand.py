class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        """Initialize restaurant name, cuisine type, and number of customers served."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        """Brief description of restaurant."""
        print(f"Indulge in culinary delights of {self.restaurant_name}!")
        print(f"Serving you the most delicious {self.cuisine_type} cuisines!")

    def open_restaurant(self):
        """Now Open"""
        print(f"{self.restaurant_name} is now open.")
    
    def set_number_served(self, number):
        """Set the number of customers served."""
        self.number_served = number

    def increment_number_served(self, increment):
        """Increment the number of customers served."""
        self.number_served += increment
    
    def print_number_served(self):
        """Number of Customers Served"""
        if self.number_served == 1:
            print(f"{self.restaurant_name} has served {self.number_served} customer.")
        else:
            print(f"{self.restaurant_name} has served {self.number_served} customers.")

class IceCreamStand(Restaurant):
    """Modeling an Ice Cream Stand."""

    def __init__(self, restaurant_name, *flavors, number_served=0):
        """
        Initialize attributes of the parent class.
        Initialize attributes specific to the Ice Cream Stand.
        """
        super().__init__(restaurant_name, cuisine_type="Ice Cream", number_served=number_served)
        self.flavors = list(flavors)

    def describe_restaurant(self):
        """Brief description of ice cream stand."""
        print(f"Welcome to {self.restaurant_name}!")
        print("We offer the following flavors:")
        for flavor in self.flavors:
            print("-", flavor)
    
    def print_number_served(self):
        """Number of Ice Creams Sold"""
        if self.number_served == 1:
            print(f"{self.restaurant_name} has served {self.number_served} ice cream.")
        else:
            print(f"{self.restaurant_name} has sold {self.number_served} ice creams.")

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




class Restaurant:
    """A simple attempt to model a restraurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Brief description of restaurant."""
        print(f"Indulge in culinary delights of {self.restaurant_name}!")
        print(f"Serving you the most delicious {self.cuisine_type} cuisines!")

    def open_restaurant(self):
        """Now Open"""
        print(f"{self.restaurant_name} is now open.")

class IceCreamStand(Restaurant):
    """A simple attempt to model an ice cream stand."""

    def __init__(self, restaurant_name, *flavors):
        """ 
        Initialize attributes of the parent class.
        initialize attributes specific to the ice cream stand.
        """
        super().__init__(restaurant_name, cuisine_type="Ice Cream")
        self.flavors = list(flavors)

    def describe_ice_cream_stand(self):
        """Brief description of ice cream stand."""
        print(f"Welcome to {self.restaurant_name}, the Ice Cream Stand!")
    
    def display_flavors(self):
        """Display the available flavors."""
        print("Available flavors:")
        for flavor in self.flavors:
            print("-", flavor)
        #print(f"Enjoy the most delicious {self.flavors} ice cream!")
    
# Creating an instance of the Restaurant class
restaurant = Restaurant('Kyoto', 'Japanese')

# Calling methods
restaurant.describe_restaurant()
restaurant.open_restaurant()

print("\n")

# Creating an instance of the IceCreamStand class
ice_cream_stand = IceCreamStand('Rainbow', 'Vanilla', 'Chocolate', 'Strawberry')

# Calling methods
ice_cream_stand.describe_ice_cream_stand()
ice_cream_stand.display_flavors()

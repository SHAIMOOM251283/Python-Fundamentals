from component_restaurant import Restaurant

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

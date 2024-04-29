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

# Creating an instance of the Restaurant class
restaurant = Restaurant('Kyoto', 'Japanese')

# Printing individual attributes
print(f"Welcme to {restaurant.restaurant_name}!")
print(f"Enjoy the most delicious {restaurant.cuisine_type} cuisines!")

# Calling methods
restaurant.describe_restaurant()
restaurant.open_restaurant()
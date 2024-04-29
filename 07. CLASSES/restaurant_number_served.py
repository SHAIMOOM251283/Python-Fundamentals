class Restaurant:
    """A simple attempt to model a restraurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name, cuisine type, and number of customers served."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

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

# Creating an instance of the Restaurant class
restaurant = Restaurant('Kyoto', 'Japanese')

# Printing individual attributes
print(f"Welcme to {restaurant.restaurant_name}!")
print(f"Enjoy the most delicious {restaurant.cuisine_type} cuisines!")

# Calling methods
restaurant.describe_restaurant()
restaurant.open_restaurant()

# Printing the initial number of customers served
print(f"Number of customers served: {restaurant.number_served}")

# Changing the number of customers served and printing again
restaurant.number_served = 50
print(f"Number of customers served: {restaurant.number_served}")

# Using the set_number_served method
restaurant.set_number_served(100)
print(f"Number of customers served: {restaurant.number_served}")

# Using the increment_number_served method
restaurant.increment_number_served(30)
print(f"Number of customers served: {restaurant.number_served}")
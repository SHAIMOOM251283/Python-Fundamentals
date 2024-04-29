class Restaurant:
    """A simple attempt to model a restaurant."""

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

# List to hold instances of Restaurant class
restaurants = []

# Input loop
while True:
    name = input("Enter restaurant name (type 'quit' to exit): ").title()
    if name.lower() == 'quit':
        break
    cuisine = input("Enter cuisine type: ").title()
    restaurant = Restaurant(name, cuisine)
    restaurants.append(restaurant)

# Displaying restaurants and their details
for restaurant in restaurants:
    print(f"\nWelcome to {restaurant.restaurant_name}!")
    print(f"Enjoy the most delicious {restaurant.cuisine_type} cuisines!")
    restaurant.describe_restaurant()
    restaurant.open_restaurant()


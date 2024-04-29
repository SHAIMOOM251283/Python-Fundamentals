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
    
    def print_number_served(self):
        """Number of Customers Served"""
        print(f"{self.restaurant_name} has served {self.number_served} customers.")

    def set_number_served(self, number):
        """Set the number of customers served."""
        self.number_served = number

    def increment_number_served(self, increment):
        """Increment the number of customers served."""
        self.number_served += increment

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

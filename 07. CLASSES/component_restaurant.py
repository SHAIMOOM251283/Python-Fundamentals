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
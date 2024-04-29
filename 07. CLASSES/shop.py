class Shop:
    """A simple attempt to model a shop."""

    def __init__(self, name, type, operating_days, hours):
        """Initialize name and type"""
        self.name = name
        self.type = type
        self.operating_days = operating_days
        self.hours = hours
        self.sale_volume = 0

    def describe_shop(self):
        """Brief description of shop"""
        print(f"Name of shop: {self.name}")
        print(f"Category of items sold: {self.type}")
    
    def opening_hours(self):
        """Opening Hours"""
        print(f"{self.name} is open from {self.operating_days}, {self.hours}.")

    def volume_sold(self, number):
        """Number of items sold"""
        self.sale_volume = number

    def increment_volume_sold(self, increment):
        """Increment sale volume"""
        self.sale_volume += increment

object = Shop('Gamer Paradise', 'Video Games', 'Monday to Friday', '9am to 10pm')

object.describe_shop()
object.opening_hours()

print(f"Initial Sale Volume: {object.sale_volume}")

object.sale_volume = 1000
print(f"Number of {object.type} sold: {object.sale_volume}.") 

object.volume_sold(2000)
print(f"Number of {object.type} sold: {object.sale_volume}.")

object.increment_volume_sold(5000)
print(f"Number of {object.type} sold: {object.sale_volume}.")





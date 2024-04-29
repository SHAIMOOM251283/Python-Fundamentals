class Shop:
    """A simple attempt to model a shop."""

    def __init__(self, name, type, operating_days, hours, sale_volume=0):
        """Initialize name and type"""
        self.name = name
        self.type = type
        self.operating_days = operating_days
        self.hours = hours
        self.sale_volume = sale_volume

    def describe_shop(self):
        """Brief description of shop"""
        print(f"Name of shop: {self.name}")
        print(f"Category of items sold: {self.type}")
    
    def opening_hours(self):
        """Opening Hours"""
        print(f"{self.name} is open from {self.operating_days}, {self.hours}.")

    def print_volume_sold(self):
        """Sale Volume"""
        print(f"{self.name} has sold {self.sale_volume} {self.type}")

    def volume_sold(self, number):
        """Number of items sold"""
        self.sale_volume = number

    def increment_volume_sold(self, increment):
        """Increment sale volume"""
        self.sale_volume += increment

shops = []

while True:
    name = input("\nEnter Name of Shop: ").title()
    type = input("Enter Category of Items sold: ").title()
    operating_days = (f"{input('Enter First Week Day: ').title()} {input('Enter Last Week Day: ').title()}")
    hours = (f"{input('Enter Opening Hour: ')} to {input('Enter Closing Hour: ')}")
    volume = int(input("Enter sale volume: "))
    shop_info = Shop(name, type, operating_days, hours, volume)
    shops.append(shop_info)

    repeat = input("\nDo you want to add another shop? (yes/no): ")
    if repeat.lower() != 'yes':
        break

print("\n----Shops----")
for shop in shops:
    print("\n")
    shop.describe_shop()
    shop.opening_hours()
    shop.print_volume_sold()
    new_sale_volume = int(input("Enter New Sale Volume: "))
    shop.volume_sold(new_sale_volume)
    increment_sale_volume = int(input("Incremented Sale Volume: "))
    shop.increment_volume_sold(increment_sale_volume)
    shop.print_volume_sold()
    


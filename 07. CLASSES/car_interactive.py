class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
    
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()


my_new_car = []

while True:
    make = input("Enter Brand: ").title()
    model = input("Enter Model: ").title()
    year = input("Enter Year of Manufacture: ")
    car_info = Car(make, model, year)
    my_new_car.append(car_info)
    break

print(f"\n{my_new_car[0].get_descriptive_name()}")
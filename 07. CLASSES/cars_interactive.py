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


cars = []

while True:
    make = input("\nEnter Brand: ").title()
    model = input("Enter Model: ").title()
    year = input("Enter Year of Manufacture: ")
    car_info = Car(make, model, year)
    cars.append(car_info)
    
    repeat = input("\nDo you want to add another car? (yes/no): ")
    if repeat.lower() != 'yes':
        break
    
print("\n---- CARS ----")
for car in cars:
    print(car.get_descriptive_name())
    


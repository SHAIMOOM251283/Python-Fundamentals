from car_module import Car, ElectricCar
#from car_module import *

my_mustang = Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())

my_mustang.update_odometer(23)
my_mustang.read_odometer()

print("\n")

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())

my_leaf.battery.describe_battery()
my_leaf.battery.get_range()
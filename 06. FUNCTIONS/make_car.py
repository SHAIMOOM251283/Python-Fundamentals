def make_car(brand, model, **info):
    """Build a dictionary containing info of a car"""
    info['brand name'] = brand
    info['model'] = model
    return info


car_profile = {}

brand_name = input("Enter brand name: ").title()
model_type = input("Enter model: ").title()

while True:
    print("Enter user information (or type 'done' to finish)")
    key = input("Enter key: ")
    if key.lower() == 'done':
        break
    value = input(f"Enter value for {key}: ")
    car_profile[key] = value

car_profile = make_car(brand_name, model_type, **car_profile)

print(("\n--- Car Profile ---"))
print(f"\n{car_profile}")

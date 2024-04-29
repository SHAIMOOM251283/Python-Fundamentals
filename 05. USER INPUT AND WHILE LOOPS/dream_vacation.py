responses = {}

while True:
    name = input('\nWhat is your name?\nEnter: ').title()

    location = input('\nWhere is the destinatin of your dream vacation?\nEnter: ').title()

    responses[name] = location

    print(f"{name} would like to visit {location}.")

    repeat = input("\nDo you want to enter more responses? (yes/no): ").lower()

    if repeat != 'yes':
        break
    
print("\n--- Poll Results ---")
for name, location in responses.items():
    print(f"{name} wants to go to {location}.")
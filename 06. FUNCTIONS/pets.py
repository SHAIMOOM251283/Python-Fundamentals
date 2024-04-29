def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name}.")


pets = []

while True:
    type_of_animal = input('\nEnter Animal Type: ')
    name_of_pet = input("Enter Pet Name: ").title()

    pets.append((type_of_animal, name_of_pet))

    repeat = input("\nDo you want to enter more items? (yes/no): ").lower()

    if repeat != 'yes':
        break

for animal_type, pet_name in pets:
    describe_pet(animal_type, pet_name)

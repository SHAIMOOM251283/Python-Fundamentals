responses = {}

while True:
    name = input('\nWhat is your name?\nEnter: ').title()

    mountain = input('\nWhich mountain would you like to climb?\nEnter: ').title()

    responses[name] = mountain

    print(f"{name} would like to climb {mountain}.")

    repeat = input("\nDo you want to enter more responses? (yes/no): ").lower()

    if repeat != 'yes':
        break
    
print("\n--- Poll Results ---")
for name, mountain in responses.items():
    print(f"{name} wants to climb the {mountain}.")


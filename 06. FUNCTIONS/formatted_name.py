def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()


musicians = []

# while True:
#    musician = get_formatted_name((input('\nEnter First Name: ')), (input('Enter Middle Name: ')), (input('Enter Last Name: ')))
#    musicians.append(musician)

#    repeat = input("\nDo you want to enter more names? (yes/no): ").lower()

#    if repeat != 'yes':
#        break

while True:
    first_name = input("\nEnter First Name: ")
    middle_name = input("\nEnter Middle Name: ")
    last_name = input("\nEnter Last Name: ")

    musicians.append(get_formatted_name(first_name, last_name, middle_name))

    repeat = input("\nDo you want to enter more names? (yes/no): ").lower()

    if repeat != 'yes':
        break

print("\n--- Musicians ---")
for name in musicians:
    print(f"\n{name}")

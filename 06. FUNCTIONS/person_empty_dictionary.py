def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person

musicians = {}

while True:
    first_name = input('\nEnter First Name: ').title()
    last_name = input('Enter Last Name: ').title()

    musician_info = build_person(first_name, last_name)
    musicians[first_name] = musician_info

    repeat = input("\nDo you want to enter more names? (yes/no): ").lower()

    if repeat != 'yes':
        break

print("\n--- Musicians ---")
for first, info in musicians.items():
    print(f"\n{first} {info['last']}")

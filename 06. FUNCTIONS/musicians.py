def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person

first_name = input("Enter first name: ").title()
last_name = input("Enter last name: ").title()

musician = build_person(first_name, last_name)
print(musician)
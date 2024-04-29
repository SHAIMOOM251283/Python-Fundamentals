def city_country(city, country):
    """Return a name of a city and country."""
    if country.lower() == 'usa':
        return f'"{city.title()}, {country.upper()}"'
    else:
        return f'"{city.title()}, {country.title()}"'


info = []

while True:
    city = input("\nEnter City: ")
    country = input("Enter Country: ")

    info.append(city_country(city, country))

    repeat = input("\nDo you want to enter more items? (yes/no): ").lower()

    if repeat != 'yes':
        break

print(("\n--- Cities and Countries ---"))
for name in info:
    print(f"\n{name}")

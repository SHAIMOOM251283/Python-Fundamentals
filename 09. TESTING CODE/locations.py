from city_functions import get_single_string

print("Enter 'q' at any time to quit.")

while True:
    city = input("\nCity: ")
    if city == 'q':
        break
    country = input("Country: ")
    if country == 'q':
        break
    single_string = get_single_string(city, country)
    print(f"\tLocation: {single_string}.")


def describe_city(city, country='usa'):
    """Display information about cities."""
    if country == 'usa':
        print(f"\n{city.title()} is in {country.upper()}.")
    else:
        print(f"\n{city.title()} is in {country.title()}.")


describe_city('denver')
describe_city('miami')
describe_city(city='venice', country='italy')

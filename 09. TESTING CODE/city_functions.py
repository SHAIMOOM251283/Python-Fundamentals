def get_single_string(city, country, population=''):
    """Return a single string."""
    if population:
        location = f"{city}, {country} - {population}"
    else:
        location = f"{city}, {country}"
    return location.title()
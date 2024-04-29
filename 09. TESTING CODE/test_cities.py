from city_functions import get_single_string

def test_city_country():
    """Do locations like Berlin, Germany work?"""
    single_string = get_single_string('Berlin', 'Germany')
    assert single_string == 'Berlin, Germany'


def test_city_country_population():
    """Do locations like Berlin, Germany work?"""
    single_string = get_single_string('Berlin', 'Germany', 'Population 500000')
    assert single_string == 'Berlin, Germany - Population 500000'

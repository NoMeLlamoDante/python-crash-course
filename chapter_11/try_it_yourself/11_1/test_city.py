#11-1 city, country
from city_functions import get_city_country_formatted

def test_city_country():
    """testing 'Santiago, Chile'"""
    formatted_city = get_city_country_formatted("santiago", 'chile')
    assert formatted_city == "Santiago, Chile"
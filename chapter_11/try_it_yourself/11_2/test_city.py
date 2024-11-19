#11-2 city, country
from city_functions import get_city_country_formatted

def test_city_country():
    """testing 'Santiago, Chile'"""
    formatted_city = get_city_country_formatted("santiago", 'chile')
    assert formatted_city == "Santiago, Chile"
    
def test_city_country_poopulation():
    """testing 'Santiago, Chile - population 5000000'"""
    formatted_city = get_city_country_formatted("santiago", 'chile', 5_000_000)
    assert formatted_city == "Santiago, Chile - population 5000000"
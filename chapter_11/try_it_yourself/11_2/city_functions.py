#11-2 City, Country

def get_city_country_formatted(city, country, population=0):
    """Return in formatting 'City, Country - population xxx'"""
    if population>0:
        return f"{city.title()}, {country.title()} - population {population}"
    else:
        return f"{city.title()}, {country.title()}"
def get_formatted_city_name(city, country, population=0):
    return f'{city.title()}, {country.title()} - population {population}' if population else f'{city.title()}, {country.title()}'
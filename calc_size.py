def calc_size(city):
    if len(city.population) < 6:
        city.size = "village"
    elif len(city.population) > 5 and len(city.population) < 9:
        city.size = "town"
    elif len(city.population) > 8 and len(city.population) < 11:
        city.size = "city"
    elif len(city.population) > 10:
        city.size = "metropolis"

    return city
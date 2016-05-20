from gen_name import gen_city_name
from city import City
from random import choice
from random import randint
from gen_person import gen_person


SIZES = ["village", "town", "city", "metropolis"]


def gen_city():
    city = City()
    city.name = gen_city_name()
    city.size = choice(SIZES)
    city.danger = randint(-3, 4)
    city.draw = randint(-3, 4)

    if city.size == "village":
        city.danger -= 1
        city.draw -= 1
    elif city.size == "city":
        city.danger += 1
        city.draw += 1
    elif city.size == "metropolis":
        city.danger += 2
        city.draw += 2

    if city.size == "village":
        population_count = randint(4, 5)
    elif city.size == "town":
        population_count = randint(6, 8)
    elif city.size == "city":
        population_count = randint(9, 10)
    elif city.size == "metropolis":
        population_count = randint(11, 12)

    city.population = []
    for person in range(population_count):
        person = gen_person()
        city.population.append(person)

    return city

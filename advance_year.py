from random import randint
from gen_person import gen_person

def advance_year(city):
    print("A year has passed.")
    for person in city.population:
        person.age += 1

    for person in city.population:
        if person.age < 50 and person.spouse:
            for spouse in city.population:
                if person.spouse == spouse:
                    if person.sex != spouse.sex:
                        if person.deceased == False and spouse.deceased == False:
                            if person.sex == "female":
                                if randint(0, 100) < 20:
                                    child = gen_person()
                                    child.last_name = person.last_name
                                    child.age = 0
                                    child.parents = [person, spouse]
                                    city.population.append(child)
                                    print("{} {} has been born to {} and {} {}.".format(child.first_name, child.last_name, person.first_name, spouse.first_name, spouse.last_name))

    city.draw += randint(-1, 1)
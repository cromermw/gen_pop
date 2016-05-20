from random import randint
from gen_person import gen_person


def draw_and_death(city):
    for person in city.population:
        if person.age > 70 and person.deceased == False:
            if randint(0, 100) < 20:
                person.deceased = True
                print("{} {} has died.".format(person.first_name, person.last_name))
        elif person.age > 50 and person.age < 71 and person.deceased == False:
            if randint(0, 100) < 10:
                person.deceased = True
                print("{} {} has died.".format(person.first_name, person.last_name))
        elif person.age >= 0 and person.age < 51 and person.deceased == False:
            if randint(0, 100) < 5:
                person.deceased = True
                print("{} {} has died.".format(person.first_name, person.last_name))

    if city.draw > 0 and city.draw * 10 > randint(0, 100):
        for person in range(0, city.draw):
            if 50 > randint(0,100):
                person = gen_person()
                parent1 = gen_person()
                parent1.age = person.age + randint(16, 30)
                parent1.sex = "male"
                person.parents.append(parent1)

                parent2 = gen_person()
                parent2.age = person.age + randint(16, 30)
                parent2.sex = "female"
                person.parents.append(parent2)

                city.population.append(person)
                print("{} {} has moved to town.".format(person.first_name, person.last_name))
    if city.draw < 0:
        for person in city.population:
            if not person.spouse and person.age > 17 and person.age < 40:
                if randint(0, 100) < 10:
                    print("{} {} has moved away.".format(person.first_name, person.last_name))
                    person.gone = True

    return city
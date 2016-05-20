from gen_person import gen_person
from random import randint

def gen_generations(population):
    for person in population:
        if person.age < 33 and person.spouse:
            for spouse in population:
                if person.spouse == spouse:
                    person.age += 17
                    spouse.age += 17
                    if person.sex != spouse.sex:
                        child_count = randint(1, 3)
                        for child in range(child_count):
                            child = gen_person()
                            child.age -= 16
                            child.parents = [person, spouse]
                            population.append(child)
        elif person.age < 33 and person.age > 16 and not person.spouse:
            person.age += 50

    for person in population:
        if person.parents == []:
            person.parents = []
            parent = gen_person()
            parent.age += 32
            parent.sex = "male"
            parent.deceased = True
            person.parents.append(parent)

            parent2 = gen_person()
            parent2.last_name = parent.last_name
            parent2.age += 32
            parent2.sex = "female"
            parent2.deceased = True
            person.parents.append(parent2)

    return population

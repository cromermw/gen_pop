from gen_name import gen_first_name
from gen_name import gen_last_name
from person import Person
from random import choice
from random import randint


def gen_person():
    SEXES = ["male", "female"]
    person = Person()
    person.first_name = gen_first_name()
    person.last_name = gen_last_name()
    person.sex = choice(SEXES)
    if person.sex == "male":
        if 4 < randint(0, 100):
            person.preference = "female"
        else:
            person.preference = "male"
    else:
        if 4 < randint(0, 100):
            person.preference = "male"
        else:
            person.preference = "female"

    person.age = randint(16, 32)
    return person

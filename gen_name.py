import random

first_syllables = ["Ab", "Ac", "En", "Es", "Ik", "Il", "Og", "Ot", "Ur", "Uqu", "Yew", "Ys"]
second_syllables = ["ash", "af", "elt", "erg", "if", "ips", "ort", "old", "ulf", "ups"]
third_syllables = ["dan", "dorn", "far", "gold", "son", "span", "tow", "tine", "yew"]
city_syllables = ["berg", "burg", "stan", "ston", "ton", "town", "ville", "wood"]


def gen_first_name():
    firstname_first_syllable = random.choice(first_syllables)
    firstname_second_syllable = random.choice(second_syllables)

    first_name = firstname_first_syllable + firstname_second_syllable

    return first_name

def gen_last_name():
    lastname_first_syllable = random.choice(first_syllables)
    lastname_second_syllable = random.choice(second_syllables)
    lastname_third_syllable = random.choice(third_syllables)

    last_name = lastname_first_syllable + lastname_second_syllable + lastname_third_syllable

    return last_name

def gen_city_name():
    first_syllable = random.choice(first_syllables)
    second_syllable = random.choice(second_syllables)
    third_syllable = random.choice(city_syllables)

    city_name = first_syllable + second_syllable + third_syllable

    return city_name

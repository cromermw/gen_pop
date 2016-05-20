def display_population(city):
    print("{} of {}. Danger: {}. Draw: {}.".format(city.size.title(), city.name, city.danger, city.draw))
    print("")
    #for person in city.population:
        #if person.maiden_name and person.deceased == False:
            #print("{} {}-{}, {} age {} (preference {}). Parents: {} and {} {}".format(person.first_name, person.maiden_name, person.last_name, person.sex, str(person.age), person.preference, person.parents[0].first_name, person.parents[1].first_name, person.parents[1].last_name))
        #elif not person.maiden_name and person.deceased == False:
            #print("{} {}, {} age {} (preference {}). Parents: {} and {} {}.".format(person.first_name, person.last_name, person.sex, str(person.age), person.preference, person.parents[0].first_name, person.parents[1].first_name, person.parents[1].last_name))
    #print("")
    count = 0
    for person in city.population:
        if person.deceased == False and person.gone == False:
            count += 1
    print("Total population: " + str(count))
    if count == 0:
        print("This city has died!")
    count = 0
    for person in city.population:
        if person.spouse:
            if person.spouse.deceased == False and person.deceased == False:
                count += 1
    print("{} couples.".format(int(count / 2)))
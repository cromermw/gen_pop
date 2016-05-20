def marry_couples(population):

    for suitor in population:
        if suitor.age > 15 and suitor.age < 66:
            for match in population:
                if suitor.first_name != match.first_name and suitor.last_name != match.last_name:
                    if match.age > 15 and match.age < 66:
                        if match.sex == suitor.preference and suitor.sex == match.preference:
                            if suitor.spouse == None and match.spouse == None:
                                suitor.spouse = match
                                match.spouse = suitor
                                match.maiden_name = match.last_name
                                match.last_name = suitor.last_name
                                print("{} {} married {} {}, who is now {} {}-{}".format(suitor.first_name, suitor.last_name, match.first_name, match.maiden_name, match.first_name, match.maiden_name, match.last_name))
    print("")
    return population



from gen_city import gen_city
from marry_couples import marry_couples
from display_population import display_population
from gen_generations import gen_generations
from advance_year import advance_year
from draw_and_death import draw_and_death
from calc_size import calc_size

def main():
    city = gen_city()
    marry_couples(city.population)
    gen_generations(city.population)
    display_population(city)
    while True:
        print("")
        input("Press Enter to advance a year.")
        advance_year(city)
        draw_and_death(city)
        marry_couples(city.population)
        calc_size(city)
        display_population(city)
main()

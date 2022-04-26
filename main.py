
planets = (
    ('Mercury', 29),
    ('Venus', 66),
    ('Earth', 91),
    ('Mars', 127),
    ('Jupiter', 460),
    ('Saturn', 839),
    ('Uranus', 1710),
    ('Neptune', 2770),
    ('Pluto', 2760)
)


# gets the selected planet and compares it to the planets in the tuple
def get_selected_dist(selected_planet):
    for planet_info in planets:
        planet, distance = planet_info
        if planet == selected_planet:
            return distance
    return -1


# takes the selected planet's distance and checks if it is negative
def calc_dist(selected_planet):
    selected_dist = get_selected_dist(selected_planet)

    if selected_dist < 0:
        print()
        print('Error!', selected_planet, 'is not in the list')
        return

    dist_diff_list = []

    # compares the planet distances and takes the difference between distances and adds them to a list
    for planet in planets:
        planet_name, planet_dist = planet

        if planet_name != selected_planet:
            dist_diff = abs(selected_dist - planet_dist)

            dist_diff_list.append([planet_name, dist_diff])

    # sorts the planets based on the distance between them, closest to furthest
    def sort_planet(dist_diff_list):
        dist_diff_list.sort(key=lambda x: x[1])
        return dist_diff_list

    sort_planet(dist_diff_list)

    # prints the final sorted list in a manner that makes sense
    for final in dist_diff_list:
        name, dist = final

        print(name, 'is', dist, 'million miles from', selected_planet)
    return


# displays the initial list of planets to pick from
def display_planets():
    print("Planets: ", end=' ')

    for planet_info in planets:
        planet, distance = planet_info

        print(planet, end=' ')

    print()


# asks the user to select a planet from the list and begins the sorting program
def main():
    while True:
        print('=' * 70)
        display_planets()
        print('=' * 70)
        selected_planet = input('Enter the name of a planet, or type Q to exit: ')
        selected_planet = selected_planet.capitalize()
        if selected_planet == 'Q':
            print()
            print('Bye bye!')
            break

        calc_dist(selected_planet)


if __name__ == '__main__':
    main()

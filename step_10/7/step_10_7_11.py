def txt_to_dict():
    with open('planets.txt', encoding='utf-8') as file:
        planets = (line.strip() for line in ''.join(file).split('\n\n') if line.strip())
        for planet in planets:
            yield dict(line.split(' = ') for line in planet.split('\n'))


planets = txt_to_dict()

print(next(planets))


def txt_to_dict():
    with open('planets.txt', encoding='utf-8') as fi:
        # генератор объектов вида:
        # ['Name = Mercury', 'Diameter = 4879.4', 'Mass = 3.302×10^23', 'OrbitalPeriod = 0.241']
        planets = (planet.split('\n') for planet in fi.read().split('\n\n'))

        # генератор объектов вида:
        # [['Name', 'Mercury'], ['Diameter', '4879.4'], ['Mass', '3.302×10^23'], ['OrbitalPeriod', '0.241']]
        planets_info = ((p.split(' = ') for p in planet) for planet in planets)

    # преобразование объектов генератора в словари согласно условию
    for planet in planets_info:
        yield dict(planet)

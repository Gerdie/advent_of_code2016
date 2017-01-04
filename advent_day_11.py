import re

input11 = """The first floor contains a promethium generator and a promethium-compatible microchip.
          The second floor contains a cobalt generator, a curium generator, a ruthenium generator, and a plutonium generator.
          The third floor contains a cobalt-compatible microchip, a curium-compatible microchip, a ruthenium-compatible microchip, and a plutonium-compatible microchip.
          The fourth floor contains nothing relevant."""

microchip_pattern = re.compile(r'(\w+)-compatible')
generator_pattern = re.compile(r'(\w+) generator')


class Microchip(object):

    def __init__(self, material):
        self.material = material

    def __repr__(self):
        return "{} microchip".format(self.material)


class Generator(object):

    def __init__(self, material):
        self.material = material

    def __repr__(self):
        return "{} generator".format(self.material)


class Floor(object):

    def __init__(self, level):
        self.level = level
        self.contents = set()
        self.elevator = False
        if self.level == 0:
            self.elevator = True

    def __repr__(self):
        return str(self.contents)

    @staticmethod
    def is_balanced(altered_set):
        micros = set()
        gens = set()
        for item in altered_set:
            if isinstance(item, Microchip):
                micros.add(item.material)
            else:
                gens.add(item.material)
        contents = gens ^ micros
        if micros & contents and gens & contents:
            return False
        return True

    def can_move(self, *args):
        if len(*args) > 2:
            return False
        return self.is_balanced(self.contents - set(*args))

    def can_accept(self, *args):
        return self.is_balanced(self.contents + set(*args))

building = []

for i, line in enumerate(input11.split("\n")):
    floor = Floor(i)
    microchips = microchip_pattern.findall(line)
    for micro in microchips:
        new = Microchip(micro)
        floor.contents.add(new)
    generators = generator_pattern.findall(line)
    for gen in generators:
        new = Generator(gen)
        floor.contents.add(new)
    print floor
    building.append(floor)

stops = 0
elevator = []
current_floor = 0
# while building[0] or building[1] or building[2] or elevator:
#     if current_floor == 0 or 


# print building

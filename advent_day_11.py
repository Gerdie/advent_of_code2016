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


class Generator(object):

    def __init__(self, material):
        self.material = material


class Floor(object):

    def __init__(self, level):
        self.level = level
        self.contents = set()
        self.elevator = False
        if self.level == 0:
            self.elevator = True

    def is_balanced(self):
        for item in self.contents:
            pass

    def can_move(self, *args):
        if len(*args) > 2:
            return False

    def can_accept(self, *args):
        pass

building = []

for line in input11.split("\n"):
    microchips = microchip_pattern.findall(line)
    generators = generator_pattern.findall(line)
    floor = microchips + generators
    print floor
    building.append(floor)

stops = 0
elevator = []
current_floor = 0
# while building[0] or building[1] or building[2] or elevator:
#     if current_floor == 0 or 


# print building

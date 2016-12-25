
screen = []

for y in xrange(6):
    screen.append(['.' for x in xrange(50)])

with open('input8.txt') as screen_reader:
    for line in screen_reader:
        line = line.rstrip().split(" ")
        if line[0] == "rect":
            dimensions = line[1].split("x")
            width = int(dimensions[0])
            height = int(dimensions[1])
            for y in xrange(height):
                for x in xrange(width):
                    screen[y][x] = 'X'
        elif line[0] == "rotate":
            if line[1] == "row":
                row = int(line[2][2:])
                shift = int(line[-1])
            else:
                col = int(line[2][2:])
                shift = int(line[-1])

print len(screen[0]), len(screen)
print sum(screen[num].count('X') for num in xrange(6))


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
                for x in xrange(shift):
                    screen[row] = screen[row][-1:] + screen[row][:-1]
            else:
                col = int(line[2][2:])
                shift = int(line[-1])
                for y in xrange(shift):
                    r0, r1, r2, r3, r4, r5 = [screen[y1][col] for y1 in xrange(6)]
                    screen[0][col] = r5
                    screen[1][col] = r0
                    screen[2][col] = r1
                    screen[3][col] = r2
                    screen[4][col] = r3
                    screen[5][col] = r4

print sum(screen[num].count('X') for num in xrange(6))
# Part 1: 123

for y in screen:
    for x in y:
        print x,
    print "\n"
# Part 2: AFBUPZBJPS

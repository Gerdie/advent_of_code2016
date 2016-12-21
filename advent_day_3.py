
good_triangles = 0

with open('input.txt') as input_file:
    for i, line in enumerate(input_file):
        line = line.rstrip().split()
        if i % 3 == 0:
            a1, a2, a3 = line
            a1, a2, a3 = int(a1), int(a2), int(a3)
        elif i % 3 == 1:
            b1, b2, b3 = line
            b1, b2, b3 = int(b1), int(b2), int(b3)
        elif i % 3 == 2:
            c1, c2, c3 = line
            c1, c2, c3 = int(c1), int(c2), int(c3)
            if not (a1 + b1 > c1 and a1 + c1 > b1 and b1 + c1 > a1):
                pass
            else:
                good_triangles += 1
            if not (a2 + b2 > c2 and a2 + c2 > b2 and b2 + c2 > a2):
                pass
            else:
                good_triangles += 1
            if not (a3 + b3 > c3 and a3 + c3 > b3 and b3 + c3 > a3):
                pass
            else:
                good_triangles += 1

print good_triangles


good_triangles = 0
i = 0

with open('input.txt') as input_file:
    for line in input_file:
        line = line.rstrip().split()
        a, b, c = line
        a, b, c = int(a), int(b), int(c)
        if not (a + b > c and a + c > b and b + c > a):
            pass
        else:
            good_triangles += 1
        i += 1

print i
print good_triangles

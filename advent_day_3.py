
good_triangles = 0

with open('input.txt') as input_file:
    for line in input_file:
        line = line.rstrip().split()
        a, b, c = line
        if a + b > c or a + c > b or b + c > a:
            continue
        good_triangles += 1

print good_triangles

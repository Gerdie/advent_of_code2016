directions = "R5, R4, R2, L3, R1, R1, L4, L5, R3, L1, L1, R4, L2, R1, R4, R4, L2, L2, R4, L4, R1, R3, L3, L1, L2, R1, R5, L5, L1, L1, R3, R5, L1, R4, L5, R5, R1, L185, R4, L1, R51, R3, L2, R78, R1, L4, R188, R1, L5, R5, R2, R3, L5, R3, R4, L1, R2, R2, L4, L4, L5, R5, R4, L4, R2, L5, R2, L1, L4, R4, L4, R2, L3, L4, R2, L3, R3, R2, L2, L3, R4, R3, R1, L4, L2, L5, R4, R4, L1, R1, L5, L1, R3, R1, L2, R1, R1, R3, L4, L1, L3, R2, R4, R2, L2, R1, L5, R3, L3, R3, L1, R4, L3, L3, R4, L2, L1, L3, R2, R3, L2, L1, R4, L3, L5, L2, L4, R1, L4, L4, R3, R5, L4, L1, L1, R4, L2, R5, R1, R1, R2, R1, R5, L1, L3, L5, R2"
coords = [0,0]
directions = directions.split(", ")
direction_set = set([(0,0)])
visited = None
facing = "N"  # E, N, S, W

for direction in directions:

    if facing == "E":
        if direction[0] == "R":
            facing = "S"
            for y in range(1, int(direction[1:]) + 1):
                new_place = (coords[0], coords[1] - y)
                if new_place in direction_set and not visited:
                    visited = new_place
                else:
                    direction_set.add(new_place)
            coords[1] -= int(direction[1:])
        else:
            facing = "N"
            for y in range(1, int(direction[1:]) + 1):
                new_place = (coords[0], coords[1] + y)
                if new_place in direction_set and not visited:
                    visited = new_place
                else:
                    direction_set.add(new_place)
            coords[1] += int(direction[1:])
    elif facing == "N":
        if direction[0] == "R":
            facing = "E"
            for x in range(1, int(direction[1:]) + 1):
                new_place = (coords[0] + x, coords[1])
                if new_place in direction_set and not visited:
                    visited = new_place
                else:
                    direction_set.add(new_place)
            coords[0] += int(direction[1:])
        else:
            facing = "W"
            for x in range(1, int(direction[1:]) + 1):
                new_place = (coords[0] - x, coords[1])
                if new_place in direction_set and not visited:
                    visited = new_place
                else:
                    direction_set.add(new_place)
            coords[0] -= int(direction[1:])
    elif facing == "S":
        if direction[0] == "R":
            facing = "W"
            for x in range(1, int(direction[1:]) + 1):
                new_place = (coords[0] - x, coords[1])
                if new_place in direction_set and not visited:
                    visited = new_place
                else:
                    direction_set.add(new_place)
            coords[0] -= int(direction[1:])
        else:
            facing = "E"
            for x in range(1, int(direction[1:]) + 1):
                new_place = (coords[0] + x, coords[1])
                if new_place in direction_set and not visited:
                    visited = new_place
                else:
                    direction_set.add(new_place)
            coords[0] += int(direction[1:])
    elif facing == "W":
        if direction[0] == "R":
            facing = "N"
            for y in range(1, int(direction[1:]) + 1):
                new_place = (coords[0], coords[1] + y)
                if new_place in direction_set and not visited:
                    visited = new_place
                else:
                    direction_set.add(new_place)
            coords[1] += int(direction[1:])
        else:
            facing = "S"
            for y in range(1, int(direction[1:]) + 1):
                new_place = (coords[0], coords[1] - y)
                if new_place in direction_set and not visited:
                    visited = new_place
                else:
                    direction_set.add(new_place)
            coords[1] -= int(direction[1:])

#Answer to Part One:
print abs(coords[0]) + abs(coords[1])
#Answer to Part Two:
print abs(visited[0]) + abs(visited[1])


with open('input4.txt') as room_codes:
    for line in room_codes:
        line = line.rstrip().split('-')
        coded = line[:-1]
        last = line[-1]
        for i, char in enumerate(last):
            if char == '[':
                sector = last[:i]
                checksum = last[i+1:-1]
        
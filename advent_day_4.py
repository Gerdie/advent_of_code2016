from collections import Counter

real_sectors = []
i = 0
with open('input4.txt') as room_codes:
    for line in room_codes:
        line = line.rstrip().split('-')
        coded = line[:-1]
        last = line[-1]
        for i2, char in enumerate(last):
            if char == '[':
                sector = int(last[:i2])
                checksum = last[i2+1:-1]
        c = Counter("".join(coded))
        top_five = sorted(c.values())[-5:]
        contenders = []
        ties = []
        for num in top_five[::-1]:
            if top_five.count(num) == 1:
                for letter in c:
                    if c[letter] == num:
                        contenders.append(letter)
            else:
                for letter in c:
                    if c[letter] == num:
                        ties.append(letter)
                        if len(ties) == top_five.count(num):
                            contenders = contenders + sorted(ties)
                            ties = []

        if checksum == "".join(contenders[:5]):
            real_sectors.append(sector)
        if i < 5:
            print coded, sector, checksum, "".join(contenders[:5]), len(checksum), len("".join(contenders[:5]))
        i += 1

print sum(real_sectors)
print i
        
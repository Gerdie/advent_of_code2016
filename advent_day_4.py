from collections import Counter

test_data = ["aaaaa-bbb-z-y-x-123[abxyz]",
             "a-b-c-d-e-f-g-h-987[abcde]",
             "not-a-real-room-404[oarel]",
             "totally-real-room-200[decoy]"]

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
        top_five = sorted(c.values(), reverse=True)[:5]
        contenders = []
        ties = []
        for num in top_five:
            for letter in [l for l in sorted(c.keys()) if c[l] == num]:
                    if letter not in contenders:
                        contenders.append(letter)
                        break

        if checksum == "".join(contenders[:5]):
            real_sectors.append(sector)
        # print coded, sector, checksum, "".join(contenders[:5]), len(checksum), len("".join(contenders[:5]))
        i += 1

print "real sectors: ", len(real_sectors)
print "end sum: ", sum(real_sectors)
        
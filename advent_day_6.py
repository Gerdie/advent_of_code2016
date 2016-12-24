test_input = ["eedadn",
              "drvtee",
              "eandsr",
              "raavrd",
              "atevrs",
              "tsrnev",
              "sdttsa",
              "rasrtv",
              "nssdts",
              "ntnada",
              "svetve",
              "tesnvt",
              "vntsnd",
              "vrdear",
              "dvrsen",
              "enarar"]

result = {}
result_str = ""

with open('input6.txt') as santa_code:
    for line in santa_code:
        line = line.rstrip()
        for i, char in enumerate(line):
            result[i] = result.get(i, [])
            result[i].append(char)

for num in xrange(len(result)):
    result_str += str(min(result[num], key=result[num].count))

print result_str

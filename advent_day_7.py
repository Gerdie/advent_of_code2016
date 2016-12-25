inside = False
tls_support = []
test_input = ["abba[mnop]qrst",
              "abcd[bddb]xyyx",
              "aaaa[qwer]tyui",
              "ioxxoj[asdfgh]zxcvbn"]
ssl_support = []

with open('input7.txt') as ip_file:
    for line in ip_file:
        line = line.rstrip()
        ssl_in = []
        ssl_out = []
        inside = False
        for i, char in enumerate(line):
            if char == '[':
                inside = True
            elif char == ']':
                inside = False
            elif i + 2 < len(line) and '[' not in line[i:i+3] and ']' not in line[i:i+3]:
                if char == line[i + 2] and char != line[i+1]:
                    if inside:
                        ssl_in.append(line[i:i+3])
                        if line[i+1] + char + line[i+1] in ssl_out:
                            ssl_support.append(line)
                            break
                    else:
                        ssl_out.append(line[i:i+3])
                        if line[i+1] + char + line[i+1] in ssl_in:
                            ssl_support.append(line)
                            break

print len(ssl_support)
# Part B: 231

# with open('input7.txt') as ip_file:
#     for line in ip_file:
#         line = line.rstrip()
#         supports_tls = False
#         inside = False
#         for i, char in enumerate(line):
#             if char == '[':
#                 inside = True
#             elif char == ']':
#                 inside = False
#             elif i + 3 < len(line) and '[' not in line[i:i+4] and ']' not in line[i:i+4]:
#                 if char == line[i + 3] and line[i+1] == line[i + 2] and char != line[i+1]:
#                     if inside:
#                         supports_tls = False
#                         break
#                     else:
#                         supports_tls = True
#         if supports_tls:
#             tls_support.append(line)

# print len(tls_support)
# Part A: 115

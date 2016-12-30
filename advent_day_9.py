word_count = ""
inside = False
parens = False
ignore = -1
test_cases = ["(3x3)XYZ",
              "A(2x2)BCD(2x2)EFG",
              "(6x1)(1x3)A",
              "X(8x2)(3x3)ABCY"]

def compress_file(filename):
    word_count = ""
    inside = False
    parens = False
    ignore = -1
    with open(filename) as compressed_file:
        for line in compressed_file:
            for i, char in enumerate(line.rstrip()):
                if char in "    ":
                    continue
                if char == '(':
                    parens = True
                    if i > ignore:
                        start = i
                        inside = True
                elif char == ')' and i > ignore:
                    end = i
                    inside = False
                    compress = line[start+1: end].split("x")
                    # eval_i = i+1
                    char_amt = int(compress[0])
                    repeat_amt = int(compress[1])
                    word_count += line[i+1: i + char_amt + 1] * repeat_amt
                    ignore = i + char_amt
                elif i > ignore and not inside:
                    word_count += char

    secondary = open('secondary.txt', 'w')
    secondary.write(word_count)
    if parens:
        compress_file('secondary.txt')
    print len(word_count)

compress_file('input9.txt')
# Part 1: 150914

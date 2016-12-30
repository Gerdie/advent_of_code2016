word_count = 0
inside = False
parens = False
ignore = -1
test_cases = ["(3x3)XYZ",
              "A(2x2)BCD(2x2)EFG",
              "(6x1)(1x3)A",
              "X(8x2)(3x3)ABCY"]

# def compress_file(line):
# word_count = ""
# inside = False
# parens = False
# ignore = -1
with open('input9.txt') as compressed_file:
    for line in compressed_file:
        while '(' in line:
            inside = False
            ignore = -1
            decomp_line = ""
            for i, char in enumerate(line.rstrip()):
                if char in "    " or i < ignore:
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
                    print compress
                    # eval_i = i+1
                    char_amt = int(compress[0])
                    repeat_amt = int(compress[1])
                    decomp_line += line[i+1: i + char_amt + 1] * repeat_amt
                    ignore = i + char_amt
                if i > ignore and not inside:
                    decomp_line += char
            line = decomp_line
        word_count += len(line)

# secondary = open('secondary.txt', 'w')
# secondary.write(word_count)
    # if parens:
    #     compress_file(word_count)
    print word_count

# with open('input9.txt') as compressed_file:
#     word_total = ""
#         for line in compressed_file:
#             word_total += compress_file(line)
#         if parens:
#             compress_file(word_count)
# Part 1: 150914

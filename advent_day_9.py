word_count = 0
inside = False
eval_i = None
ignore = -1
test_cases = ["(3x3)XYZ",
              "A(2x2)BCD(2x2)EFG",
              "(6x1)(1x3)A",
              "X(8x2)(3x3)ABCY"]

with open('input9.txt') as compressed_file:
    for line in compressed_file:
        for i, char in enumerate(line.rstrip()):
            if char in "    ":
                continue
            if char == '(' and i > ignore:
                start = i
                inside = True
            elif char == ')' and i > ignore:
                end = i
                inside = False
                compress = line[start+1: end].split("x")
                # eval_i = i+1
                char_amt = int(compress[0])
                repeat_amt = int(compress[1])
                word_count += char_amt * repeat_amt
                ignore = i + char_amt
            elif i > ignore and not inside:
                word_count += 1

print word_count
# Part 1: 150914

from time import time

test_cases = ["(3x3)XYZ",
              "A(2x2)BCD(2x2)EFG",
              "(6x1)(1x3)A",
              "X(8x2)(3x3)ABCY"]

more_tests = "(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN"  # should be 445


starting = time()
compressed_file = open('input9.txt').read().strip()
compressed_time = time()
print "Took {} seconds to read input file".format(compressed_time - starting)


def decompress_file(s):
    word_count = 0
    while '(' in s:
        start = s.find('(')
        end = s.find(')', start)
        word_count += start
        marker = s[start+1:end].split('x')
        char_amt = int(marker[0])
        repeat_amt = int(marker[1])
        s = s[end+1: end+char_amt] * repeat_amt + s[end+1+char_amt:]
    if '(' not in s:
        word_count += len(s)

    return word_count


print decompress_file(more_tests)

ending = time()

print "Took {} seconds to decompress file".format(ending - compressed_time)
# Part 1: 150914

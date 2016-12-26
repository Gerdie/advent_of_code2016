word_count = 0
inside = False
eval_i = None
ignore = 0

with open('input9.txt') as compressed_file:
    for line in compressed_file:
        for i, char in enumerate(line.rstrip()):
            if char in "    ":
                continue
            if char == '(':
                start = i
                inside = True
            elif char == ')':
                end = i
                inside = False
                compress = line[start+1: end].split("x")
                eval_i = i+1
            elif i == eval_i:
                char_amt = int(compress[0])
                repeat_amt = int(compress[1])
                word_count += char_amt * repeat_amt
                ignore = i + char_amt
            elif i >= ignore and not inside:
                word_count += 1

print word_count

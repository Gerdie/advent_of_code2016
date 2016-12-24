from hashlib import md5

door_code = "reyedfim"
test_code = "abc"
result = {}
result_str = ""

i = 0

while len(result) < 8:
    hash_test = md5(door_code + str(i))
    hash_test = hash_test.hexdigest()
    if hash_test[:5] == "00000":
        try:
            position = int(hash_test[5])
            character = hash_test[6]
            if position in result or position > 7:
                pass
            else:
                result[position] = character
        except ValueError:
            pass
    i += 1

for num in xrange(8):
    result_str += result[num]
print result_str
#Part A: f97c354d
#Part B: 863dde27

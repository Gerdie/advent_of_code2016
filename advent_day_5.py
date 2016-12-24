from hashlib import md5

door_code = "reyedfim"
test_code = "abc"
result = []

i = 0

while len(result) < 8:
    hash_test = md5(door_code + str(i))
    hash_test = hash_test.hexdigest()
    if hash_test[:5] == "00000":
        result.append(hash_test[5])
    i += 1

print result
#Part A: f97c354d

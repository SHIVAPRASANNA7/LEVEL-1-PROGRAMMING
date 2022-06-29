
test_tup = (19, 33, 31, 7, 64, 8)


print("The original tuple is : " + str(test_tup))


K = 2


test_tup = list(test_tup)
temp = sorted(test_tup)
res = tuple(temp[:K] + temp[-K:])


print("The extracted values : " + str(res))

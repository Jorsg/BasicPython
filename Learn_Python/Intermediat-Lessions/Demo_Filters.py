newlist = [1,3,5,7,9,11,13,14,17]

result = list(filter(lambda x: x % 2 == 0, newlist))
print(result)
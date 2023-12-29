def add(x):
    return x+(4*2)

newlist = [10,20,30,40,50,60,70]
result = list(map(add,newlist ))
#print(list(map(add,newlist )))

result1 = list(map(lambda x: x *2, newlist))
print(result1)
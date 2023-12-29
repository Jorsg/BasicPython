def function1():
    print("something")
    print("someone")
    print("sometimes")


#function1()


def function2(ending):
    for x in range(1,ending,3):
     print(((x*3)*(-1))+100)

#function2(50)


fruit = ["apple", "Mango","Pinapple", "Banana","Bluberry"]
def function3():
    for x in fruit:
        print(x)

#function3()


username = "jorsgar"
passw = "1234admin"

def functionlogin(username, passw):
    if(username == "jorsgar" and passw == "1234admin"):
        print("Succefully Access")
    else:
        print("You don't have access")

#functionLogin(username, passw)

def add(a, b):
    print(a+b)

# add(12, 23)
# add(190, 300)
# add(19045, 1)


def functionadd(a, b):
    c = a + b
    return c

result = functionadd(123, 676)
#print(result)


class Students:

    def __init__(self, name, contact):
        self.name = name
        self.contact = contact

    def getdata(self):
        print("Accepting data")
        self.name = input("Enter name:  ")
        self.contact = input("Enter contact:  ")

    def putdata(self):
        print("There is name: {0} and There is contact: {1}".format(self.name, self.contact))

# Jors = Students("Nata", "s")
# Jors.getdata()
# Jors.putdata()

class Engeneertudent(Students):

    def __init__(self, age):
        self.age = age

    def engeneer(self):
        print("I am engeneer student")

Nat = Engeneertudent(35)
Nat.engeneer()
Nat.getdata()
Nat.putdata()

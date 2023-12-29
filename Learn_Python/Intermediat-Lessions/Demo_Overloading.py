class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


    def __add__(self, z):
        x = self.x + z.x
        y = self.y + z.y
        return Point(x, y)

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)


poit1 = Point(2, 6)
poit2 = Point(3, 4)
print(poit1 + poit2)        

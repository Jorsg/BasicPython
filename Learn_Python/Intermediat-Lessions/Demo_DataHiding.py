class Myclass:

    __hiddenvarible = 0

    def add(self, increment):
        self.__hiddenvarible += increment
        print(self.__hiddenvarible)

objectHiding = Myclass()
objectHiding.add(5)
print(objectHiding)
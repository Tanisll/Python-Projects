class Protected:
    def __init__(self):
        self.__privateVar = 12

    def getPrivate (self):
        print (self.__privateVar)

    def setPrivate (self, private):
        self.__privateVar = private
obj = Protected()
obj.getPrivate()
obj.setPrivate(23)
obj.getPrivate()


class Protected:
    def __init__(self):
        self._protectedVar = 0

obj = Protected()
obj._protectedVar = 34
print (obj._protectedVar)
# The outcome should be 34 and not 0. By assigning the Protected method
# to the variable obj, we were then able to modify the variable _protectedVar

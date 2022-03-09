# [x] 1 This class should make use of a private attribute or function.
# [x] 2 This class should make use of a protected attribute or function.
# [x] 3 Create an object that makes use of protected and private.
#----------------------------------------------------------------------

class Protected:               #base protected code
    def __init__(self):        #base protected code
        self._protectedVar = 0 #base protected code denoted with a single underscore
        self.__privateVar = 12        #private code

    def getPrivate(self):             #private code
        print(self.__privateVar)      #private code denoted with a double underscore prefix

    def setPrivate(self, private):    #private code
        self.__privateVar = private   #private code

obj = Protected()              #base protected code
obj.getPrivate()                      #private code
obj.setPrivate(23)                    #private code
obj.getPrivate()                      #private code
obj._protectedVar = 34         #base protected code
print(obj._protectedVar)       #base protected code


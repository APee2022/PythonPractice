# we are adding a bookmarks in chrome about Encapsulation study for more details.
'''
Encapsulation

An object variables should not always be directly accessible.
The method can ensure the correct values are set. If an incorrect value
 is set, the method can return an error.
'''

class Student:
    __name = "Ravi"
    def __init__(self):
        print(self.__name)
        self.__displayinfo()
    def __displayinfo(self):
        print("welcome")

obj=Student()
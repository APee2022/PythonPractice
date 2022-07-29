# we are adding a bookmarks in chrome about getter and setter study for more details
# Getters are the methods that are used in Object-Oriented Programming (OOPS) to access a class's private attributes.
#The setter is a method that is used to set the property's value. It is very useful in object-oriented programming to set the value of private attributes in a class.

#Generally, getters and setters are mainly used to ensure the data encapsulation in OOPs.
class Student:
    def __init__(self):
        self.__name=""
    def getname(self):
        return self.__name
    def setname(self,name):
        self.__name=name

obj=Student()
obj.setname("Testing")
name=obj.getname()
print(name)
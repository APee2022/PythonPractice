# for more details visit GFG
'''
Instance Variable: It is basically a class variable without a static modifier and is usually shared by all class instances.
Across different objects, these variables can have different values. They are tied to a particular object instance of the class,
therefore, the contents of an instance variable are totally independent of one object instance to others.
'''
'''
Class Variable: It is basically a static variable that can be declared anywhere at class level with static. 
Across different objects, these variables can have only one value. These variables are not tied to any particular object of the class, 
therefore, can share across all objects of the class. 
'''
class Car:

    wheels = 4#Class variables

    def __init__(self):
        self.mil = 10 #Instance variables
        self.com = "BMW" #Instance variables

c1 = Car()
c2 = Car()

c1.mil = 8

Car.wheels = 5 #modified class variables

print(c1.com , c1.mil , c1.wheels)
print(c2.com , c2.mil , c2.wheels)
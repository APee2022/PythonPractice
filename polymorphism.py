'''
poly:- stands for MANY
Morph:- stand for FORM

There are four method of Polymorphism
:-Duck Typing
:-Operator Overloading
:-Method Overloading
:-Method Overriding
'''
# Duck Typing (study from GFG)

class PyCharm:

    def execute(self):
        print("Compiling")
        print("Running")

class MyEditor:

    def execute(self):
        print("Spell check")
        print("Convention check")
        print("Compiling")
        print("Running")

class Laptop:

    def code(self,ide):
        ide.execute()

#ide = PyCharm()
ide = MyEditor()
lap1 = Laptop()
lap1.code(ide)

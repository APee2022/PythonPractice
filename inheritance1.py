'''
When we create object of sub class it will call init of sub class first if we
have call super then it will first call init of super class then call init of sub class
'''
class A:

    def __init__(self):
        print("in A init")

    def feature1(self):
        print("1 working")

    def feature2(self):
        print("2 working")

class B(A):

    def __init__(self):
        super().__init__()#while using super we call all the features of parent/super class
        print("in B init")

    def feature3(self):
        print("3 working")

    def feature4(self):
        print("4 working")

a1 = B()


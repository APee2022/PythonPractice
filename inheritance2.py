# Method Resolution Order(MRO) study about MRO on GFG.
class A:

    def __init__(self):
        print("in A init")

    def feature1(self):
        print("1 working")

    def feature2(self):
        print("2 working")

class B:

    def __init__(self):
        super().__init__()
        print("in B init")

    def feature1(self):# we change the feature3 as feature1 which is same in class A
        print("3 working")

    def feature4(self):
        print("4 working")

class C(A,B):
    def __init__(self):
        super().__init__()# Method Resolution Order(MRO): As we know that
        print("in C init") # init method print itself and there are two classes A and B
                          # A is in left side and B is in right side. we got only class A in output
                      # because (MRO) prefer only left to print.

a1 = C()
a1.feature1()# it's also work on MRO method we have feature1 in both class
             # A and B but get only A in output.

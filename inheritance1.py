class A:
    def displayA(self):
        print("welcome to wscubetech A")

class B:
    def displayB(self):
        print("welcome B")
# here we are using multiple inheritance property in which we are calling class A and class B in class C.
# that's why we are using only single object " obj = C() " to call all the classes A, B and C.
class C(A,B):
    def displayC(self):
        print("welcome to WscubeTech C")
obj = C()
obj.displayA()
obj.displayB()
obj.displayC()
class A:
    def displayA(self):
        print("welcome to wscubetech A")

class B(A):# here A is inherted in B.
    def displayB(self):
        print("welcome B")
# we are calling 2 classes with single object this is single line inheritance
#let create one more class to watch multi level inheritance

class C(B): # here B is inherted in C.
    def displayC(self):
        print("welcome to WscubeTech C")
obj = C()
obj.displayA()
obj.displayB()
obj.displayC()
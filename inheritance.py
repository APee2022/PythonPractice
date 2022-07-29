# Here A is a parent class/super class and B is child class/sub class of A and C is child class of B

class A:
    def feature1(self):
        print("1 working")

    def feature2(self):
        print("2 working")

class B(A):# single level inheritance
    def feature3(self):
        print("3 working")

    def feature4(self):
        print("4 working")

#class C(A,B):# multiple inheritance
class C(B):# multi level inheritance
    def feature5(self):
        print("5 working")

a1 = A()

a1.feature1()
b1 = B()
b1.feature2()

c1 = C()
c1.feature5()
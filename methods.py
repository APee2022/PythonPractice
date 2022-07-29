# Study this lecture again (lect..no..:--57)
'''
we add some article about getter & setter and types of methods
in booksmarks watch them later
'''
class Student:
    school = 'Telusko' #Class variables or static variable
    def __init__(self,m1,m2,m3):# m1,m2,m3 are Instance variables
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3
    '''
    def get_m1(self):
        return self.m1
    # getter help to get the value while setter use to set the value
    def set_m1(self,value):
        self.m1 = value
    '''
    @classmethod
    def getSchool(cls):
        return cls.school

    @staticmethod
    def info():
        print("This is student class")

s1 = Student(34,47,32)
s2 = Student(89,32,12)

print(s1.avg())
print(Student.getSchool())
Student.info()
# accessor methods
# mutator methods
'''
 when we import any modules it call all the functions,
  to not call all the functions and call some special function
  we have to use __name__ == "__main__"

In given example below when we import module from __nam__calc file
we import only add function but we get all function imported
to avoid this we have to use *if __name__ == "__main__"*
'''
from __nam__calc import add

def fun1():
    add()
    print("from fun1")

def fun2():
    print("from fun2")



def main():#here we create a function name main() to call fun1() and fun2()
    fun1()
    fun2()

main() # here we call main() function
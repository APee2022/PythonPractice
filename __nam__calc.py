



def add():
    print("result 1 is ",__name__)

def sub():
    print("result 2 is")

def main():#here we create a function name main() to call add() and sub()
    print("in calc main")
    add()
    sub()

if __name__ == "__main__":
   main()
class Computer:
    def __init__(self):# while using __init__ we don't need to call the function
        print("in init")

    def config(self):# here we have to call the function
        print("i5, 16gb, 1TB")

com1 = Computer()# here we are creating the object for class Computer

com1.config() # Here we are calling the function config()
#or
#Computer.config(com1)# Here we are calling the function config()
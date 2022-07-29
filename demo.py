# input(), it is used for user input
# int(), it is used for integer value
# float(), it is used for decimal value
# eval(), it is used for both int and float value

a = input("Enter the value 1:-") # for this method we get string value
b = input("Enter the value 2:-")
print(a+" "+b)

a = int(input("Enter the value 1:-")) # here we get addition of two numbers
b = float(input("Enter the value 2:-"))
print(a+b)

a = eval(input("Enter the value 1:-")) # in previous example if we use float in int value we get an error but while using eval we don't get error
b = eval(input("Enter the value 2:-"))
print(a+b)
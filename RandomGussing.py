import random
cnumber = random.randrange(1,101)
userInput = int(input("enter your number:--"))
if userInput>cnumber:
    print("computer number",cnumber)
    print("your guess number is too high")
elif cnumber>userInput:
    print("computer number", cnumber)
    print("your guess number is too low")
else:
    print("computer number", cnumber)
    print("your guess number is equal")
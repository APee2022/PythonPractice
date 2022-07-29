a = eval(input("enter the first value:="))
b = eval(input("enter the second value:="))
opr = input("select an operator +, -, *, / :=")
if opr == "+":
    print(a+b)
elif opr == "-":
    print(a-b)
elif opr == "*":
    print(a*b)
elif opr == "/":
    print(a/b)
else:
    print("invalid opr")

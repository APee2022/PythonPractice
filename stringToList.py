# here we learn about how to convert string into list
#if we have single entry
'''
n = input("enter the value :-")
print(n)
l=n.split()
print(l)
'''
# if we have multiple entery
l=[]
for a in range(1,4):
    n=input("enter the value" + str(a) +":-")
    l.append(n)
print(l)
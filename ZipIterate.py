# if we have to iterate two list together than we use zip() function
l=[10,20,30,40]
#l1=[2,3,4,88,77] # in l & l1 no of items are same if we put different no of items than in output we get only same no of item.
l1=[2,3,4,88]

for a,b in zip(l,l1):
    print(a,b)

print("")
#another method
t = len(l)

for h in range(t):
    print(l[h],l1[h])
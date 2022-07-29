l=[10,20,30,40,50,60,80,90]
t=len(l)
for a in range(t):
    print(l[a])

print("")
# another method without len()
for a in l:
    print(a)

print("")
# to print in reverse order
for a in range(t-1,-1,-1):# t = 8, t-1=7 so start from index no 7
    print(l[a])
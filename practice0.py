#Tn = a+(n-1)*d
#Sn = n/2 (2a+(n−1)d)
a = int(input("enter the first number of series:--"))
d = int(input("enter the common difference:--"))
n = int(input("enter the number of terms:--"))
Tn = a+(n-1)*d
Sn = (n/2 * (2 * a + (n - 1) * d))
print(Tn)
print(Sn)
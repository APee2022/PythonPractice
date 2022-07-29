#count() :- it is used to count a number or character that how much time it appears.
#max() :- it gives the maximum values, in case of alphabets A<B<C<D....
#min() :- it gives the minimum values.
#sort() :- it arrange in assending order.
#reverse() :- it reverse the original value.
#index() :- when we enter the number or character it gives the index number.

l = [10,33,43,5,9,10,10]
m = ["hello","world","ok","ok"]

z = l.count(10)
print(z)
x = m.count("ok")
print(x)

print("")

q = max(l)
print(q)
w = max(m)
print(w)

print("")

e = min(l)
print(e)
r = min(m)
print(r)

print("")

l.sort() #we don't put l.sort into a variable ex: a=l.sort. we get none as output
print(l)
m.sort()
print(m)

print("")
l.reverse()
print(l)
m.reverse()
print(m)

print("")

a=l.index(9)
print(a)
s=m.index("hello")
print(s)



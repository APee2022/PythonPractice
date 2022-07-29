# study from w3school.
names = ("navin","kiran","harsh")
comps = ("dell","apple","ms")
'''
zipped = dict(zip(names,comps))# we also use set,tuple,list.
print(zipped)
'''
#we also use for loop to iterate value
zipped = zip(names,comps)

for (a,b) in zipped:
    print(a,b)
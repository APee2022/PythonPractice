# we learn here about FILTER, MAP and REDUCE
'''
 there is a inbuilt function in python to filter a sequence
 known as filter()
 filter takes two arguments : filter(function,iterable)
'''

from functools import reduce

'''
def isEven(n):
    return n%2==0

nums = [3,2,6,8,4,6,2,9]
evens = list(filter(isEven,nums))

print(evens)
'''
# using lambda method
nums = [3,2,6,8,4,6,2,9]
evens = list(filter(lambda n : n%2==0,nums))

print(evens)

# map :- if we have to change every value of a sequence we use map() function
#map takes two arguments : map(function,iterable)
nums = [3,2,6,8,4,6,2,9]
evens = list(filter(lambda n : n%2==0,nums))

doubles = list(map(lambda n : n+2,evens))

print(doubles)

# reduce() function is used for sum all the element in a sequence
#reduce takes two arguments : reduce(function,sequence)
# reduce() function is a module so we have to import it first
'''
def addAll(a,b):
    return a+b
nums = [3,2,6,8,4,6,2,9]
evens = list(filter(lambda n : n%2==0,nums))

doubles = list(map(lambda n : n+2,evens))

sum = reduce(addAll,doubles)
print(sum)'''

# Now use lambda method
nums = [3,2,6,8,4,6,2,9]
evens = list(filter(lambda n : n%2==0,nums))

doubles = list(map(lambda n : n*2,evens))

sum = reduce(lambda a,b : a+b,doubles)
print(sum)

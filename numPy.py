# creating arrays in different ways in numPy.
#there is 6 ways to create array:
# array(), linspace(), logspace(), arange(), zeros(), ones().

from numpy import *
# this ia array() method
arr = array([1,2,3,4,5])# here change any value to float and then check dtype
print(arr.dtype)
print(arr)

# linspace() methods
arr = linspace(0,15,16)# here 0 and 15 is range and 16 tell us to divide this range in 16 parts
print(arr) # if we not use 16 than it divide the range in 50 parts default.

# arange() methods
arr = arange(1,15,2)# here 1 and 15 is range but 2 is step which means skip 2 steps.
print(arr)

# logspace() methods
arr = logspace(1,40,5)# here range is log of 1 to log of 40 and divide into 5 parts.
print(arr)

# zeros() methods
arr = zeros(5)# print 5 zeros to form an array
print(arr)

# ones() methods
arr = ones(5,int) # print 5 ones to form an array
print(arr)
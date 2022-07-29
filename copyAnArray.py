from numpy import *
arr1 = array([2,6,8,1,3])

#arr2 = arr1 # this is known as alicing method
'''arr2 = arr1.view()
   in view() method we are doing shallow copy which means if we change the value
   of arr1 we also got change in arr2'''
#arr2 = arr1.view()

'''arr2 = arr1.copy() in copy method we are doing deep copy which means
if we change the value of arr1 we can not change the value of arr2'''
arr2 = arr1.copy()
arr1[1] = 7

print(arr1)
print(arr2)

print(id(arr1))
print(id(arr2)) # the memory location of arr1 and arr2 is same array in same id

# to copying the array we use arr1.view()
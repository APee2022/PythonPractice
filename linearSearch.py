'''
Linear search is a method of finding elements within a list.
It is also called a sequential search.
It is the simplest searching algorithm because
it searches the desired element in a sequential manner.
'''
pos = -1# return -1 which means element is not present in the list.

def search(list,n):
    i = 0
    while i< len(list):# try this with for loop.
        if list[i] == n:
            globals()['pos'] = i
            return True
        i=i+1

    return False

list = [5,8,4,6,9,2]
n=1

if search(list,n):
    print("Found at ",pos+1)
else:
    print("Not Found")
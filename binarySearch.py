'''
Binary search is a searching algorithm which is used to
search an element from a sorted array.
It cannot be used to search from an unsorted array.
Binary search is an efficient algorithm and is better than
linear search in terms of time complexity.
'''
pos = -1# return -1 which means element is not present in the list.

def search(list,n):
    l = 0
    u = len(list)-1
    while l <= u:
        mid = (l+u) // 2

        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                l = mid+1
            else:
                u = mid-1

    return False

list = [4,7,8,12,45,99] # in case of binary search list must be sorted
n=4

if search(list,n):
    print("Found at ",pos+1)
else:
    print("Not Found")
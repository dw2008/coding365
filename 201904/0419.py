#Given an array A of integers, return true if and only if it is sorted in ascending order.
#
#sorted means: A[0] < A[1] < ... A[i-1] < A[i]

 

#Example 1:

#Input: [2,1]
#Output: false
#Example 2:

#Input: [3,5,5]
#Output: true
#Example 3:

#Input: [0,3,2,1]
#Output: false
 
def isSorted(alist) :
    for i in range(1, len(alist)) :
        if alist[i] >= alist[i -1] :
            continue
        else :
            return False
    return True
numbers = [-1, 29, 3, 4, 5]
print(isSorted(numbers))
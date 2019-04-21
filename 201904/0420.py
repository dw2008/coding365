#Given an array A of integers, return true if and only if it is a valid mountain array.

#Recall that A is a mountain array if and only if:

#A.length >= 3
#There exists some i with 0 < i < A.length - 1 such that:
#A[0] < A[1] < ... A[i-1] < A[i]
#A[i] > A[i+1] > ... > A[B.length - 1]
 

#Example 1:

#Input: [2,1]
#Output: false
#Example 2:

#Input: [3,5,5]
#Output: false
#Example 3:

#Input: [0,3,2,1]
#Output: true
numbers = [0, 3, 2, 1]
def findPeak(alist) :
    largestNumber = -10000
    peakIndex = -1
    for i in range(0, len(alist)) :
        if alist[i] > largestNumber :
            largestNumber = alist[i]
            peakIndex = i
    return peakIndex
print(findPeak(numbers))
def isMountain(alist) :
    peakIndex = findPeak(alist)
    if peakIndex == 0 or peakIndex == len(alist) - 1  :
        return False
    for i in range(1, peakIndex + 1) :
        if alist[i] > alist[i - 1] :
            continue
        else :
            return False
    for i in range(peakIndex, len(alist) - 1) :
        if alist[i] > alist[i + 1] :
            continue
        else :
            return False
    return True
print(isMountain(numbers))

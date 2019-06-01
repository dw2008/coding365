"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
def addTogeth(alist, target) :
    for i in range(0, len(alist)) :
        for j in range(i + 1, len(alist)) :
            if alist[i] + alist[j] == target :
                return i, j
    return -1
alist = [2, 7, 11, 15]
print(addTogeth(alist, 18))
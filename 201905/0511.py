# review binary search problem
# Given a list of ascending sorted number and a target
# Write a function to return: if target is in the list, return the index of target, otherwise return the insertion point
numbers = [1, 2, 4, 6, 7]
def getPos(alist, target) :
    start = 0
    end = len(alist) - 1
    while start + 1 < end :
        md = start + (end - start) / 2
        if alist[md] == target :
            return md
        if alist[md] > target :
            end = md
        else :
            start = md
    if target < alist[start] :
        return start
    if target > alist[end] :
        return end + 1
    if target >= alist[start] and target < alist[end] :
        return end
print(getPos(numbers, 5))
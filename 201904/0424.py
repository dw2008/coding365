#Given an ordered list which is sorted in descending order and a target. 
#Return the position in the list if target exist in the list
#If target does not exist in the list, return the position this target should be inserted to. 
#Example: [4, 2, 1] target = 3, return 1(the third position in the list) since 3 should be inserted before 2 and after 4.
numbers = [5, 5, 4, 1, 0]
def getPos(alist, target) :
    start = 0
    end = len(alist) - 1
    while start + 1 < end :
        md = start + (end - start) / 2
        if alist[md] == target :
            return md
        if alist[md] < target :
            end = md
        else :
            start = md
    if target > alist[start] :
        return start
    if target < alist[end] :
        return end + 1
    if target <= alist[start] and target > alist[end] :
        return end
print(getPos(numbers, 3))
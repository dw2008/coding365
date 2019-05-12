#Given an ordered list which is sorted in ascending order and a target. 
#Return the position in the list if target exist in the list
#If target does not exist in the list, return the position this target should be inserted to. 
#Example: [1, 2, 4] target = 3, return 2(the third position in the list) since 3 should be inserted before 4 and after 2. 
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
print(getPos(numbers, 100))
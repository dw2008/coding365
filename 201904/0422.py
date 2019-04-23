#Given a list of integers (sorted in decending order) and a target
#Use binary search to find the index of the target. If target does not exist, return -1.
#Print out how many loops did you use until find the target or quite the program
numbers = [10, 8, 3, 1, 0]
def genList(rangea) :
    result = list()
    for x in range(rangea, -1, -1) :
        result.append(x)
    return result

def binarySearch(alist, target) :
    start = 0
    end = len(alist) - 1
    counter = 0
    while start + 1 < end :
        counter += 1
        md = start + (end - start) / 2
        print("start =", start)
        print("end =", end)
        print("md =", md)
        if alist[md] == target :
            return md
        if alist[md] < target :
            end = md
        else :
            start = md
    if alist[start] == target :
        return start
    if alist[end] == target :
        return end
    return -1
    print("Ran this many times :", counter)
print(binarySearch(genList(10), 5))
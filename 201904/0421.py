#Given a list and a target, return the index of the target if it exist in list, otherwise return -1
#Example: [0, 2, 3, 4, 10, 44] target is 10, return 4
numbers = [0, 2, 3, 4, 10, 44]
def genList(arange) :
    result = list()
    for x in range(0, arange) :
        result.append(x + 1)
    return result
print(genList(10))
def binarySearch(alist, target) :
    start = 0
    end = len(alist) - 1
    counter = 0
    while start < end :
        counter += 1
        print("B Looped :", counter)
        md = start + (end - start) / 2
        print(md)
        if alist[md] == target :
            return md
        if alist[md] > target :
            end = md
        else :
            start = md
    return -1
print(binarySearch(numbers, 10))

#Generate a list contains 1 - 1000
#Search 998 in this list by linear search, print out how many loops it takes
#Search by binary search and compare with linear

testList = genList(1000)
def linearSearch(alist, target) :
    i = 0
    for x in alist :
        print("Looped :", i)
        i += 1
        if x == target :
            return True
    return False
print(linearSearch(testList, 998))
print(binarySearch(testList, 998))

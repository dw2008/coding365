#Given a list of numbers, can you return the average and median. 
#Hints: Can you do it with a unsorted list? If not, search "python list sort" to find out how to sort a list. 
def mean(alist) :
    alist.sort()
    number = 0
    count = len(alist)
    for x in alist :
        number += x
    print(alist)
    return number / count
def median(alist) :
    alist.sort()
    return alist[len(alist) / 2]
someList = [6, 2, 1]
print(mean(someList))
print(median(someList))
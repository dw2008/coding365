"""
Given a list of intergers, and a target number, can you write a function to return the index of the target number efficiently? 
What algorithm(s) do you need? 
"""
def bubbleSort(alist) :
    number = len(alist)
    for i in range(number) :
        for j in range(0, number-1-i) :
            if alist[j] > alist[j + 1] :
                alist[j], alist[j + 1] = alist[j + 1], alist[j]
def binarySearch(alist, target) :
    start = 0
    end = len(alist) - 1
    while start + 1 < end :
        md = start + (end - start) / 2
        print(md)
        if alist[md] == target :
            return md
        if alist[md] < target :
            start = md
        else :
            end = md
    if alist[start] == target :
        return start
    if alist[end] == target :
        return end
    return -1
alist = [1, 5, 1, 6, 7, 3]
bubbleSort(alist)
print(alist)
print(binarySearch(alist, 7))

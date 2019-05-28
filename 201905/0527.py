"""
Search for "insertion sort" and implement it in python. 
What is the complexity of this algorithm? 
"""
def insertionSort(alist, target, swap) :
    result = list()
    for x in alist :
        if x == target :
            result.append(swap)
        else :
            result.append(x)
    return result
alist = [0, 5, 3, 2, 66, 2, 2, 2, 2]
print(insertionSort(alist, 2, 3))
print("The insertion sort's complexity is N^2.")
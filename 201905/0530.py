"""
change your bubble sort algorithm to sort the list in reversing order. 
"""
def bubbleSort(alist) :
    number = len(alist)
    counter = 0
    for i in range(number) :
        for j in range(0, number-1-i) :
            if alist[j] < alist[j + 1] :
                alist[j], alist[j + 1] = alist[j + 1], alist[j]
            counter += 1
alist = [9, 2, 5, 1, 42]
bubbleSort(alist)
print(alist)
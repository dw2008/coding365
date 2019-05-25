#use bubblesort
def bubbleSort(alist) :
    number = len(alist)
    for i in range(number) :
        for j in range(0, number-i-1) :
            if alist[j] > alist[j + 1] :
                alist[j], alist[j + 1] = alist[j + 1], alist[j]
alist = [1, 6, 3, 2, 6, 9, 0]
bubbleSort(alist)
print(alist)
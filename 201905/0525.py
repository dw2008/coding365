#Use bubble sort to sort an array in place. Print out the whole array on each swap. Count how many swap needed to sort a list. 
def bubbleSort(alist) :
    number = len(alist)
    counter = 0
    for i in range(number) :
        for j in range(0, number-1-i) :
            if alist[j] > alist[j + 1] :
                alist[j], alist[j + 1] = alist[j + 1], alist[j]
            print(alist)
            counter += 1
    print("# of times needed to swap:", counter)
alist = [9, 2, 5, 1, 42]
bubbleSort(alist)
print("The list is now", alist)
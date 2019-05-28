"""
Learn what is a big O notaion from https://www.youtube.com/watch?v=D6xkbGLQesk&t=46s
What is the big O of bubble sort?
"""
# It's the relationship between the input and the steps required to complete the algorithm
def bubbleSort(alist) :
    number = len(alist)
    for i in range(number) :
        for j in range(0, number-1-i) :
            if alist[j] > alist[j + 1] :
                alist[j], alist[j + 1] = alist[j + 1], alist[j]
alist = [4, 5, 2, 6, 8]
bubbleSort(alist)
print(alist)
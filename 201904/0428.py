#Implement a function to return a 2D array which filled with 0s. 

#Implement another function takes above 2D array as input and mark its border as 1 then return it. 

#Printout this 2D array
def gen2D(rows, cols) :
    arr = [[0] * cols] * rows
    return arr
def markBorder(array) :
    row = len(array)
    col = len(array[0])
    count = 0 
    for i in range(0, row) :
        for j in range(0, col) :
            # if i == 0 :
            #     array[0][0] = 1
            # if i == row - 1 :
            #     array[0][col - 1] = 1
            array[i][j] = count
            count += 1
    return array
arr = gen2D(5, 5)
for row in arr :
    print(row)
arr = markBorder(arr)
for row in arr :
    print(row)
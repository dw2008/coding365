#Create a 2D array https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/
#Set border elements to 1 and other elements to 0.
#Print out this 2D array.
rows, cols = (5, 5) 
arr = [[0]*cols]*rows 
arr[0][4] = 1
arr[0][0] = 1
for row in arr: 
    print(row) 
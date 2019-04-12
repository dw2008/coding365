#create a func: pass in a list of integers, print out all element in the list in reverse order. 
def printList(list) :
	for i in range(0, len(list)) :
		print(list[i])
aList = [2, 6, 20, 3, 5, 3]
print(printList(aList))
def printListBack(list) :
	for i in range(len(list) - 1, -1, -1) :
		print(list[i])
print(printListBack(aList))
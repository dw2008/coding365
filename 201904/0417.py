#use while loop to printout all elements in a list from star to end then from end to start. 
#https://www.w3schools.com/python/python_while_loops.asp
numbers = [4, 2, 7, 1]
def printOutA(alist) :
	result = list()
	i = 0
	while i < len(alist) :
		result.append(alist[i])
		i += 1
	return result
print(printOutA(numbers))
def printOutB(alist) :
	result = list()
	i = len(alist) - 1
	while i > -1 :
		result.append(alist[i])
		i -= 1
	return result
print(printOutB(numbers))

#Create a function, input two lists of intergers, return a new list which contains larger numbers in each position. 
#Note: lists in inputs may have different length. 
#You can use only 1 for loop in your fucntion to generate the new list. 
#Example: inputs: [1,2,3,4] [3,2,1] outputs: [3,2,3,4]
numbers1 = [1, 2, 3, 4]
numbers2 = [3, 2, 1]
def returnList(alist, blist) :
	result = list()
	size = 0
	if len(alist) < len(blist) :
		size = len(alist)
	else :
		size = len(blist)
	for i in range(0, size) :
		if alist[i] > blist[i] :
			result.append(alist[i])
		else :
			result.append(blist[i])
	return result
print(returnList(numbers1, numbers2))
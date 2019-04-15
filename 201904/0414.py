#Create a function, input two lists of intergers, return a new list which contains larger numbers in each position. 
#Note: list in inputs has same length. You can use only 1 for loop in your fucntion to generate the new list. 
#Example: inputs: [1,2,3] [3,2,1] outputs: [3,2,3]
numbers1 = [6, 2, 0]
numbers2 = [3, 2, 1]
def largestNumber(alist, blist) :
	result = list()
	for i in range(0, len(alist)) :
		if alist[i] > blist[i] :
			result.append(alist[i])
		else :
			result.append(blist[i])
	return result
print(largestNumber(numbers1, numbers2))
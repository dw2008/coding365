#Given a list of intergers such as {1,3,4,5,7,8} and a target, such as 5
#Can you write a function to return the index of the target? 
#example: for above list, if target is 5 then return 3. (index start from?)
def findIndex(list, target) :
	for i in range(0, len(list)) :
		if list[i] == target :
			return i
	return -1
target = 1
aList = [1, 2, 4, 5, 7, 8]
print(findIndex(aList, target))
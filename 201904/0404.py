#Given a list of numbers, write a function to find the largest number in the list, create another function to find the smallest number 
#Example: for list{1,2,3, 4, 5,3, 4,2} find largest function should return 5, find smallest function should return 1
aListOfNumbers = [2, 4, 2, 8, 5, 4, 1337]

def theLargestNumber(list) :
	largestNumber = -10000
	for x in list :
		if x > largestNumber :
			largestNumber = x
	return largestNumber
print(theLargestNumber(aListOfNumbers))

def theSmallestNumber(list) :
	smallestNumber = 10000
	for y in list :
		if y < smallestNumber :
			smallestNumber = y
	return smallestNumber
print(theSmallestNumber(aListOfNumbers))
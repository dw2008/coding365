#Create a list, put 1000 random integer in it
#Create a func, find the largest number in the list. 
import random

def genRandom(size) :
	result = list()
	for x in range(size) :
		randomNumber = random.randint(-size, size)
		result.append(randomNumber)
	return result

def largestNumInList(list) :
	largestNum = -10000
	for x in list :
		if x > largestNum :
			largestNum = x
	return largestNum

# print(largestNumInList(genRandom(1000)))
aList = genRandom(100)
print(aList)
print(largestNumInList(aList))
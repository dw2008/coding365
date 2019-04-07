#Create a function, take list size as input, return a list of random integers(range -1000, 1000).
#Create a function, take above list as input, return the sum of this list. 
#Create a function, use above two functions, return the average of the list. 
import random

def genRandom(size) :
	result = list()
	for x in range(size) :
		randomnumber = random.randint(-1000, 1000)
		result.append(randomnumber)
	return result

def sumOfList(list) :
	sumOfNumbers = 0
	for x in list :
		sumOfNumbers = sumOfNumbers + x
	print(sumOfNumbers)
	return sumOfNumbers

def daAverage(list) :
	total = sumOfList(list)
	size = len(list)
	average = total / size
	return average
print(daAverage(genRandom(100)))

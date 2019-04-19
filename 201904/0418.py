#Create a function, take list size as input, return a list of random integers(range -1000, 1000).
#Create a function, take above list as input, return the sum of this list. 
#Create a function, use above two functions, return the average of the list.
#Note: use while loop instead of for to implement 
import random
def genRandom(size) :
    result = list()
    i = 0
    while i < size :
        result.append(random.randint(-1000, 1000))
        i += 1
    return result

print(genRandom(10))

def returnSum(alist) :
    result = 0
    i = 0
    while i < len(alist) :
        result = result + alist[i]
        i += 1
    return result

print(returnSum(genRandom(10)))

def returnAvg(alist) :
    result = 0
    i = 0
    sum = returnSum(alist)
    return sum / len(alist)

print(returnAvg(genRandom(10)))
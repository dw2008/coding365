#Your program should able to accepting a number from command line.  
#if the nubmer is <= 0, return nothing. else do following
#Create an empty list called "all" then add 1 to this number in it. 
#Create one list called evenList, another list called oddList. 
#Loop "all", for each number, if it is even, add to evenList, if it is odd, add to oddList
#print out eventList and oddList in different line. 
import sys
number = int(sys.argv[1:][0])

if(number <= 0) :
	print("This number is less or equal to 0")
	quit()

listboi = list()
for x in range(1, number + 1):
   listboi.append(x)
print(listboi)
oddList = list()
evenList = list()

for x in listboi :
	if(x % 2 == 0) :
		evenList.append(x)
	else :
		oddList.append(x)

print(f"This is a list of all the odd numbers before {number}")

print(oddList)

print(f"This is a list of all the even numbers before {number}")

print(evenList)

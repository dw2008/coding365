# create a list and add 1 to 100, total 100 number in it using for loop
# print out all numbers in list one by one using for loop
# print out all numbers reversely using for loop
aList = list()
for x in range(1, 101) :
	aList.append(x)

print(aList)
print(len(aList))

for i in range(len(aList)-1, -1, -1) :
	print(aList[i])
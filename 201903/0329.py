# create a list and add 1 to 100, total 100 number in it using for loop(https://www.w3schools.com/python/python_for_loops.asp)
# print out all numbers in list one by one using for loop
# print out all numbers reversely using for loop
alist = list()
for x in range(1, 101):
  alist.append(x)
print(alist)
for x in range(99, 0, -1):
 	print(alist[x])
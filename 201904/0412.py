#Create a function.
#Input: a list of string or integers
#Output: for element in even index, print out "Even Index: {index number} - Element: {Element value}"
# for element in odd index, print out "This is Odd: {Element value} "
def oddOrEven(list) :
	for i in range(0, len(list)) :
		if i % 2 == 0 :
			print(f"Even Index: {i} - Element: {list[i]}")
		elif i % 2 == 1 :
			print(f"This is in an Odd position: {list[i]}")
aList = [1, 2, 3, "s", 0]
bList = [1, 4, 9, 2, 5, 6]
print(oddOrEven(bList))
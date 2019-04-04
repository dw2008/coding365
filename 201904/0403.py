#Create two functions:
# func1: speicalSub(x, y), pass in two integers, if x > y return x - y, if x <=y return 0
# func2: speicalSub(x, y), pass in two integers, if x or y is 0, return 0, else return x times y
def specialSub(x,y) :
	if x > y :
		return x - y
	return 0
print(specialSub(21, 16))

def notSpecialSub(x, y) :
	if x == 0 or y == 0 :
		return 0
	return x * y
print(notSpecialSub(5, 3))
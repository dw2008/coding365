#Design a func, pass in two numbers and return its sum "def add(x, y)"
#Think about what is the type of x and y
#Design a func called addString, pass in two single digit numbers represented as string and return its sum in string format as well.
#Example: addString("1", "2") shoudl return "3"
def add(x, y) :
	return x + y
print(add(1,2))

def addString(x, y) :
	result = int(x) + int(y) 
	return str(result)

print(addString("21", "31"))
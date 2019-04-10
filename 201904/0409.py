#You have the function to calculate POW, can you optimize it so it only needs half of the running time?
#Hints: 2 * 2 * 2 * 2 = 4 * 4. to calculate 2 ^ 4, you can just calculate 2 ^ 2  then reuse the result to calculate 2 ^ 4 
#Your function in 0408.py is good when y is even, can you make it work when y is odd? 
def calculatePow(x, y) :
	result = 1
	if y == 0 :
		return result
	for i in range(y) :
		result = result * x
	return result

def fastPow(x, y) :
	ny = int(y / 2)
	half = calculatePow(x, ny)
	if y % 2 == 0 :
		return half * half
	else :
		return half * half * x

print(fastPow(2, 3))
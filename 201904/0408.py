#You have the function to calculate POW, can you optimize it so it only needs half of the running time?
#Hints: 2 * 2 * 2 * 2 = 4 * 4. to calculate 2 ^ 4, you can just calculate 2 ^ 2  then reuse the result to calculate 2 ^ 4 
def calculatePOW(x, y) :
	result = 1
	if y == 0 :
		return result
	for i in range(y) :
		result = result * x
	return result

base = 2
power = 4

def fastPOW(x, y) :
	y = int(y / 2)
	half = calculatePOW(x, y)
	return half * half


print(fastPOW(base, power))
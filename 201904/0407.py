#create a function, inputs are two integers, x and y, returns x ^ y
#Example, input (2, 2) return 2 ^ 2 = 4
def powPowPow(x, y) :
	result = 1
	if y == 0 :
		return result
	for i in range(y) :
		result = result * x
	return result

bass = 1234
power = 1234


test1 = powPowPow(bass, power)	
print(f"{bass} to the power of {power} = {test1}")

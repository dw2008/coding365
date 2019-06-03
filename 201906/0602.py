"""
Write a function to find the position of the operator and return it
"""
def findOperator(ainput) :
    for i in range(0, len(ainput)) :
        op = ainput[i]
        if op == "+" or op == "-" or op == "*" or op == "/" :
            return i
print(findOperator("1 + 1"))
def findLeftOperand(ainput) :
    index = findOperator(ainput)
    return int(ainput[0:index])
print(findLeftOperand("100 + 1"))
def findRightOperand(ainput) :
    index = findOperator(ainput)
    return int(ainput[index + 1:len(ainput)])
print(findRightOperand("1 + 1000000000"))
def calc(op, left, right) :
    if op == "+" :
        return (left, op, right, "=", (left + right))
    elif op == "-" :
        return (left, op, right, "=", (left - right))
    elif op == "*" :
        return (left, op, right, "=", (left * right))
    elif op == "/" :
        return (left, op, right, "=", (left / right))
equation = "4 / 2"
print(calc(equation[findOperator(equation)], findLeftOperand(equation), findRightOperand(equation)))
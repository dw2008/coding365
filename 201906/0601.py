"""
Write a function which can interperate a string to a math equation then print out the calculation result

Input: "1 + 2 " return "1 + 2 = 3"
Input: "2 * 6" return " 2 * 6 = 12"

Note: your function should support "+, -, *, /". If input string has more than one operator, just return an error message "only support one operator"
"""
def mathEquation(one, two, operator) :
    if operator == "+" :
        return one + two
    elif operator == "-" :
        return one - two
    elif operator == "*" :
        return one * two
    elif operator == "/" :
        return one / two
    else :
        return "What the hecc are you inputing"
operator = raw_input("Operator ")
print(mathEquation(1.1, 2.2, operator))
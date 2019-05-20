#Use recursive function to calculate factorial: https://en.wikipedia.org/wiki/Factorial
#Example: input 1, output 1; input 2, output 2; input 3, output 6...
number = input("Number ")
def factorial(number) :
    if number == 0 :
        return 1
    else :
        anumber = 1
        for x in range(1, number + 1) :
            anumber = anumber * x
        return anumber
print(factorial(number))

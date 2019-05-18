#Write a function to generate Fibonacci numbers https://en.wikipedia.org/wiki/Fibonacci_number#Sequence_properties
#Example, 0, 1, 1, 2, 3, 5, 8...
number = input("Number ")
def fibonacci(number) :
    if number <= 1:
       return number
    else:
       return(fibonacci(number-1) + fibonacci(number-2))
numberb = input("Another one ")
for i in range(numberb):
       print(fibonacci(i))
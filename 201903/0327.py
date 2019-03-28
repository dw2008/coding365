#For a given number, if it can be divided by 3 print "this number {} can be divided by 3 ",
#if it can be divided by 2 print "this number {} can be divided by 2"
#if it can be divided by 2 and 3, print "this number {} can be divided by 2 and 3"
#for rest scenario, just print "number {} "
#Challenge: can you pass in the number from command line instead hard-code it in code? See: https://www.pythonforbeginners.com/argv/more-fun-with-sys-argv


import sys
program_name = sys.argv[0]
number = int(sys.argv[1:][0])

print("number: ", number)

for x in sys.argv:
     print("Argument: ", x)

if (number % 2 == 0) and (number % 3 == 0) :
 print("This number is divisible by both 2 and 3")
elif number % 3 == 0 :
 print("This number is divisible by 3")
elif number % 2 == 0 :
 print("This number is divisible by 2")
else :
 print("This number is not divisible by 2 or 3")
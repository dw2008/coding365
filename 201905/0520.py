#Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

#Example 1:

#Input: "Hello"
#Output: "hello"
#Example 2:

#Input: "here"
#Output: "here"
#Example 3:

#Input: "LOVELY"
#Output: "lovely"
def lowercase(aword) :
    result = ""
    for x in aword :
        result = result + x.lower()
    return result
word = raw_input("Word ")
print(lowercase(word))
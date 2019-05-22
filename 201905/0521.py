#Input: two string
#Output: Common unique characters of these two strings
#Example: "bella" , "else". output: "e", "l"  
def commonChar(aword, bword) :
    result = list()
    for x in aword :
        for y in bword :
            if x == y :
                result.append(x)
    return result
worda = raw_input("Word ")
wordb = raw_input("Another word ")
print(commonChar(worda, wordb))
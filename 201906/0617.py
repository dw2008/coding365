import re
# def madLibs(noun1, noun2, adverb, verb) :
#     print('The', noun1, adverb, verb, 'the', noun2)
#     return " "
# noun1 = raw_input('Noun please ')
# noun2 = raw_input('Another noun please ')
# adverb = raw_input('Adverb plz ')
# verb = raw_input('Verb plox (past tense) ')
# print(madLibs(noun1, noun2, adverb, verb))
def readFile(afile) :
    result = afile.read()
    return result
afile = open('madLibs.txt')
def matchAtoZ(ainput) :
    words = ainput.split()
    result = list()
    for x in words :
        if x.isupper() == True :
            if len(x) > 3 :
                result.append(x)
    return result
def ask(alist) :
    result = list()
    for x in alist :
        print('Please enter a(n) ' + x.lower())
        quest = raw_input()
        result.append(quest)
    return result
def replace(afile) :
    someFile = readFile(afile)
    match = matchAtoZ(someFile)
    index = 0 
    ainput = ask(match)
    ayfile = someFile.split()
    result = str()
    for x in ayfile :
        if index < len(match) and  x == match[index]  :
            result = result + ainput[index] + " "
            index += 1
        else :
            result = result + x + " "
    return result
pain = replace(afile)                
print(pain)
resultFile = open('result.txt', 'a')
resultFile.write(pain)
resultFile.close()
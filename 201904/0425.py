#Implement a function to print out how many of each vowel are present in an input string. 
#Example: 
#Input: "Apple"
#Output: "Total number of As: 1, Total number of Es: 1, Total number of Is: 0, Total Number of Os: 0, Total number of Us: 0"
#Note: upper and lower case should be counted together. 
def findVowel(word) :
    As = 0
    Es = 0
    Is = 0
    Os = 0
    Us = 0
    for x in str(word) :
        if x == "a" or x == "A" :
            As = As + 1
        elif x == "e" or x == "E" :
            Es = Es + 1
        elif x == "i" or x == "I" :
            Is = Is + 1
        elif x == "o" or x == "O" :
            Os = Os + 1
        elif x == "u" or x == "U" :
            Us = Us + 1
    print("As :" , As)
    print("Es :" , Es)
    print("Is :" , Is)
    print("Os :" , Os)
    print("Us :" , Us)
print(findVowel("Shrek"))

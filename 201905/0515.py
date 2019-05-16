#A paragraph of words contains some non-character symbols, can you write a function to clean up them then return the readable paragraph? 
#Example: input - "Tod2ay i2-s S()unday." output: "Today is Sunday."
#Hint: Google "python check if character is letter"
def weedOut(aparagraph) :
    result = ""
    for char in aparagraph:
        if char.isalpha() == True or char == ' ' or char == '.' or char == ',' or char == '!' or char == '?':
            result = result + char
    return result

paragraph = "Th3eref0or3e, I d0o n0ot w4ant t0o d0o th1is."
print(weedOut(paragraph))
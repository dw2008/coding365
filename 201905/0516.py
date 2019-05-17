#Write two functions: one called encrypt which reverse all words in a paragrah, another called decrypt which reverse them back. 
#Example: "I love pizza" -> "I evol azzip" -> "I love pizza"
someWords = raw_input("")
def encrypt(words) :
    return words[::-1]
print(encrypt(someWords))
print(encrypt(encrypt(someWords)))
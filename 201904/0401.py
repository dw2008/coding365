#Given a list of strings {"I", "love", "apple", "I", "don't", "love", "orage"}
#Manually count the appearance of each string in the list
#Ref: https://www.tutorialspoint.com/python/python_dictionary.htm
#Create a dict store the  the count, what is the key and what is the value? 
#Printout String and its count in follow format in seperate lines "I: 2" "apple: 1"
#Can you let computer count it for you? 
listThing = ["I", "love", "apple", "I", "don't", "like", "orange"]
dict = {"I" : 2, "love" : 1, "apple" : 1, "don't" : 1, "like" : 1, "orange" : 1}
print(dict["I"])
# print dict["love"]
# print dict["apple"]
# print dict["don't"]
# print dict["like"]
print(dict)

anotherList = ["Hey", "Hi", "Hey"]

def countList(list) :
	result = {}
	for key in list :
		if key in result :
			result[key] = result[key] + 1
		else :
			result[key] = 1
	return result

newDict = countList(listThing)
print(newDict)
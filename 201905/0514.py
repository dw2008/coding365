#Write a function to take a paragraph of words as input
#Use turtle to printout the whole paragraph and print out how many words in this paragraph. 
import turtle
turt = turtle.Turtle()
paragraph = raw_input("Paragraph ")
turt.penup()
turt.goto(-200, 175)
turt.write(paragraph, font=("Arial", 16, "normal"))
def numberOfWords(aparagraph) :
    result = 0
    bparagraph = aparagraph.split(" ")
    for x in bparagraph :
        result += 1 
    return result
ree = numberOfWords(paragraph)
turt.goto(-200, 140)
turt.write(ree, font=("Arial", 16, "normal"))
win=turtle.Screen()
win.exitonclick()
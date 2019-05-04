#Use turtle to create a riddle game. 
#Predefine several riddles, random print one and ask for answers. 
#Print out result. 
import turtle

turt = turtle.Turtle()

def line(words, horiz_pos = -50):
    x,y = turt.pos()
    turt.goto(max(horiz_pos, -190), y)
    turt.write(words, font=("Arial", 16, "normal"))
    x,y = turt.pos()
    turt.goto(x, y - 25)
turt.penup()
line("I come out of a cold morning's sigh")
line("And your freshly baked pie")
line("I am alive when I die")
line("And can arise from your chai")
aRiddle = raw_input("What's the answer?")
print(aRiddle)
try :
    if aRiddle == "steam" :
        turt.write("Noice", font=("Arial", 16, "normal"))
    else :
        turt.write("No", font=("Arial", 16, "normal"))
except :
    turt.write("What was that")

win=turtle.Screen()
win.exitonclick()


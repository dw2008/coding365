#Add more riddles to your riddle game, ask a random one when game start.
import turtle
import random

turt = turtle.Turtle()

def line(words, horiz_pos = -50):
    x,y = turt.pos()
    turt.goto(max(horiz_pos, -190), y)
    turt.write(words, font=("Arial", 16, "normal"))
    x,y = turt.pos()
    turt.goto(x, y - 25)
turt.penup()
number = random.randint(0, 1)
if number == 0 :
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
elif number == 1 :
    line("An expert weaver")
    line("Yet so small")
    line("So many patterns")
    line("But that's not all")
    aRiddle = raw_input("What's the answer?")
    print(aRiddle)
    try :
        if aRiddle == "spider" :
            turt.write("Noice", font=("Arial", 16, "normal"))
        else :
            turt.write("No", font=("Arial", 16, "normal"))
    except :
        turt.write("What was that")


win=turtle.Screen()
win.exitonclick()

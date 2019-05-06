#Enhance your riddle game: 
#1. Save your riddles in a list so you can generate more riddles
#2. Random select a riddle from the list
#3. Refactor the code with more functions to make is reusable and more readable
import turtle
import random

turt = turtle.Turtle()
alist = ["Yeet", "Yet"]

def line(words, horiz_pos = -50):
    x,y = turt.pos()
    turt.goto(max(horiz_pos, -190), y)
    turt.write(words, font=("Arial", 16, "normal"))
    x,y = turt.pos()
    turt.goto(x, y - 25)

def riddleA() :
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

def riddleB() :
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

turt.penup()
turt.goto(0, 200)
number = random.randint(0, 1)
numberb = alist[number]

if numberb == "Yeet" :
    riddleA()
    turt.goto(0, 0)
    riddleB()

elif numberb == "Yet" :
    riddleB()
    turt.goto(0, 0)
    riddleA()

win=turtle.Screen()
win.exitonclick()
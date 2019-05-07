#Add following new function to your riddle game
#When enter the game, ask player's name first
#After the game, print out player's name and its score.
import turtle
import random

turt = turtle.Turtle()
alist = ["Yeet", "Yet"]
name = raw_input("What's your name? ")
score = 0

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

turt.goto(-200, 100)
turt.write(name, "'s score was :", font=("Arial", 16, "normal"))
turt.goto(-200, 0)
turt.write(score, font=("Arial", 16, "normal"))

win=turtle.Screen()
win.exitonclick()  

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
    aRiddle = raw_input("What's the answer? (Lowercase, please) ")
    print(aRiddle)
    if aRiddle == "steam" :
        score = score + 1
        turt.write("Noice", font=("Arial", 16, "normal"))
    else :
        turt.write("No", font=("Arial", 16, "normal"))
def riddleB() :
    line("An expert weaver")
    line("Yet so small")
    line("So many patterns")
    line("But that's not all")
    aRiddle = raw_input("What's the answer? (Lowercase, please) ")
    print(aRiddle)
    if aRiddle == "spider" :
        turt.write("Noice", font=("Arial", 16, "normal"))
    else :
        turt.write("No", font=("Arial", 16, "normal"))
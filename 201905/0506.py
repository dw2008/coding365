#Add following new function to your riddle game
#When enter the game, ask player's name first
#After the game, print out player's name and its score.
import turtle
import random
turt = turtle.Turtle()

riddles = [
["I come out of a cold morning's sigh", "And your freshly baked pie", "I am alive when I die", "And can arise from your chai"],
["An expert weaver", "Yet so small", "So many patterns", "But that's not all"],
["AAA"]
]


def line(words, horiz_pos = -50) :
    x, y = turt.pos()
    turt.goto(max(horiz_pos, -190), y)
    turt.write(words, font=("Arial", 16, "normal"))
    x, y = turt.pos()
    turt.goto(x, y - 25)
def initScreen() :
    turt.penup()
    turt.goto(0, 200)
def printRiddle(riddle) :
    for x in riddle:
        line(x)
    
initScreen()
printRiddle(riddles[0])
win=turtle.Screen()
win.exitonclick()
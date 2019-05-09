#Generate random riddle
import turtle
import random
turt = turtle.Turtle()

riddles = [
["I come out of a cold morning's sigh", "And your freshly baked pie", "I am alive when I die", "And can arise from your chai"],
["An expert weaver", "Yet so small", "So many patterns", "But that's not all"],
["AAA"]
]
answers = ["steam", "spider", "placeholder"]

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
def genRan(alist) :
    return random.randint(0, len(alist) - 1)
def checkAnswer(answerlist, answer, index) :
    if answerlist[index] == answer :
        return True
    else :
        return False
score = 0
initScreen()
indexa = genRan(riddles)
printRiddle(riddles[indexa])
answer = raw_input("What's the answer? (Use Lowercase) ")
if checkAnswer(answers, answer, indexa) :
    line("Correct")
    score += 1
else :
    line("Incorrect")
print("Your Score: ", score)
win=turtle.Screen()
win.exitonclick()
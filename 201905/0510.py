#Add a new function to your game
#Ask players name before start the game. Random select 5 riddles for the game. 
#After the game, print player's name and score. 
import turtle
import random

turt = turtle.Turtle()
riddles = [
["I come out of a cold morning's sigh", "And your freshly baked pie", "I am alive when I die", "And can arise from your chai"],
["An expert weaver", "Yet so small", "So many patterns", "But that's not all"],
["AAA"],
["1"],
["2"],
["3"],
["4"],
["5"]
]
answers = ["steam", "spider", "placeholder", 1, 2, 3, 4, 5]

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
def askName() :
    name = raw_input("What's your name? ")
    return name
def askAnswer() :
    answer = raw_input("What's the answer?(Lowercase) ")
    return answer
def printScore(name, score) :
    result = name + "'s score was: " + str(score)
    line(result)
def generateProbSet(amin, amax) :
    result = set()
    size = amax - amin
    while size > len(result) :
        result.add(random.randint(amin, amax))
    return result
score = 0
sequence = generateProbSet(0, 5)
initScreen()
name = askName()
indexa = genRan(riddles)
for x in sequence :
    printRiddle(riddles[x])
    answer = askAnswer()
    if checkAnswer(answers, answer, indexa) :
        line("Correct")
        score += 1
    else :
        line("Incorrect")
printScore(name, score)
win=turtle.Screen()
win.exitonclick()
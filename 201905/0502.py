#Finish half of this tutorial https://hourofpython.trinket.io/a-visual-introduction-to-python#/welcome/an-hour-of-code
#Write your own code below
import turtle
turt = turtle.Turtle()
turt.penup()
def line(words, horiz_pos = -50):
    x,y = turt.pos()
    turt.goto(max(horiz_pos, -190), y)
    turt.write(words)
    x,y = turt.pos()
    turt.goto(x, y - 25)
def by(author):
    x,y = turt.pos()
    turt.goto(x + 70, max( -190, y -30))
    turt.write(author)
    x,y = turt.pos()
    turt.goto(0, y)
turt.goto(-50, 0)
line("Dang cilantro sucks")
line("I mean it's not that bad really")
line("I has bad grammers")
by("Daniel Wu")
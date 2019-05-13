#Create a function to draw a ring, take the input as color
import turtle
turt = turtle.Turtle()
color = "green"
def drawRing(acolor) :
    turt.color(acolor)
    turt.pensize(40)
    turt.circle(100)
drawRing(color)
win=turtle.Screen()
win.exitonclick()
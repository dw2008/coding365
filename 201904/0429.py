#https://docs.python.org/3.3/library/turtle.html?highlight=turtle
#https://www.geeksforgeeks.org/turtle-programming-python/
#Write a function to draw a turtle and let it move forward
import turtle
turtle.bgcolor("grey")
turtle.speed(0)
colors = ["red", "blue", "yellow", "green"]
for x in range(360) :
    turtle.pencolor( colors[ x % 4 ])
    turtle.circle(x)
    turtle.left(90)
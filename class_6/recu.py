# In order to run this code, please copy the it in the following link:
# https://repl.it/languages/python_turtle

import turtle

myTurtle = turtle.Turtle()
myTurtle.speed(9)
myWin = turtle.Screen()
colors = (
        '#006699',
        '#006666',
        '#660066',
        '#990000',
        '#ad3270',
        '#e65100'
    )

def draw(myTurtle, length):
    if length > 0:
        myTurtle.forward(length)
        myTurtle.left(120)
        draw(myTurtle, length-2)

for color in colors:
    myTurtle.pencolor(color)
    myTurtle.left(60)
    draw(myTurtle, 150)

myWin.exitonclick()
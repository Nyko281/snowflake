import turtle
import random

snow = turtle.Turtle()
colours = ["cyan","magenta","white","blue"]
colours2 = ["grey", "purple"]

turtle.Screen().bgcolor(random.choice(colours2))

def branch():
    a = 0
    while a < 3:
        b = 0
        while b < 3:
            snow.forward(30)
            snow.backward(30)
            snow.right(45)
            b += 1
        snow.left(90)
        snow.backward(30)
        snow.left(45)
        a += 1
    snow.right(90)
    snow.forward(90)
 
c = 0 
while c < 4:
    snow.penup()
    snow.goto( random.randint(-250,250), random.randint(-250,250) )
    snow.forward(90)
    snow.left(45)
    snow.pendown()
    snow.color(random.choice(colours))
    c += 1
    d = 0
    while d < 8:
        branch()
        snow.left(45)
        d += 1
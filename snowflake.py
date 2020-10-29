import turtle
import random

snow = turtle.Turtle()
colours = ["cyan","magenta","white","blue"]
colours2 = ["grey", "purple"]

turtle.Screen().bgcolor(random.choice(colours2))

def branch():
    for i in range(3):
        for i in range(3):
            snow.forward(30)
            snow.backward(30)
            snow.right(45)
        snow.left(90)
        snow.backward(30)
        snow.left(45)
    snow.right(90)
    snow.forward(90)
    
for i in range(4):
    snow.penup()
    snow.goto( random.randint(-100,100), random.randint(-100,100) )
    snow.forward(90)
    snow.left(45)
    snow.pendown()
    snow.color(random.choice(colours))
    for i in range(8):
        branch()
        snow.left(45)
    

    
    
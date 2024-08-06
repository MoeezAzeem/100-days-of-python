from turtle import Turtle, Screen, colormode
import random

def randomise_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r, g, b)

colormode(255)

direction = [0, 90, 180, 270]
tim = Turtle()

tim.width(15)
tim.speed("fastest")

for _ in range(200):
    tim.color((randomise_color()))
    tim.forward(30)
    tim.right(random.choice(direction))

screen = Screen()
screen.exitonclick()

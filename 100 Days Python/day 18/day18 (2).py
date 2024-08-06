from turtle import Turtle, Screen, colormode
import random

tim = Turtle()
colormode(255)

def randomise_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r, g, b)

tim.width(4)
tim.speed("fastest")

def draw_spirograph(size):
    for _ in range(int(360 / size)):
        tim.color((randomise_color()))
        tim.circle(100)
        tim.setheading(tim.heading() + size)

draw_spirograph(10)

screen = Screen()
screen.exitonclick()
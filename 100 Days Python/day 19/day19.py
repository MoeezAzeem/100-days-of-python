from turtle import Turtle, Screen
import random

# Function to create a turtle
def create_turtle(color, y_position):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color)
    new_turtle.goto(x=-230, y=y_position)
    return new_turtle

def create_racetrack():
    for y in y_axis:
        track_line = Turtle()
        track_line.penup()
        track_line.goto(-240, y + 20)
        track_line.pendown()
        track_line.goto(250, y + 20)
        track_line.hideturtle()

def create_starting_line():
    start_line = Turtle()
    start_line.penup()
    start_line.goto(-230, 200)
    start_line.right(90)
    start_line.pendown()
    start_line.pensize(3)
    start_line.forward(400)
    start_line.hideturtle()

def create_finish_line():
    finish_line = Turtle()
    finish_line.penup()
    finish_line.goto(230, 200)
    finish_line.right(90)
    finish_line.pendown()
    finish_line.pensize(3)
    finish_line.forward(400)
    finish_line.hideturtle()
    
    for i in range(-240, 240, 40):
        checker = Turtle()
        checker.shape("square")
        checker.shapesize(stretch_wid=2, stretch_len=2)
        checker.penup()
        checker.goto(230, i)
        checker.color("black" if (i // 40) % 2 == 0 else "white")

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
screen.title("Turtle Race")

user_bet = screen.textinput(title="Make your bet", prompt="Which color turtle will win the race? Choose from the rainbow colors (red, orange, yellow, green, blue, purple): ").lower()

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
if user_bet not in colors:
    print("Invalid color. Please restart and enter a valid color.")
    screen.bye()
else:
    y_axis = [-140, -100, -60, -20, 20, 60, 100]
    all_turtles = []

    create_racetrack()
    create_starting_line()
    create_finish_line()

    for turtle_number in range(6):
        new_turtle = create_turtle(colors[turtle_number], y_axis[turtle_number + 1])
        all_turtles.append(new_turtle)

    if user_bet:
        is_race_on = True

    while is_race_on:
        for turtle in all_turtles:
            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)
            if turtle.xcor() > 230:
                is_race_on = False
                winning_color = turtle.pencolor()
                winners = [turtle.pencolor() for turtle in all_turtles if turtle.xcor() > 230]

                if len(winners) > 1:
                    print(f"It's a draw! The winning turtles are: {', '.join(winners)}")
                elif winning_color == user_bet:
                    print(f"You've won! The {winning_color} turtle is the winner!")
                else:
                    print(f"You've lost! The {winning_color} turtle is the winner!")

screen.exitonclick()

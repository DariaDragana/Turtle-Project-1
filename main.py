from turtle import Turtle, Screen
import random

screen = Screen()
# tim.pendown()
# def move_forwards():
#     tim.forward(10)
#
# def move_backwards():
#     tim.backward(10)
#
# def turn_clockwise():
#     tim.right(10)
#
# def turn_counterclockwise():
#     tim.left(10)
#
# def clear_screen():
#     tim.reset()
#
# screen.listen()
# screen.onkey(key="w", fun=move_forwards)
# screen.onkey(key="s", fun=move_backwards)
# screen.onkey(key="a", fun=turn_counterclockwise)
# screen.onkey(key="d", fun=turn_clockwise)
# screen.onkey(key="c", fun=clear_screen)

is_race_on = False
screen.setup(500, 400)
user_bet = screen.textinput("Make your bet.", "Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-230, y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost. The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()

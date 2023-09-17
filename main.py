import random
import turtle
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)

game_is_on = False

user_guess = turtle.textinput("Guess", "Guess!!Who will win, Pick a colour out of "
                                       "('violet', 'blue', 'green', 'yellow', 'orange', 'red') ")

color_list = ['violet', "blue", "green", "yellow", "orange", "red"]
y_positions = [-100, -50, 0, 50, 100, 150]

all_turtles = []

for i in range(6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(color_list[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[i])
    all_turtles.append(new_turtle)


def check_turtle_winner(turtle_obj):
    if turtle_obj.xcor() > 230:
        return True
    else:
        return False


if user_guess:
    game_is_on = True

while game_is_on:

    for turtle in all_turtles:
        if check_turtle_winner(turtle):
            game_is_on = False
            break
    if game_is_on:
        for turtle in all_turtles:
            random_dist = random.randint(0, 10)
            turtle.forward(random_dist)
            if turtle.xcor() > 230:
                if user_guess == turtle.pencolor():
                    print(f"You guessed it right!!, Winner is {user_guess} turtle!!")
                else:
                    print(f"You guessed it wrong!!, Winner is {turtle.pencolor()} turtle!!")
                game_is_on = False
                break

screen.exitonclick()

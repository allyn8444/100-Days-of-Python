from turtle import Turtle, Screen
import random
tim = Turtle()
screen = Screen()

screen.listen()  # will listen to onscreen events


# ===== Etch-A-Sketch App ==== #
# W = Forward
# S = Backward
# D = Clockwise
# A = Counter-Clockwise

# def forward():
#     tim.forward(10)
#
# def backward():
#     tim.back(10)
#
# def clockwise():
#     tim.right(10)
#
# def counter_clockwise():
#     tim.left(10)
#
# def clear_screen():  # clears screen and back to starting point
#     tim.clear()
#     tim.penup()  # so that it won't write anything going back to the starting point
#     tim.home()
#     tim.pendown()
#
# screen.onkey(clear_screen, "c")
# screen.onkey(forward, "w")
# screen.onkey(backward, "s")
# screen.onkey(clockwise, "d")
# screen.onkey(counter_clockwise, "a")


# ===== TURTLE RACE ====== #

raceOn = False
screen.setup(600, 400)  # set width and height of screen
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color")
print(user_bet)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

turtles_list = []
yaxis = -150
for index in range(6):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    # starting point (left side)
    new_turtle.penup()  # we don't need to write
    new_turtle.color(colors[index])
    new_turtle.goto(-290, yaxis)
    yaxis += 50
    turtles_list.append(new_turtle)


print(turtles_list)

if user_bet:  # if user_bet is not empty
    raceOn = True

while raceOn:
    for turtle in turtles_list:
        if turtle.xcor() > 290:  # checks if a turtle reached 290 x coordinate (WIN)
            raceOn = False  # Stop loop cuz a turtle already won
            winner = turtle.pencolor()  # get pencolor of winner turtle

            if winner == user_bet:
                print(f"You won! The {winner} turtle is the winner!")
            else:
                print(f"You lost... The {winner} turtle is the winner!")
        else:
            speed = random.randint(0, 10)
            turtle.forward(speed)







screen.exitonclick()

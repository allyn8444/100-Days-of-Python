from turtle import Turtle, Screen

# this works line by line
timmy = Turtle()
timmy.shape("turtle")
timmy.color("blue")
timmy.forward(100)
timmy.color("green")
timmy.forward(100)

my_screen = Screen()
my_screen.exitonclick()  # only exits the turtle screen when exit button is clicked

from turtle import Turtle, Screen
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        # Creation of the food
        self.shape("circle")
        self.color("coral")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.speed("fastest")
        self.spawn()

    # Randomly position food
    def spawn(self):
        x_axis = random.randint(-275, 275)
        y_axis = random.randint(-275, 250)  # only 250 up because we have the Scoreboard
        self.goto(x_axis, y_axis)






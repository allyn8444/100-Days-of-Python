from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.color("white")
        self.penup()

        self.y_move = 10
        self.x_move = 10
        self.speed = 0.1

    def move(self):
        xcor = self.xcor() + self.x_move
        ycor = self.ycor() + self.y_move
        self.goto(xcor, ycor)
        # print(self.ycor())

    # Bounce, changing its Y coordinate (move opposite along the vertical)
    def bounce_y(self):
        self.y_move *= -1  # the bounce formula
        self.speed *= 0.9  # increase BALL speed every time ball hits a Paddle

    # Bounce, change its X coordinate (move opposite direction, horizontal)
    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.speed = 0.1  # reset Ball speed after scoring

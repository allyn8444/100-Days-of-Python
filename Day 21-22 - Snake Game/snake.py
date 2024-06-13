from turtle import Turtle
SPEED = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake_body = []

    def start(self):
        x_axis = 0
        for i in range(3):
            new_body = Turtle()
            new_body.penup()
            new_body.shape("square")
            new_body.color("dark green")
            self.snake_body.append(new_body)
            self.snake_body[0].color("forest green")
            new_body.goto(x_axis, 0)
            x_axis -= 20

    # MOVE METHOD
    def move(self):
        # Iterate through the snake body parts from the end to the beginning (excluding the head)
        for body_part in range(len(self.snake_body) - 1, 0, -1):
            # Get the x and y coordinates of the previous body part
            new_x = self.snake_body[body_part - 1].xcor()
            new_y = self.snake_body[body_part - 1].ycor()

            # Move the current body part to the position of the previous body part
            self.snake_body[body_part].goto(new_x, new_y)

        # Move the head forward
        self.snake_body[0].forward(SPEED)


    def up(self):
        if self.snake_body[0].heading() != DOWN:  # Denying UP movement if Head is currently heading DOWN
            self.snake_body[0].setheading(UP)

    def down(self):
        if self.snake_body[0].heading() != UP:  # Denying DOWN movement if Head is currently heading UP
            self.snake_body[0].setheading(DOWN)

    def left(self):
        if self.snake_body[0].heading() != RIGHT:  # Denying LEFT movement if Head is currently heading RIGHT
            self.snake_body[0].setheading(LEFT)

    def right(self):
        if self.snake_body[0].heading() != LEFT:   # Denying RIGHT movement if Head is currently heading LEFT
            self.snake_body[0].setheading(RIGHT)


    def increase_size(self):
        add_body = Turtle()
        add_body.penup()
        add_body.shape("square")
        add_body.color("dark green")
        # Make sure to spawn New body part to the coordinate of the Tail (the very end)
        tail_xcor = self.snake_body[len(self.snake_body) - 1].xcor()
        tail_ycor = self.snake_body[len(self.snake_body) - 1].ycor()
        add_body.goto(tail_xcor, tail_ycor)
        # Finally, add the new body to the snake body
        self.snake_body.append(add_body)








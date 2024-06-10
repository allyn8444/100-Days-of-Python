from turtle import Screen
import time
from snake import Snake

MOVEMENT_DELAY = 0.1
screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.listen()  # Listen for key presses

screen.tracer(0)  # Set off delay in animation of turtle

screen.title("Snake Game")

snake = Snake()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


gameIsOn = True
while gameIsOn:
    # Screen updates on what to show. so that snake will move as a whole
    #   and not per body part
    screen.update()
    time.sleep(MOVEMENT_DELAY)  # Delay on movement

    snake.move()


screen.exitonclick()

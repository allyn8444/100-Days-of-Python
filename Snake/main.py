from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

MOVEMENT_DELAY = 0.1
screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.listen()  # Listen for key presses

screen.tracer(0)  # Set off delay in animation of turtle

screen.title("Snake Game")

snake = Snake()
snake.start()
food = Food()
scoreboard = Scoreboard()


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

    # === Detect collision with food === #
    SNAKE_HEAD = snake.snake_body[0]
    if SNAKE_HEAD.distance(food) < 15:  # check if snake head collided with food
        print("eat nom nom")
        food.spawn()  # spawn another food in new loc
        snake.increase_size()
        scoreboard.add_score()

    # === Detect collision with wall === #
    x_cor = SNAKE_HEAD.xcor()
    y_cor = SNAKE_HEAD.ycor()

    # These return boolean values:
    collided_x = x_cor > 290 or x_cor < -290  # checks if snake head collided in the X-axis screen edge
    collided_y = y_cor > 290 or y_cor < -290  # checks if snake head collided in the Y-axis screen edge

    if collided_x or collided_y:
        gameIsOn = False
        print("Game over")
        scoreboard.game_over()

    # === Detect collision with Tail === #
    for body_part in snake.snake_body[1:]:  # sliced, start from the body only (Head is not included)
        if SNAKE_HEAD.distance(body_part) < 10:  # checks if snake head is colliding with any body part
            print("bumped")
            gameIsOn = False
            scoreboard.game_over()




screen.exitonclick()

from turtle import Screen
from paddle import Paddle
from ball import Ball
import time  # for delay
from scoreboard import Scoreboard


SCORE_GOAL = 10
print(f"Score goal is currently: {SCORE_GOAL}")

# === Setup Screen === #
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


paddle_r = Paddle(350, 0)  # paddle on the left
paddle_l = Paddle(-350, 0)   # paddle on the right


# Listen on Key Presses
screen.listen()

# === PLAYER 1 CONTROLS === #
screen.onkey(paddle_r.go_up, "Up")
screen.onkey(paddle_r.go_down, "Down")


# === PLAYER 2 CONTROLS === #
screen.onkey(paddle_l.go_up, "w")
screen.onkey(paddle_l.go_down, "s")


ball = Ball()

p1_score = Scoreboard(-280, 260, "allyn")
p2_score = Scoreboard(280, 260, "ashley")


gameOn = True

while gameOn:
    time.sleep(ball.speed)  # put delay on ball movement
    screen.update()
    ball.move()

    # Detect collision with Top or Bottom Screen
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with Right Paddle
    collide_r = ball.distance(paddle_r) < 50 and ball.xcor() > 330
    collide_l = ball.distance(paddle_l) < 50 and ball.xcor() < -330
    if collide_l or collide_r:
        # print("collide")
        ball.bounce_x()

    # ==== SCORE === #
    if ball.xcor() > 390:
        # print("p1 score")
        p1_score.add_score()
        ball.reset_position()
        ball.move()
    elif ball.xcor() < -390:
        p2_score.add_score()
        ball.reset_position()
        ball.move()

    # winner
    if p1_score.score == SCORE_GOAL:
        p1_score.winner()
        gameOn = False
    elif p2_score.score == SCORE_GOAL:
        p2_score.winner()
        gameOn = False




screen.exitonclick()

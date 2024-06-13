from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.score = 0
        self.hideturtle()  # hide the arrow
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.write(f"Score: {self.score}", False, "center", ('Arial', 15, 'normal'))


    def add_score(self):
        self.score += 1
        self.clear()  # so that it will update 'score' everytime a player scored
        self.write(f"Score: {self.score}", False, "center", ('Arial', 15, 'normal'))


    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write("GAME OVER", False, "center", ('Arial', 30, 'normal'))

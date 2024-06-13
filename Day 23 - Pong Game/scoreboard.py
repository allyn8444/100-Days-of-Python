from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, x, y, player_name):
        super().__init__()

        self.score = 0
        self.player = player_name
        self.hideturtle()  # hide the arrow
        self.penup()
        self.color("white")
        self.goto(x, y)
        self.write(f"{self.player}: {self.score}", False, "center", ('Arial', 15, 'normal'))


    def add_score(self):
        self.score += 1
        self.clear()  # so that it will update 'score' everytime a player scored
        self.write(f"{self.player}: {self.score}", False, "center", ('Arial', 15, 'normal'))

    # Game Winner Screen
    def winner(self):
        self.goto(0, 0)
        self.color("green")
        self.write(f"{self.player} won!", False, "center", ('Arial', 30, 'normal'))
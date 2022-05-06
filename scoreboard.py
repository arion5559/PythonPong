from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()

    def update_score(self, player_1, player_2):
        self.clear()
        self.goto(-100, 200)
        self.write(player_1.score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(player_2.score, align="center", font=("Courier", 80, "normal"))

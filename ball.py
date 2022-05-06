from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.x_cor = 10
        self.y_cor = 10
        self.move_speed = 0.1

    def move(self):
        x = self.xcor() + self.x_cor
        y = self.ycor() + self.y_cor
        self.goto(x, y)

    def bounce(self):
        self.y_cor *= -1

    def paddle_bounce(self):
        self.x_cor *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.paddle_bounce()
        self.move_speed = 0.1

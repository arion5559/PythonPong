from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position_x=0):
        super().__init__()
        self.segments = []
        self.construct_paddle(position_x)
        self.score = 0

    def construct_paddle(self, x):
        y = -40
        for _ in range(5):
            new_segment = Turtle()
            new_segment.shape("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(x=x, y=y)
            y += 20
            self.segments.append(new_segment)

    # def construct_paddle(self, x):
    #     self.shape("square")
    #     self.color("white")
    #     self.shapesize(stretch_wid=5, stretch_len=1)
    #     self.penup()
    #     self.goto(x=x, y=0)

    def move_up(self):
        if self.segments[-1].ycor() < 290:
            for segment in self.segments:
                segment.goto(x=segment.xcor(), y=segment.ycor() + 10)

    def move_down(self):
        if self.segments[0].ycor() > -290:
            for segment in self.segments:
                segment.goto(x=segment.xcor(), y=segment.ycor() - 10)

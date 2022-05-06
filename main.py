import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


def detect_paddle_collision(ball, paddle1, paddle2):
    collided = False
    for i in range(len(paddle1.segments)):
        if ball.xcor() > 320 and ball.distance(paddle2.segments[i]) < 25:
            collided = True
        if ball.xcor() < -320 and ball.distance(paddle1.segments[i]) < 25:
            collided = True
    return collided


screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()

game_is_on = True

player_1 = Paddle(-350)
player_2 = Paddle(350)
ball = Ball()
scoreboard = Scoreboard()


while game_is_on:
    scoreboard.update_score(player_1, player_2)
    screen.onkeypress(fun=player_1.move_up, key="w")
    screen.onkeypress(fun=player_1.move_down, key="s")
    screen.onkeypress(fun=player_2.move_up, key="Up")
    screen.onkeypress(fun=player_2.move_down, key="Down")
    time.sleep(ball.move_speed)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    if detect_paddle_collision(ball, player_1, player_2):
        ball.paddle_bounce()
    if ball.xcor() > 380:
        ball.reset_position()
        player_1.score += 1
    if ball.xcor() < -380:
        ball.reset_position()
        player_2.score += 1
    screen.update()

screen.exitonclick()

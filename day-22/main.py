from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

screen.listen()
score = Score()

p1 = Paddle(350)
screen.onkey(p1.up, "Up")
screen.onkey(p1.down, "Down")

p2 = Paddle(-350)
screen.onkey(p2.up, "w")
screen.onkey(p2.down, "s")

ball = Ball()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() == 280 or ball.ycor() == -280:
        ball.detect_collision("wall")

    if ball.distance(p1) < 50 and ball.xcor() > 320 or ball.distance(p2) < 50 and ball.xcor() < -320:
        ball.detect_collision("paddle")

    if ball.xcor() > 380:
        ball.reset_game()
        score.l_point()

    if ball.xcor() < -380:
        ball.reset_game()
        score.r_point()

screen.exitonclick()
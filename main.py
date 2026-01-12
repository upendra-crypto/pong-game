from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time
import winsound
screen = Screen()
screen.title("PONG GAME")
screen.setup(800, 600)
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = ScoreBoard(screen)

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.xcor() > 320 and ball.distance(r_paddle) < 50:
        ball.bounce_x()
        winsound.Beep(1000,100)
    if ball.xcor() < -320 and ball.distance(l_paddle) < 50:
        ball.bounce_x()
        winsound.Beep(1000, 100)
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

    if scoreboard.l_score >= scoreboard.limit:
        game_is_on = False
        scoreboard.game_over("LEFT PLAYER")

    if scoreboard.r_score >= scoreboard.limit:
        game_is_on = False
        scoreboard.game_over("RIGHT PLAYER")

screen.exitonclick()

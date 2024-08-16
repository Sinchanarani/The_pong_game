from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(800, 600)
screen.title("Pong")
screen.bgcolor("black")
screen.tracer(0)


left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
ball = Ball()
score=Scoreboard()


screen.listen()
screen.onkey(right_paddle.go_up_r, "Up")
screen.onkey(right_paddle.go_down_r, "Down")
screen.onkey(left_paddle.go_up_l, "w")
screen.onkey(left_paddle.go_down_l, "s")

game_is_on=True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()
    # Detecting collision with wall
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()

    # Detecting collision with right paddle
    if ball.distance(right_paddle)<50 and ball.xcor() > 320 or ball.distance(left_paddle) <50 and ball.xcor() < -320:
        ball.bounce_x()

    # Resetting the position of the ball(right)
    if ball.xcor()>380:
        ball.reset_position()
        score.l_point()
    # Resetting the position of the ball(left)
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

screen.exitonclick()

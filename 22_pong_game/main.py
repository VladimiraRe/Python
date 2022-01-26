import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-360, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(fun=r_paddle.up, key="Up")
screen.onkey(fun=r_paddle.down, key="Down")
screen.onkey(fun=l_paddle.up, key="w")
screen.onkey(fun=l_paddle.down, key="s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Столкновение со стеной
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Столкновение с ракеткой
    if ball.xcor() > 320 and ball.distance(r_paddle) < 50\
            or ball.xcor() < -320 and ball.distance(l_paddle) < 50:
        ball.bounce_x()

    # Если мяч пропускает правая ракетка
    if ball.xcor() > 400:
        scoreboard.l_point()
        ball.reset_position()

    # Если мяч пропускает левая ракетка
    if ball.xcor() < -400:
        scoreboard.r_point()
        ball.reset_position()

screen.exitonclick()

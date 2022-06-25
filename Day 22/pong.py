from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


def setup_screen():
    screen = Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor('black')
    screen.tracer(0)
    draw_line()
    return screen


def draw_line():
    line = Turtle()
    line.pu()
    line.setheading(90)
    line.goto(0, -300)
    line.pd()
    line.color('white')
    line.hideturtle()
    for _ in range(-300, 300, 10):
        line.forward(10)
        line.pen(pendown=not line.isdown())


if __name__ == '__main__':
    screen = setup_screen()

    player = Paddle(-350)
    opponent = Paddle(350)
    ball = Ball()
    player_score = Scoreboard(-50)
    opponent_score = Scoreboard(50)
    screen.listen()
    screen.onkeypress(key='w', fun=player.move_up)
    screen.onkeypress(key='s', fun=player.move_down)

    is_running = True

    while is_running:
        screen.update()
        func = opponent.decide_move_dir(ball)
        if func:
            func()
        ball.move()
        if ball.xcor() > 380:
            opponent_score.increase_score()
            ball.reset()
        elif ball.xcor() < -380:
            player_score.increase_score()
            ball.reset()

        if (ball.distance(opponent) < 50 or ball.distance(player) < 50) and abs(ball.xcor()) > 330:
            ball.bounce_x()

        if abs(ball.ycor()) > 280:
            ball.bounce_y()

    screen.exitonclick()

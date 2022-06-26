from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


def setup_screen():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor('black')
    screen.title('Snake')
    screen.tracer(0)
    return screen


if __name__ == '__main__':

    screen = setup_screen()
    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()
    screen.listen()
    screen.onkeypress(key='Up', fun=snake.up)
    screen.onkeypress(key='Down', fun=snake.down)
    screen.onkeypress(key='Left', fun=snake.left)
    screen.onkeypress(key='Right', fun=snake.right)

    is_running = True
    while is_running:
        screen.update()
        time.sleep(0.1)
        snake.move()

        if snake.head.distance(food) < 15:
            scoreboard.increase_score()
            food.refresh()
            snake.grow()

        has_wall = True
        if has_wall and abs(snake.head.xcor()) > 300 or abs(snake.head.ycor()) > 300:
            #is_running = False
            scoreboard.reset()
            snake.reset()

        for segment in snake.segments:
            if snake.head.distance(segment) < 10:
                #is_running = False
                scoreboard.reset()
                snake.reset()

    screen.exitonclick()

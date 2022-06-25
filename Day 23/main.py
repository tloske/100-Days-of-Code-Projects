import time
from turtle import Screen, delay
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


def setup_screen():
    screen = Screen()
    screen.setup(width=800, height=600)
    screen.colormode(255)
    screen.tracer(0)

    return screen


if __name__ == '__main__':
    screen = setup_screen()
    player = Player()
    car_manager = CarManager(10)
    scoreboard = Scoreboard()
    screen.listen()
    screen.onkeypress(key='w', fun=player.move)

    delay = 0.1
    is_running = True
    while is_running:
        time.sleep(delay)
        screen.update()
        car_manager.move_cars()
        if car_manager.check_collision(player):
            is_running = False
            scoreboard.game_over()

        if player.ycor() >= 280:
            player.reset()
            scoreboard.increase_score()
            car_manager.add_car()
            delay *= 0.9

    screen.exitonclick()

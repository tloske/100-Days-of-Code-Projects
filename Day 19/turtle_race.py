from turtle import Turtle, Screen
from random import randint


def rand_color(t):
    t.color(randint(0, 255), randint(0, 255), randint(0, 255))


def create_turtles(num_turtles):
    return [Turtle() for _ in range(num_turtles)]


def setup_race(turtle_list):
    spacing = 400/len(turtle_list)
    ycord = spacing
    for t in turtle_list:
        rand_color(t)
        t.pu()
        t. goto(-230, -ycord+220)
        ycord += spacing
        t.pd()


def move_turtle(t):
    t.forward(randint(0, 11))


def run_race(turtle_list):
    while True:
        index = 1
        for t in turtle_list:
            move_turtle(t)
            if t.xcor() >= 230:
                return index
            index += 1


def main():
    screen = Screen()
    screen.setup(width=500, height=400)
    screen.colormode(255)
    num_turtles = 10
    user_bet = screen.textinput(title='Make your bet',
                                prompt=f'Which turtle will win the race? Enter a number between 1 and {num_turtles} :')

    turtle_list = create_turtles(num_turtles)
    setup_race(turtle_list)
    winner = run_race(turtle_list)
    if winner == int(user_bet):
        print(f"Yo have won! The winner is turtle number {winner}")
    else:
        print(f"You have lost! The winner is turtle number {winner}")
    screen.exitonclick()


if __name__ == '__main__':
    main()

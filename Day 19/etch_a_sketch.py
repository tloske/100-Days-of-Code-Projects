from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.back(10)


def rotate_right():
    tim.right(10)


def rotate_left():
    tim.left(10)


def clear():
    tim.clear()
    tim.pu()
    tim.home()
    tim.pd()

screen.listen()
screen.onkeypress(key='w', fun=move_forwards)
screen.onkeypress(key='s', fun=move_backwards)
screen.onkeypress(key='a', fun=rotate_left)
screen.onkeypress(key='d', fun=rotate_right)
screen.onkey(key='c', fun=clear)
screen.exitonclick()

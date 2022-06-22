from turtle import Turtle, Screen
from random import choice, randint
import colorgram


def rand_color(t):
    t.color(randint(0, 255), randint(0, 255), randint(0, 255))


def challenge2(t):
    """Draws a dotted line"""
    t = Turtle()
    for _ in range(30):
        t.forward(10)
        t.pen(pendown=not t.isdown())


def draw_shape(num_sides, turtle):
    angle = 360/num_sides
    for _ in range(num_sides):
        turtle.left(360/num_sides)
        turtle.forward(100)


def challenge3(t):
    """Draws multpile shapes with increasing number of sides"""
    max_num_sides = 10
    for num_sides in range(3, max_num_sides):
        rand_color(t)
        draw_shape(num_sides, t)


def draw_walk(t):
    direction_list = [0, 90, 180, 270]
    t.setheading(choice(direction_list))
    t.forward(50)


def challenge4(t):
    """Lets the turtle walk randomly north,west,south,east"""
    t.pensize(10)
    for _ in range(1000):
        rand_color(t)
        draw_walk(t)


def draw_circles(t, size_of_gap):
    for i in range(0, 360, size_of_gap):
        rand_color(t)
        t.setheading(i)
        t.circle(50)


def challenge5(t):
    """Rotates the turtle by 360 degress and draws a circle after each step"""
    draw_circles(t, 5)


rgb_colors = []


def extract_colors(num_colors):
    colors = colorgram.extract('image.jpg', num_colors)
    global rgb_colors
    rgb_colors = [(x.rgb.r, x.rgb.g, x.rgb.b) for x in colors]


def move_turtle(t, spacing):
    t.forward(spacing)


def draw_dot(t, dot_size):
    t.dot(dot_size, choice(rgb_colors))


def hirst_painting(t, dots_per_row, num_rows, dot_size, num_colors):
    """Extracts colors form the given image to create a hirst painting"""
    t.pu()
    t.setheading(225)
    t.forward(300)
    t.setheading(0)
    extract_colors(num_colors)
    for _ in range(num_rows):
        for _ in range(dots_per_row):
            draw_dot(t, dot_size)
            move_turtle(t, dot_size*2)
        t.setheading(180)
        move_turtle(t, dot_size*dots_per_row*2)
        t.setheading(90)
        move_turtle(t, dot_size*2)
        t.setheading(0)


def main():
    tim = Turtle()
    tim.speed('fastest')
    # tim.hideturtle()
    # challenge2(tim)
    # challenge3(tim)
    # challenge4(tim)
    # challenge5(tim)
    hirst_painting(tim, 10, 10, 20, 10)


if __name__ == '__main__':
    screen = Screen()
    screen.colormode(255)
    main()
    screen.exitonclick()

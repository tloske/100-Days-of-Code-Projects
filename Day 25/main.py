from operator import contains
import pandas
from turtle import Turtle, Screen

"""Counts the different colored squirrels"""
#data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
#data['Primary Fur Color'].value_counts().to_csv('squirrel_count.csv')


def setup_screen():
    screen = Screen()
    screen.bgpic('blank_states_img.gif')

    return screen


def get_data():
    return pandas.read_csv('50_states.csv')


def create_turtle(state):
    t = Turtle()
    t.speed('fastest')
    t.hideturtle()
    t.pu()
    t.goto(int(state.x), int(state.y))
    t.write(arg=f'{state.state.item()}', align='left',
            font=("Arial", 12, "normal"))


def check_answer(states, answer):
    if answer in states:
        return True
    return False


if __name__ == '__main__':
    data = get_data()
    states = data.state.to_list()
    screen = setup_screen()
    guessed_states = []
    while len(guessed_states) < len(states):

        answer = screen.textinput(title=f"{len(guessed_states)}/{len(states)} States guessed",
                                  prompt=f"Type in the name of a state located in the USA.").title()

        if answer == 'Exit':
            missing_states = [
                state for state in states if state not in guessed_states]
            new_data = pandas.DataFrame(missing_states)
            new_data.to_csv('states_to_learn.csv')
            break
        elif check_answer(states, answer):
            create_turtle(data[data.state == answer])
            guessed_states.append(answer)

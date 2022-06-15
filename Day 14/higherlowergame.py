from art import logo, vs
from game_data import data
import random
from os import system

score = 0


def get_data() -> dict:
    return random.choice(data)


def format_data(data: dict):
    return f"{data['name']}, a {data['description']}, from {data['country']}."


def increase_score() -> None:
    global score
    score += 1
    print(f"You're right! Current score: {score}.")


def higher_lower_game():
    print(logo)
    is_running = True
    while is_running:
        data_a = get_data()
        data_b = get_data()
        while data_a == data_b:
            data_b = get_data()
        print(f"Compare A: {format_data(data_a)}")
        print(vs)
        print(f"Compare B: {format_data(data_b)}")
        choice = input("Who has more followers? Type 'A' or 'B': ")
        system("cls")
        print(logo)
        match choice:
            case 'A' if data_a['follower_count'] > data_b['follower_count']:
                increase_score()
            case 'B' if data_a['follower_count'] < data_b['follower_count']:
                increase_score()
            case _:
                is_running = False
    print(f"Sorry, that's wrong. Final score {score}")


if __name__ == "__main__":
    higher_lower_game()

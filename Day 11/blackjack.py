import random
from art import logo
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    return random.choice(cards)


def calculate_score(card_list):
    if sum(card_list) == 21 and len(card_list) == 2:
        return 0
    score = sum(card_list)
    if score > 21 and 11 in card_list:
        card_list.remove(11)
        card_list.append(1)
        score = calculate_score(card_list)
    return score


def compare(player_score, computer_score):
    return player_score >= computer_score or player_score == 0


def hit(cards_dict):
    cards_dict['cards'].append(deal_card())
    cards_dict["value"] = calculate_score(cards_dict['cards'])


def blackjack():
    print(logo)
    is_running = True
    player_cards = {'value': 0, 'cards': [deal_card(), deal_card()]}
    computer_cards = {'value': 0, 'cards': [deal_card(), deal_card()]}

    player_cards["value"] = calculate_score(player_cards["cards"])
    computer_cards["value"] = calculate_score(computer_cards["cards"])
    if player_cards["value"] == 0 or computer_cards["value"] == 0:
        is_running = False

    while is_running:
        print(
            f"Your cards: {player_cards['cards']}, current score {player_cards['value']}")
        print(
            f"Computer's cards: {computer_cards['cards']},  current score {computer_cards['value']}")
        choice = input(
            "Type 'y' to get another cards, type anything else to pass: ")

        match choice:
            case 'y':
                hit(player_cards)
                if player_cards['value'] > 21:
                    is_running = False
                    break
            case _:
                while computer_cards['value'] < 17 and computer_cards['value'] != 0:
                    if compare(computer_cards['value'], player_cards['value']):
                        break
                    hit(computer_cards)
                is_running = False

    print(
        f"Your final hand: {player_cards['cards']}, score {player_cards['value']}")
    print(
        f"Computer's final hand: {computer_cards['cards']}, score {computer_cards['value']}")

    player_score = player_cards['value']
    computer_score = computer_cards['value']
    if player_score > 21:
        print("You lost")
    elif computer_score > 21:
        print("You won")
    elif compare(player_score, computer_score):
        print("You won")
    else:
        print("You lost")

    choice = input("Play again?: 'yes' or 'no'")
    if choice == 'yes':
        os.system('cls')
        blackjack()


if __name__ == "__main__":
    blackjack()

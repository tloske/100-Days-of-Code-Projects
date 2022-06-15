MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

coins = {'quarters': 0.25, 'dimes': 0.1, 'nickles': 0.05, 'pennies': 0.01}


def prepare_drink(drink: str) -> None:
    chosen_drink = MENU[drink]
    if not check_ressources(chosen_drink):
        return
    money_paid = request_coins()
    if money_paid < chosen_drink['cost']:
        print("Not enough money.")
        return
    elif money_paid > chosen_drink['cost']:
        change = money_paid - chosen_drink['cost']
        print(f"Here is ${change:.2f} in change.")
    update_resources(chosen_drink)
    print(f"Here is your {drink} enjoy.")


def update_resources(drink: dict) -> None:
    for key, value in drink['ingredients'].items():
        resources[key] -= value
    resources['money'] += drink['cost']


def check_ressources(drink) -> bool:
    for key, value in drink['ingredients'].items():
        if resources[key] >= value:
            return True
        else:
            print(f"Sorry there is not enough {key}.")
            return False


def request_coins() -> int:
    print("Please insert coins.")
    total = 0
    for key in coins:
        coin_num = int(input(f"How many {key}: "))
        total += coin_num * coins[key]
    return total


def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


def coffee_machine():
    is_running = True
    while is_running:
        choice = input(
            "What would you like (espresso/latte/cappuccion): ").lower()
        match choice:
            case "espresso":
                prepare_drink(choice)
            case "latte":
                prepare_drink(choice)
            case "cappuccion":
                prepare_drink(choice)
            case "report":
                print_report()
            case "off":
                break
            case _:
                print("Invalid Input.")


if __name__ == "__main__":
    coffee_machine()

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

if __name__ == "__main__":
    coffee_machine = CoffeeMaker()
    money_machine = MoneyMachine()
    menu = Menu()

    while True:
        choice = input(f"What would you like ({menu.get_items()}): ").lower()

        if choice == "report":
            coffee_machine.report()
            money_machine.report()
        elif choice == "off":
            break
        else:
            order = menu.find_drink(choice)
            if coffee_machine.is_resource_sufficient(order):
                money_machine.make_payment(order.cost)
                coffee_machine.make_coffee(order)

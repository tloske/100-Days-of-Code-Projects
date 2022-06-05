from art import logo


def add(x: float, y: float) -> float:
    return x + y


def multiply(x: float, y: float) -> float:
    return x * y


def divide(x: float, y: float) -> float:
    return x / y


def calculate(x: float) -> bool:
    operation = input("Pick an operation: ")

    y = float(input("What's the second number ?: "))

    result = 0
    match operation:
        case '+':
            result = add(x, y)
        case '-':
            result = add(x, -y)
        case '*':
            result = multiply(x, y)
        case '/':
            result = divide(x, y)
        case _:
            print("Invalid operation")

    print(f'{x} {operation} {y} = {result}')
    choice = input(
        f"Type 'y' to continue calulating with {result}, or type 'n' to start a new calcuation: ")

    match choice:
        case 'y':
            calculate(result)
        case 'n':
            return True
        case _:
            return False


if __name__ == '__main__':
    print(logo)
    is_running = True
    while is_running:
        x = float(input("What's the first number ?: "))
        print('+\n-\n*\n/')

        is_running = calculate(x)

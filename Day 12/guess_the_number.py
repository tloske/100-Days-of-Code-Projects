import random


def number_guesser():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' of 'hard': ")
    if difficulty == 'easy':
        lives = 10
    elif difficulty == 'hard':
        lives = 5
    else:
        print("Invalid input.")
        return

    secret_number = random.randint(1, 100)
    while lives:
        print(f"You have {lives} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        match guess:
            case guess if guess > secret_number:
                print("Too high.")
                lives -= 1
            case guess if guess < secret_number:
                print("Too low.")
                lives -= 1
            case guess if guess == secret_number:
                print("You guessed the number.")
                return
            case _:
                print("Invalid input.")
    print(f"You ran out of attempts the secret number was {secret_number}.")


if __name__ == '__main__':
    number_guesser()

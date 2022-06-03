import random
from hangman_art import logo, stages
from hangman_words import word_list
import os


def print_hangman():
    os.system("cls")
    print(stages[lives])
    print(''.join(display))


word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
display = ['_' for _ in chosen_word]

end_of_game = False
lives = 6

print(logo)

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You already guessed {guess}. You don't lose a life.")
    elif guess not in chosen_word:
        print(f"The letter {guess} is not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            print("You lose.")
            end_of_game = True
    else:
        for i in range(len(chosen_word)):
            if guess == chosen_word[i]:
                display[i] = guess
        if '_' not in display:
            end_of_game = True
            print("You win.")
    print_hangman()

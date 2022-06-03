import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇

print("Welcome to Rock Paper Scissors.")

choice = input(
    "Choose what to throw type either 'Rock', 'Paper' or 'Scissors'. ").lower()

choices = [rock, paper, scissors]

opponents_choice = choices[random.randint(0, len(choices) - 1)]

match choice:
    case 'rock':
        print(f"You chose:\n{rock}")
        print(f"Opponent chose:\n{opponents_choice}")
        if opponents_choice == rock:
            print("It's a draw.")
        elif opponents_choice == scissors:
            print("You won!!!")
        else:
            print("You lost!!!")
    case 'paper':
        print(f"You chose:\n{paper}")
        print(f"Opponent chose:\n{opponents_choice}")
        if opponents_choice == paper:
            print("It's a draw.")
        elif opponents_choice == rock:
            print("You won!!!")
        else:
            print("You lost!!!")
    case 'scissors':
        print(f"You chose:\n{scissors}")
        print(f"Opponent chose:\n{opponents_choice}")
        if opponents_choice == scissors:
            print("It's a draw.")
        elif opponents_choice == paper:
            print("You won!!!")
        else:
            print("You lost!!!")

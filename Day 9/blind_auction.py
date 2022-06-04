from art import logo
import os


print(logo)
print("Welcome to the secret auction program.")

auction = []
add_bid = True
while(add_bid):
    name = input("What is your name?: ").lower()
    bid = int(input("What is your bid?: $"))
    choice = input("Are there any other bidders? Type 'yes' or 'no'.")

    auction.append({'name': name, 'bid': bid})
    match choice:
        case 'yes':
            os.system('cls')
            pass
        case _:
            add_bid = False

winning_bid = 0
for bidder in auction:
    if bidder['bid'] > winning_bid:
        winning_bid = bidder['bid']
        winner = bidder['name']

print(f"The winner is {winner} with a bid of ${winning_bid}")

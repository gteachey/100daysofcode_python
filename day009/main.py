from art import logo

# import only system from os
from os import system, name
# import sleep to show output for some time period
from time import sleep
# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

print(logo)
print("Welcome to the secret auction")

another_bid = 'y'
bidders = {}

while another_bid == 'y':
    user_name = input("Please enter your name: ")
    user_bid = float(input("Please enter your bid: $"))
    bidders[user_name] = user_bid

    clear()
    print(logo)
    another_bid = input("Is there another bidder('y' or 'n')? ")


winning_bid = 0
for (user, bid) in bidders.items():
    if bid > winning_bid:
        winner_name = user
        winning_bid = bid


print(f"Congratulations {winner_name}!\nYou've won with a bid of ${winning_bid:.2f}.")
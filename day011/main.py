from art import logo
import random
from os import system, name

############### Blackjack Project #####################

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

def check_hand(card_hand):
    if sum(card_hand) > 21:
        # Report the hand busted by returning a 2
        return 2
    else:
        return 1


def add_card(card_hand, add_card):
    if add_card == 11:
        if sum(card_hand) + add_card > 21:
            add_card = 1
    card_hand.append(add_card)
    return check_hand(card_hand)


def display_hands(dealer_hand, user_hand):
    print(f"Dealer shows a {dealer_hand[0]}.")

    if len(user_hand) == 2:
        print(f"You hold a {user_hand[0]} and {user_hand[1]}; totaling {sum(user_hand)}")
    else:
        player_cards = ""

        for card in user_hand[0:-1]:
            player_cards += str(card) + ", "
        print(f"You hold a {player_cards}and {user_hand[-1]}; totaling {sum(user_hand)}")
    # return player_cards


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


print(logo)
print("Welcome Player! Let's play a game of Blackjack!")
user_input = input("Press 'y' to begin, any other key to quit\n>>> ")

while user_input.lower() == 'y':

    print(logo)

    for i in range(2):
        dealer_hand = [random.choice(cards), random.choice(cards)]
        user_hand = [random.choice(cards), random.choice(cards)]

    player_turn = True
    while player_turn:
        display_hands(dealer_hand, user_hand)
        # print(player_cards)
        user_choice = input("Your choice is: \n"
                            "'h' - Hit\n"
                            "'s' - Stand\n"
                            ">>> ")
        if user_choice.lower() == 'h':
            new_card = random.choice(cards)
            result = add_card(user_hand, new_card)
            if result == 2:
                print("Bust! Dealer Wins!")
                player_turn = False
        elif user_choice.lower() == 's':
            player_turn = False
            dealer_turn = True
            while dealer_turn:
                if sum(user_hand) > sum(dealer_hand) and sum(dealer_hand) < 17:
                    new_card = random.choice(cards)
                    result = add_card(dealer_hand, new_card)
                    if result == 2:
                        print("Bust! Player Wins!")
                        user_input = 'n'
                        dealer_turn = False
                else:
                    if sum(user_hand) > sum(dealer_hand):
                        print(f"Dealer has {sum(dealer_hand)}\nPlayer has {sum(user_hand)}\nPlayer wins!\n")
                    elif sum(user_hand) < sum(dealer_hand):
                        print(f"Dealer has {sum(dealer_hand)}\nPlayer has {sum(user_hand)}\nDealer wins!\n")
                    else:
                        print(f"Dealer has {sum(dealer_hand)}\nPlayer has {sum(user_hand)}\nPush!\n")
                    dealer_turn = False

    user_input = input("'y' or 'Y' - Play Again\n"
                       "'Any key' - Quit\n"
                       ">>> ")
    clear()

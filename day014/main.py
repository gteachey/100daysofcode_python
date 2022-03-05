from art import logo, vs
import game_data
import random
from replit import clear

'''
data = [
    {
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
        'country': 'United States'
    },
'''


def check_answer(answer, choiceOne, choiceTwo):
    right_answer = {}
    if choiceOne['follower_count'] > choiceTwo['follower_count']:
        right_answer = choiceOne
    else:
        right_answer = choiceTwo

    if right_answer == answer:
        return True
    return False


def get_choices():
    option_one = random.choice(game_data.data)
    # print(option_one)

    option_two = random.choice(game_data.data)
    while option_one == option_two:
        option_two = random.choice(game_data.data)
    # print(option_two)
    return option_one, option_two


def game():
    keep_going = True
    points = 0

    while keep_going:
        choiceOne, choiceTwo = get_choices()
        # clear()

        print(f"Choice A: {choiceOne['name']}, a {choiceOne['description']}, from {choiceOne['country']}.")
        print(vs)
        print(f"Choice B: {choiceTwo['name']}, a {choiceTwo['description']}, from {choiceTwo['country']}.")

        player_choice = input("Does 'A' or 'B' have more followers?\n").lower()
        while player_choice != 'a' and player_choice != 'b':
            print("Please enter 'A' or 'B'")
        if player_choice == 'a':
            answer = choiceOne
        else:
            answer = choiceTwo

        if check_answer(answer, choiceOne, choiceTwo):
            points += 1
            clear()
            print(logo)
            print(f"You're right! Total points: {points}\n")
        else:
            clear()
            print(logo)
            print(f"You're wrong! Total points: {points}\n")
            keep_going = False


print(logo)
game()

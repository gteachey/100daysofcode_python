import random
from art import logo
from os import system, name


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


print(logo)
print("Welcome to the Number Guessing Game!")
answer = random.randint(1, 100)
print("Alright! I've got a number between 1 and 100.")
user_input = input("Choose your difficulty:\n'1' - Easy\n'2' - Hard\n>>>")
num_of_choices = 10 if user_input == '1' else 5
while num_of_choices > 0:
    print(f"Chances remaining: {num_of_choices}")
    guess = int(input("What's your guess?\n>>> "))
    if guess == answer:
        print(f"Correct! The answer was {answer}")
        break
    elif guess < answer:
        print(f"Too low! The answer is higher than {guess}\n")
    else:
        print(f"Too high! The answer is lower than {guess}\n")
    num_of_choices -= 1

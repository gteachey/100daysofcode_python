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

#Write your code below this line 👇

hand_choices = [rock, paper, scissors]
print_hands = ['rock', 'paper', 'scissors']
print("Time to play some ROCK PAPER SCISSORS!")

choices = '\n'.join(map(str, [f"{index}: {value}" for (index, value) in enumerate(print_hands)]))
user_hand = int(input(f"What's your choice? \n{choices}\nInput: "))
comp_choice = random.randint(0, 2)
print(f"You: {hand_choices[user_hand]} vs Computer: {hand_choices[comp_choice]}")


if user_hand == comp_choice:
    print("Tie!!")
elif (user_hand + 1) % 3 == comp_choice:
    print("You Lost!")
else:
    print("You Won!")
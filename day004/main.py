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
hand_choices = ['rock', 'paper', 'scissors']
winning_hands = {
    'paper': 'rock',
    'scissors': 'paper',
    'rock': 'scissors'
}
print("Time to play some ROCK PAPER SCISSORS!")
user_hand = input(f"What's your choice? {' '.join(hand_choices)}\n")
comp_choice = random.choice(hand_choices)
print( winning_hands[user_hand])
print(comp_choice)
if user_hand == comp_choice:
    print("Tie!!")
elif winning_hands[user_hand] == comp_choice:
    print("You Win!")
else:
    print("Computer wins!")
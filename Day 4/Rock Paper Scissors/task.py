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

import random

# Ask player for entering a num 0 - 2 to pick Rock, Paper or Scissors
player_answer = ""
player_choice = ""
while player_answer != 0 and player_answer != 1 and player_answer != 2:
    player_answer = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    if player_answer == 0:
        player_choice = "rock"
    elif player_answer == 1:
        player_choice = "paper"
    elif player_answer == 2:
        player_choice = "scissors"

# Randomly select computers chose
rand_int = random.randint(0, 2)
computer_choice = ""
if rand_int == 0:
    computer_choice = "rock"
elif rand_int == 1:
    computer_choice = "paper"
elif rand_int == 2:
    computer_choice = "scissors"

# Print results
print("PLAYER:")
if player_choice == "rock":
    print(rock)
elif player_choice == "paper":
    print(paper)
else:
    print(scissors)

print("COMPUTER:")
if computer_choice == "rock":
    print(rock)
elif computer_choice == "paper":
    print(paper)
else:
    print(scissors)

if player_choice == "rock":
    if computer_choice == "rock":
        print("YOU TIED")
    elif computer_choice == "paper":
        print("YOU LOSE")
    else:
        print("YOU WIN")
if player_choice == "paper":
    if computer_choice == "rock":
        print("YOU WIN")
    elif computer_choice == "paper":
        print("YOU TIED")
    else:
        print("YOU LOSE")
if player_choice == "scissors":
    if computer_choice == "rock":
        print("YOU LOSE")
    elif computer_choice == "paper":
        print("YOU WIN")
    else:
        print("YOU TIED")
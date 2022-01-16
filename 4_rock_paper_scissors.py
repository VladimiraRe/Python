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

game_images = [rock, paper, scissors]

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if player >= 3 or player < 0:
    raise NameError("You typed an invalid number.")
else:
    print(game_images[player])

computer = random.randint(0, 2)
print(f"Computer chose:{game_images[computer]}")

if computer - player == 1 or computer - player == -2:
    print("You lose. :(")
elif computer - player == 0:
    print("It's a draw.")
else:
    print("You win!")
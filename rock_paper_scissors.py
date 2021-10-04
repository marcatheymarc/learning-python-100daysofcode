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

game_images = [rock, paper, scissors]
choice = int(input("Welcome to Rock Paper Scissors; Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
if choice >= 3 or choice < 0:
  print("Funny how that's not a valid number, you LOSE")
else:
  print(game_images[choice])

  computer_choices = random.randint(0, 2)
  print("Computer chose:")
  print(game_images[computer_choices])


  if choice == 0 and computer_choices == 2:
    print("You WIN")
  elif computer_choices == 0 and choice == 2:
    print("You Lose!")
  elif computer_choices > choice:
    print("Oh No you Lost!")
  elif choice > computer_choices:
    print("Yeah You win!")
  elif computer_choices == choice:
    print("It's a Draw!")
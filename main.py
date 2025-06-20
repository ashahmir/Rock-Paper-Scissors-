import random

gestures = ['''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''', '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''', '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''']

moves = ["Rock", "Paper", "Scissor"]

bot_choice = random.randint(0,2)
print("Welcome to Rock Paper Scissors!")
user_choice = int(input("Select Your Choice\n\tRock = 1\n\tPaper = 2\n\tScissors = 3\n"))
user_choice = user_choice - 1
print(f"You Chose {moves[user_choice]}")
print(gestures[user_choice])
print(f"Computer Chose {moves[bot_choice]}")
print(gestures[bot_choice])

if user_choice == 0 and bot_choice == 2:
    print("You Smashed The Scissors and Won!")
if user_choice == 1 and bot_choice == 0:
    print("You caught the rock and Won!")
if user_choice == 2 and bot_choice == 1:
    print("You cut down the Paper in pieces and Won!")
if user_choice == 0 and bot_choice == 1:
    print("The Paper Caught You, Better Luck Next Time")
if user_choice == 1 and bot_choice == 2:
    print("The Scissors cut right through you, Better Luck Next Time")
if user_choice == 2 and bot_choice == 0:
    print("The rock smashed you, Better Luck Next Time")
if user_choice == bot_choice:
    print("Game is Draw")




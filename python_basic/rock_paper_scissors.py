import random

# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

gamelist = [rock, paper, scissors]
yours = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computers = random.randint(0, 2)

print(gamelist[yours])
print(f"Computer chose: {computers}")
print(gamelist[computers])

if yours == computers:
    print("Draw!!")
elif yours == 0 and computers == 2:
    print("You Win!!!")
elif (yours-computers) > 0 and (yours-computers) < 2:
    print("You Win!!!")
else:
    print("You Lose!!!")


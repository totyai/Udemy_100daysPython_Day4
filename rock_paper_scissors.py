choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
import random
computer_choice = random.randint(0,2)

outcomes = ["""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
"""
    _______
---'   ____)____
          ______)
          _______)
          _______)
---.__________)
""",
"""
    _______
---'   ____)____
          ______)
        __________)
      (____)
---.__(___)
"""]

print("You chose:")
if choice == 0:
    print(outcomes[0])
elif choice == 1:
    print(outcomes[1])
else:
    print(outcomes[2])

print("Computer chose:")
if computer_choice == 0:
    print(outcomes[0])
elif computer_choice == 1:
    print(outcomes[1])
else:
    print(outcomes[2])

if choice == computer_choice:
    print("It's a draw")
elif (choice == 0 and computer_choice == 2) or (choice == 1 and computer_choice == 0) or (choice == 2 and computer_choice == 1):
    print("You win!")
elif (choice == 0 and computer_choice == 1) or (choice == 1 and computer_choice == 2) or (choice == 2 and computer_choice == 0):
    print("You lose!")
else:
    print("Invalid input, try again!")
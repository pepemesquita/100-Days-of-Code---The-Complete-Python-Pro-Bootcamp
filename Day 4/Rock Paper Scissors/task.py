import random

computer_choice = random.randint(0, 2)
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")) #Always remember to parse a string input to integer

if computer_choice == 0:
    print("Computer choose: Rock")
elif computer_choice == 1:
    print("Computer choose: Paper")
else:
    print("Computer choose: Scissors")

if user_choice == 0 and computer_choice == 1:
    print("You lose!")
elif user_choice == 1 and computer_choice == 2:
    print("You lose!")
elif user_choice == 2 and computer_choice == 0:
    print("You lose!")
elif user_choice == computer_choice:
    print("Is a draw, try again")
else:
    print("You won!")
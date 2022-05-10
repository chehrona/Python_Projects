import random

possibleList = ['r', 'p', 's']

compChoice = random.choice(possibleList)
print(compChoice)

playerChoice = input("What is your pick? ")

if compChoice == playerChoice:
    print("It is a tie")
elif (compChoice == 'r' and playerChoice == 'p') or (compChoice == 'p' and playerChoice == 's') or (compChoice == 's' and playerChoice == 'r'):
    print("You won!")
else:
    print("You lost")



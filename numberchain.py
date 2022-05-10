userInput = input("How many numbers? ")

userInputInt = int(userInput)

start = 0
numbers = []
while start < userInputInt:
    print(start)
    start += 1
    if start == userInputInt:
        again = input("Would you like to continue? ")
        if again == 'y':
            start = userInputInt
            userInput = input("How many numbers? ")
            userInputInt = int(userInput) + start
        else:
            print("Thanks for playing!")


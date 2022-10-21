import random

guessNumberStr = ""

def guess():
    print("\n**************************************************************\nI am thinking of a 3-digit number. Try to guess what it is.\n\nHere are some clues:\nWhen I say:    This means:\n\n  Pico         One digit is correct but in the wrong position.\n  Fermi        One digit is correct and in the right position.\n  Bagels       No digit is correct.\n\n\nI have thought up a number.\nYou have 10 guesses to get it.\n**************************************************************\n")
    randomNumberFinal = []
    i = 0
    while i < 3:
        i += 1
        randomGeneratedInt = random.randrange(0, 9)
        randomNumberFinal.append(str(randomGeneratedInt))
   

    for n in range(1, 11):
        print("Guess #{}".format(n))
        guessNumberStr = input()

        joinedListRandom = ''.join(randomNumberFinal)
        if guessNumberStr == joinedListRandom:
            print("You got it!")
            break     
        else:
            guessNumberToList = []
            finalAnswer = ""
            for digit in guessNumberStr:
                guessNumberToList.append(digit)
                if digit in randomNumberFinal and randomNumberFinal.index(digit) != guessNumberToList.index(digit):
                    answerStr = "Pico"
                elif digit in randomNumberFinal and randomNumberFinal.index(digit) == guessNumberToList.index(digit):
                    answerStr = "Fermi"
                else:
                    answerStr = "Bagels"
                finalAnswer += answerStr + " "
            print(finalAnswer)
        if n == 10:
            print("You ran out of guesses.")
            print("The answer was {}". format(joinedListRandom))

    anotherRound = input("Do you want to play again? (yes or no) ")
    if anotherRound == "yes":
        guess()
    elif anotherRound == "no":
        print("Thanks for playing!")
    return 




if __name__=="__main__":
    guess()
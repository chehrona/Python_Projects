import sys
import random


HEART = "\u2665"
SPADE = "\u2660"
CLUB = "\u2663"
DIAMOND = "\u2666"
TOTAL_MONEY = 5000
moneyLeft = 0

cardShapes = [HEART, SPADE, CLUB, DIAMOND]
cardValues = {"K": 10, "Q": 10, "J": 10, "A": [11, 1], "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10}

print("   Rules:\n\t Try to get as close to 21 without going over.\n\t Kings, Queens, and Jacks are worth 10 points.\n\t Aces are worth 1 or 11 points.\n\t "
      "Cards 2 through 10 are worth their face value.\n\t (H)it to take another card.\n\t (S)tand to stop taking cards.\n\t "
      "On your first play, you can (D)ouble down to increase your bet but must hit exactly one more time before standing.\n\t "
      "In case of a tie, the bet is returned to the player.\n\t The dealer stops hitting at 17.\nMoney: 5000")


betMoney = input("How much do you bet? (1-5000, or QUIT) ")
playerValue = 0
dealerValue = 0
playerCard = ""
dealerCard = ""
if int(betMoney) in range(1, 5001):
    moneyLeft = TOTAL_MONEY - int(betMoney)
    print("Bet:", betMoney)

dealerCardVal = random.choice(list(cardValues))
dealerValue += cardValues[dealerCardVal]
dealerCardShape = random.choice(cardShapes)
playerCardVal = random.choice(list(cardValues))
playerValue += cardValues[playerCardVal]
playerCardShape = random.choice(cardShapes)
playerCard = f" ____ \n|{playerCardVal}  |\n|  {playerCardShape} |\n|__{playerCardVal}|"
print(playerCard)
actionQuestion = input("(H)it, (S)tand, (D)ouble down")
if actionQuestion == "H":
    dealerCardVal = random.choice(list(cardValues))
    dealerValue += cardValues[dealerCardVal]
    dealerCardShape = random.choice(cardShapes)
    playerCardVal = random.choice(list(cardValues))
    playerValue += cardValues[playerCardVal]
    playerCardShape = random.choice(cardShapes)
elif actionQuestion == "S":
    if dealerValue <= 17:
        dealerCardVal = random.choice(list(cardValues))
        dealerValue += cardValues[dealerCardVal]
        dealerCardShape = random.choice(cardShapes)
elif betMoney == "QUIT":
    sys.exit()






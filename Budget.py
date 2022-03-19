class Category:

    def __init__(self, categoryName):
        self.categoryName = categoryName
        self.ledger = []
        self.money = 0.0

    def deposit(self, amount, description = ""):
        depositDict = dict()
        depositDict["amount"] = amount
        depositDict["description"] = description
        self.ledger.append(depositDict)
        self.money += float(amount)

    def withdraw(self, amount, description = ""):
        withdrawDict = dict()
        withdrawDict["amount"] = - amount
        withdrawDict["description"] = description
        if self.check_funds(amount) == False:
            return False
        else:
            self.money -= float(amount)
            self.ledger.append(withdrawDict)
            return True

    def get_balance(self):
        return self.money

    def transfer(self, amount, otherCategory):
        otherCategoryName = otherCategory.categoryName
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to {}".format(otherCategoryName))
            otherCategory.deposit(amount, "Transfer from {}".format(self.categoryName))
            return True
        else:
            return False

    def check_funds(self, amount):
            if amount > self.get_balance():
                return False
            else:
                return True

    def __str__(self):
        header = f'{self.categoryName:*^30}'
        rowsAdded = ""
        for entry in self.ledger:
            if len(entry["description"]) > 23:
                croppedDescription = f'{entry["description"][0:23]:<23}'
            else:
                croppedDescription = f'{entry["description"]:<23}'
            rowsAdded += croppedDescription + f'{entry["amount"]:>7.2f}' + "\n"

        totalBalance = f'Total: {self.money:<.2f}'
        receiptPicture = header + "\n" + rowsAdded + totalBalance
        return receiptPicture

def create_spend_chart(categoryListEntry):
    if len(categoryListEntry) > 4:
        return

    # Creates the percents from 0 to 100
    percentList = list()
    percent = -20
    while percent < 100:
        percent = percent + 10
        if percent == 110:
            break
        percentList.append(percent)

    # Finds the percentage of spending in each category
    percentPerCategoryList = []
    totalDepositedAmounts = 0
    withdrawalsPerCategory = []
    for category in categoryListEntry:

        depositedAmounts = 0
        withdrawnAmounts = 0
        accessingLedger = category.ledger
        for item in accessingLedger:
            if item["amount"] > 0:
                depositedAmounts += item["amount"]
            else:
                withdrawnAmounts += item["amount"]
        totalDepositedAmounts += depositedAmounts
        withdrawalsPerCategory.append(withdrawnAmounts)

    for value in withdrawalsPerCategory:
        decimalPercentage = (abs(value)/totalDepositedAmounts)*100
        percentPerCategory = int(round(decimalPercentage/10)*10)
        percentPerCategoryList.append(percentPerCategory)

    # Makes bubbles from the percentage. One bubble is 10%
    listOfBubblesPerCategory = []
    for perBubble in percentPerCategoryList:
        listOfBubbleNumber = ["o"]
        numberOfBubbles = int((perBubble/10) + 1)
        for i in range(0, 12):
            if i < numberOfBubbles:
                listOfBubbleNumber.append("o")
            else:
                listOfBubbleNumber.append(" ")
        listOfBubblesPerCategory.append(listOfBubbleNumber)

    # Converts category names to its list of letters
    nameLengthsList = []
    categoryNamesList = []
    for item in categoryListEntry:
        categoryName = item.categoryName
        categoryNamesList.append(categoryName)
        nameLength = len(categoryName)
        nameLengthsList.append(nameLength)

    longestName = max(nameLengthsList)

    # Add spaces for names that are shorter
    for name in categoryNamesList:
        if  len(name) < longestName:
            categoryNameIndex = categoryNamesList.index(name)
            categoryNamesList[categoryNameIndex] = name + (longestName - len(name)) * " "

    # Prints out the lefthand side percents(0-100), bubbles and the bottom dashes
    # for upto 4 categories
    rowSpelling = ""
    finalSpelling = ""
    finalResult = ""

    i = 12
    while i > 1:
        i = i - 1
        lefthandPercents = f'{str(percentList[i]):>3}' + "|" + " "
        percentHeader = "Percentage spent by category" + "\n"
        if len(categoryListEntry) == 1:
            rowSpelling = lefthandPercents + listOfBubblesPerCategory[0][i] + 2*" "
            if i == 1:
                rowSpelling = lefthandPercents  + listOfBubblesPerCategory[0][i] + \
                + 2*" " + "\n" + 4*" " + 4*"-"
            elif i == 11:
                rowSpelling = percentHeader + lefthandPercents + \
                listOfBubblesPerCategory[0][i] + 2*" "
        elif len(categoryListEntry) == 2:
            rowSpelling = lefthandPercents + \
            listOfBubblesPerCategory[0][i] + "  " + listOfBubblesPerCategory[1][i] + 2*" "
            if i == 1:
                rowSpelling = lefthandPercents + \
                listOfBubblesPerCategory[0][i] + "  " + listOfBubblesPerCategory[1][i] \
                + 2*" " + "\n" + 4*" " + 7*"-"
            elif i == 11:
                rowSpelling = percentHeader + lefthandPercents + \
                listOfBubblesPerCategory[0][i] + "  " + listOfBubblesPerCategory[1][i] + 2*" "
        elif len(categoryListEntry) == 3:
            rowSpelling = lefthandPercents + listOfBubblesPerCategory[0][i] + "  " + listOfBubblesPerCategory[1][i] + \
            "  " + listOfBubblesPerCategory[2][i] + 2*" "
            if i == 1:
                rowSpelling = lefthandPercents + listOfBubblesPerCategory[0][i] + "  " + listOfBubblesPerCategory[1][i] + \
                "  " + listOfBubblesPerCategory[2][i] + 2*" " + "\n" + 4*" " + 10*"-"
            elif i == 11:
                rowSpelling = percentHeader + lefthandPercents + \
                listOfBubblesPerCategory[0][i] + "  " + listOfBubblesPerCategory[1][i] + \
                "  " + listOfBubblesPerCategory[2][i] + 2*" "
        else:
            rowSpelling = lefthandPercents + \
            listOfBubblesPerCategory[0][i] + "  " + listOfBubblesPerCategory[1][i] + \
            "  " + listOfBubblesPerCategory[2][i] + "  " + listOfBubblesPerCategory[3][i] + 2*" "
            if i == 1:
                rowSpelling = lefthandPercents + \
                listOfBubblesPerCategory[0][i] + "  " + listOfBubblesPerCategory[1][i] + \
                "  " + listOfBubblesPerCategory[2][i] + "  " + listOfBubblesPerCategory[3][i] \
                + 2*" "+ "\n" + 4*" " + 13*"-"
            elif i == 11:
                rowSpelling = percentHeader + lefthandPercents + \
                listOfBubblesPerCategory[0][i] + "  " + listOfBubblesPerCategory[1][i] + \
                "  " + listOfBubblesPerCategory[2][i] + "  " + listOfBubblesPerCategory[3][i] + 2*" "
        finalResult += rowSpelling + "\n"

    # Iterates through the category names and adds the letters to the rowSpelling string
    verticalNameSpelling = ""
    for length in range(0, longestName):
        if len(categoryListEntry) == 1:
            verticalNameSpelling = 5*" " + categoryNamesList[0][length] + "  "
        elif len(categoryListEntry) == 2:
            verticalNameSpelling = 5*" " + categoryNamesList[0][length] + \
            "  " + categoryNamesList[1][length] + "  "
        elif len(categoryListEntry) == 3:
            verticalNameSpelling = 5*" " + categoryNamesList[0][length] + \
            "  " + categoryNamesList[1][length] + "  " + categoryNamesList[2][length]\
            + "  "
        else:
            verticalNameSpelling = 5*" " + categoryNamesList[0][length] + \
            "  " + categoryNamesList[1][length] + "  " + categoryNamesList[2][length] + \
            "  " + categoryNamesList[3][length] + "  "
        if length == longestName - 1:
            finalResult += verticalNameSpelling
        else:
            finalResult += verticalNameSpelling + "\n"
    return finalResult



food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")
food.deposit(600, "deposit")
food.withdraw(437, "milk, cereal, eggs, bacon, bread")
entertainment.deposit(300)
entertainment.withdraw(185, "trip")
business.deposit(100, "work order")
business.withdraw(85, "flyers")

print(food)
print(entertainment)
print(business)
print(create_spend_chart([entertainment, business, food]))

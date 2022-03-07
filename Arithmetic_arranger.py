def computing_errors(problems):
    justValues = ""
    if len(problems) > 5:
        return "Error: Too many problems."
    for entry in problems:
        individualExpression = entry.split()
        operator = individualExpression[1]
        firstValue = str(individualExpression[0])
        secondValue = str(individualExpression[2])
        justValues = firstValue + secondValue
        for i in justValues:
            if i.isdigit():
                continue
            else:
                return "Error: Numbers must only contain digits."
        if operator == "*" or operator == "/":
            return "Error: Operator must be \'+\' or \'-\'."
        elif len(firstValue) > 4 or len(secondValue) > 4:
            return "Error: Numbers cannot be more than four digits."
    return False



# parameter: {list} problems
# return void
def arithmetic_arranger(problems, shouldPrint = False):
    arranged_problems = ""
    operators = []
    allFirstValues = []
    allSecondValues = []
    allFinalResults = ""
    hasError = computing_errors(problems)
    if hasError != False:
      return hasError


    finalResults = ""
    indexCounter = 0
    for entry in problems:
        individualExpression = entry.split()
        operator = individualExpression[1]
        operators.append(operator)
        firstValueInt = int(individualExpression[0])
        secondValueInt = int(individualExpression[2])
        allFirstValues.append(firstValueInt)
        allSecondValues.append(secondValueInt)
        maxValue = max(firstValueInt, secondValueInt)
        result = ""
        if shouldPrint == True and operator == "+":
            result = str(firstValueInt + secondValueInt)
        elif shouldPrint == True and operator == "-":
            result = str(firstValueInt - secondValueInt)




        # if len(result) == len(str(maxValue)):
        numberSpaces = (len(str(maxValue)) + 2) - (len(result))
        # elif len(result) < len(str(maxValue)):
        #     numberSpaces = 3
        # else:
        #     numberSpaces = 1
        totalSpaces = " " * numberSpaces

        if indexCounter == len(problems) - 1:
            finalResults += totalSpaces + result
        else:
            finalResults += totalSpaces + result + "    "
        indexCounter = indexCounter + 1

    allFinalResults = finalResults

    finalStringFirst = ""

    for index in range(0, len(allFirstValues)):
        firstValue = allFirstValues[index]
        secondValue = allSecondValues[index]
        maxValue = max(int(firstValue), int(secondValue))
        if firstValue == maxValue:
            numberSpaces = 2
        else:
            numberSpaces = 2 + (len(str(secondValue)) - len(str(firstValue)))

        totalSpaces = " " * numberSpaces
        if index == len(allFirstValues) - 1:
            finalStringFirst += totalSpaces + str(firstValue)
        else:
            finalStringFirst += totalSpaces + str(firstValue) + "    "

    finalStringSecond = ""

    for index in range(0, len(allSecondValues)):
        firstValue = allFirstValues[index]
        secondValue = allSecondValues[index]
        operator = operators[index]
        maxValue = max(int(firstValue), int(secondValue))
        if secondValue == maxValue:
            numberSpaces = 0
        else:
            numberSpaces = len(str(firstValue)) - len(str(secondValue))

        totalSpaces = " " * numberSpaces
        if index == len(allFirstValues) - 1:
            finalStringSecond += operator + " " + totalSpaces + str(secondValue)
        else:
            finalStringSecond += operator + " " + totalSpaces + str(secondValue) + "    "


    finalStringJustDashes = ""
    for index in range(0, len(allSecondValues)):
        firstValue = allFirstValues[index]
        secondValue = allSecondValues[index]
        maxValue = max(int(firstValue), int(secondValue))
        if secondValue == maxValue or firstValue == maxValue:
            numberDashes = (len(str(maxValue)) + 2)

        totalDashes = "-" * numberDashes
        if index == len(allFirstValues) - 1:
            finalStringJustDashes += totalDashes
        else:
            finalStringJustDashes += totalDashes + "    "

    if shouldPrint == True:
        arranged_problems = finalStringFirst + "\n" + finalStringSecond + "\n" + finalStringJustDashes + "\n" + allFinalResults
    else:
        arranged_problems = finalStringFirst + "\n" + finalStringSecond + "\n" + finalStringJustDashes

    return arranged_problems


print(arithmetic_arranger(['3 + 855', '988 + 40'], True))

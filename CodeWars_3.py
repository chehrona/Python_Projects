def narcissistic(value):
    valueStr = str(value)
    resultPower = []
    for digit in valueStr:
        digitInt = int(digit)
        powerDigit = digitInt**(len(valueStr))
        resultPower.append(powerDigit)
    sumItems = sum(resultPower)
    print(sumItems)
    if sumItems == value:
        return True
    else:
        return False

print(narcissistic(371))

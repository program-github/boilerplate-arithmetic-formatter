def arithmetic_arranger(problems, showResultLine=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    firstLineArray = []
    secondLineArray = []
    thirdLineArray = []
    fourthLineArray = []
    for i in problems:
        number_sections = i.split()
        firstNumber = number_sections[0]
        secondNumber = number_sections[2]
        if len(firstNumber) > 4 or len(secondNumber) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        if not firstNumber.isdigit() or not secondNumber.isdigit():
            return 'Error: Numbers must only contain digits.'

        converted_operator = number_sections[1]
        if converted_operator == '+':
            fourthLineCal = int(firstNumber) + int(secondNumber)
            fourthLineAns = str(fourthLineCal)
        elif converted_operator == '-':
            fourthLineCal = int(firstNumber) - int(secondNumber)
            fourthLineAns = str(fourthLineCal)
        else:
            return "Error: Operator must be '+' or '-'."
        firstNumberLenght = len(firstNumber)
        secondNumberLenght = len(secondNumber)
        operator = number_sections[1] + ' '
        firstNumberSpace = '  '
        firstNumberFormatted = firstNumber
        secondNumberFormatted = secondNumber
        if firstNumberLenght > secondNumberLenght:
            space_difference = firstNumberLenght - secondNumberLenght
            secondNumberFormatted = ' ' * space_difference + secondNumber
        elif secondNumberLenght > firstNumberLenght:
            space_difference = secondNumberLenght - firstNumberLenght
            firstNumberFormatted = ' ' * space_difference + firstNumber
        firstline = firstNumberSpace + firstNumberFormatted
        secondline = operator + secondNumberFormatted
        thirdline = '-' * len(secondline)
        fourthLineLength = len(thirdline) - len(fourthLineAns)
        fourthline = ' ' * fourthLineLength + fourthLineAns
        firstLineArray.append(firstline)
        secondLineArray.append(secondline)
        thirdLineArray.append(thirdline)
        fourthLineArray.append(fourthline)
    masterFirstline = '    '.join(firstLineArray)
    masterSecondline = '    '.join(secondLineArray)
    masterThirdline = '    '.join(thirdLineArray)
    masterfourthline = '    '.join(fourthLineArray)
    printLine = masterFirstline + '\n' + masterSecondline + '\n' + masterThirdline
    if showResultLine:
        printLine = printLine + '\n' + masterfourthline
    return printLine

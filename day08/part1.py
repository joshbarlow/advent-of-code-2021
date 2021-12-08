def importData():
    with open('input.txt') as input_file:
        inputDataArray = input_file.readlines()
    return inputDataArray

def calculateOutput(inputDataArray):

    cleanInputArray = []

    for line in inputDataArray:
        if (line[-1] == '\n'):
            cleanInputArray.append(line[:-1])
        else:
            cleanInputArray.append(line)

    finalTotal = 0
    correctDigits = [2,3,4,7]

    for line in cleanInputArray:
        linesplit = line.split('|')
        outputSplit = linesplit[1].split()
        for digit in outputSplit:
            le = len(digit)
            #print(digit + ' - ' + str(le))
            if(le in correctDigits):
                finalTotal += 1

    return finalTotal
        
if __name__ == '__main__':
    print(calculateOutput(importData()))
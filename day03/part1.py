def importData():
    with open('input.txt') as input_file:
        inputDataArray = input_file.readlines()
    return inputDataArray

def calculatePower(inputDataArray):

    binaryArray = [0] * (len(inputDataArray[0])-1)

    for inputLine in range(len(inputDataArray)):
        for x in range(len(binaryArray)):
            binaryArray[x] += int(inputDataArray[inputLine][x])

    for x in range(len(binaryArray)):
        binaryArray[x] = binaryArray[x]/len(inputDataArray)

    
    gammaString = ''
    epsilonString = ''

    for x in binaryArray:
        if (x < 0.5):
            gammaString += '0'
            epsilonString += '1'
        else:
            gammaString += '1'
            epsilonString += '0'


    return int(gammaString, 2) * int(epsilonString, 2)

        
if __name__ == '__main__':
    print(calculatePower(importData()))
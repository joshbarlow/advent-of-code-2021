def importData():
    with open('input.txt') as input_file:
        inputDataArray = input_file.readlines()
    return inputDataArray

def calculateLifeRating(inputDataArray):

    cleanInputArray = []

    for line in inputDataArray:
        if (line[-1] == '\n'):
            cleanInputArray.append(line[:-1])
        else:
            cleanInputArray.append(line)
    
    ##print(calculateOxygen(cleanInputArray))
    ##print(calculateC02(cleanInputArray))
    
    return calculateOxygen(cleanInputArray) * calculateC02(cleanInputArray)
    

    
def calculateOxygen(cleanInputArray):

    binaryLength = len(cleanInputArray[0])
    finalBinary = ''

    for x in range(binaryLength):

        workingArray = []
        runningTotal = 0
        mostCommon = 0

        for y in range(len(cleanInputArray)):
            runningTotal += int(cleanInputArray[y][x])
        
        if (runningTotal/len(cleanInputArray) >= 0.5):
            mostCommon = 1

        for y in range(len(cleanInputArray)):
            if (int(cleanInputArray[y][x]) == mostCommon):
                workingArray.append(cleanInputArray[y])
        
        if (len(workingArray) == 1):
            finalBinary = workingArray[0]
            break
        
        cleanInputArray = workingArray
    
    return int(finalBinary, 2)

def calculateC02(cleanInputArray):

    binaryLength = len(cleanInputArray[0])
    finalBinary = ''

    for x in range(binaryLength):

        workingArray = []
        runningTotal = 0
        mostCommon = 1

        for y in range(len(cleanInputArray)):
            runningTotal += int(cleanInputArray[y][x])
        
        if (runningTotal/len(cleanInputArray) >= 0.5):
            mostCommon = 0

        for y in range(len(cleanInputArray)):
            if (int(cleanInputArray[y][x]) == mostCommon):
                workingArray.append(cleanInputArray[y])
        
        #print(workingArray)
        
        if (len(workingArray) == 1):
            finalBinary = workingArray[0]
            break
        
        cleanInputArray = workingArray
    
    return int(finalBinary, 2)
        



        
if __name__ == '__main__':
    print(calculateLifeRating(importData()))
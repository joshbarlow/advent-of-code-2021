def importData():
    with open('input.txt') as input_file:
        inputDataArray = input_file.readlines()
    return inputDataArray

def calculateRiskLevel(inputDataArray):

    cleanInputArray = []

    for line in inputDataArray:
        if (line[-1] == '\n'):
            cleanInputArray.append(line[:-1])
        else:
            cleanInputArray.append(line)

    xLength = len(cleanInputArray[0])
    yLength = len(cleanInputArray)

    gridArray =[]

    for x in range(xLength):
        tmpArray = []
        for y in range(yLength):
            tmpArray.append(int(cleanInputArray[y][x]))
        gridArray.append(tmpArray)
    
    riskLevel = 0   

    for x in range(xLength):
        for y in range(yLength):
            Lowest = True
            # x's
            if(x!=0):
                if(gridArray[x][y] >= gridArray[x-1][y]):
                    Lowest = False
            if(x!=xLength-1):
                if(gridArray[x][y] >= gridArray[x+1][y]):
                    Lowest = False
            # y's
            if(y!=0):
                if(gridArray[x][y] >= gridArray[x][y-1]):
                    Lowest = False
            if(y!=yLength-1):
                if(gridArray[x][y] >= gridArray[x][y+1]):
                    Lowest = False
            
            if(Lowest):
                riskLevel += (1 + gridArray[x][y])
                #print(gridArray[x][y])
            
    return riskLevel

if __name__ == '__main__':
    print(calculateRiskLevel(importData()))
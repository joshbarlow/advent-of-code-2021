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
    
    riskLevel = 1
    basinDict = {}

    for x in range(xLength):
        for y in range(yLength):
            lowest = findLowest(x,y,xLength,yLength,gridArray)
            if(lowest in basinDict.keys()):
                basinDict[lowest] += 1
            else:
                basinDict[lowest] = 1
    
    #print(basinDict)

    for x in range(3):
        highest = 0
        highestKey = ''
        for key in basinDict.keys():
            if(basinDict[key] >= highest):
                highest = basinDict[key]
                highestKey = key
        riskLevel = riskLevel * highest
        #print(basinDict[highestKey])
        del basinDict[highestKey]
            
    return riskLevel

# recursion time!
def findLowest(x,y,xLength,yLength,gridArray):
    Lowest = True
    lowestNum = 10
    lowestX = 0
    lowestY = 0
    # x's
    if(x!=0):
        if(gridArray[x][y] >= gridArray[x-1][y]):
            Lowest = False
            if(lowestNum > gridArray[x-1][y]):
                lowestNum = gridArray[x-1][y]
                lowestX = x-1
                lowestY = y

    if(x!=xLength-1):
        if(gridArray[x][y] >= gridArray[x+1][y]):
            Lowest = False
            if(lowestNum > gridArray[x+1][y]):
                lowestNum = gridArray[x+1][y]
                lowestX = x+1
                lowestY = y
    # y's
    if(y!=0):
        if(gridArray[x][y] >= gridArray[x][y-1]):
            Lowest = False
            if(lowestNum > gridArray[x][y-1]):
                lowestNum = gridArray[x][y-1]
                lowestX = x
                lowestY = y-1

    if(y!=yLength-1):
        if(gridArray[x][y] >= gridArray[x][y+1]):
            Lowest = False
            if(lowestNum > gridArray[x][y+1]):
                lowestNum = gridArray[x][y+1]
                lowestX = x
                lowestY = y+1
            
    if(Lowest):
        #print(gridArray[x][y])
        return(str(x) + ',' + str(y))
    if(gridArray[x][y] == 9):
        return(str(x) + ',' + str(y))
    else:
        return(findLowest(lowestX,lowestY,xLength,yLength,gridArray))

if __name__ == '__main__':
    print(calculateRiskLevel(importData()))
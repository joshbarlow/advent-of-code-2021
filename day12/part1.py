import copy

def importData():
    with open('input.txt') as input_file:
        inputDataArray = input_file.readlines()
    return inputDataArray

def calculatePaths(inputDataArray):

    cleanInputArray = []

    for line in inputDataArray:
        if (line[-1] == '\n'):
            cleanInputArray.append(line[:-1])
        else:
            cleanInputArray.append(line)
    
    connectionList = []

    for line in cleanInputArray:
        splitLine = line.split('-')
        tmpArray = [splitLine[0],splitLine[1]]
        connectionList.append(tmpArray)
        tmpArray = [splitLine[1],splitLine[0]]
        connectionList.append(tmpArray)

    #for line in connectionList:
    #    print(line)

    connectionDict = {}

    for line in connectionList:
        if(line[0] in connectionDict.keys() and line[1] != 'start'):
            connectionDict[line[0]].append(line[1])
        elif(line[1] != 'start'):
            connectionDict[line[0]] = [line[1]]
    
    #for key in connectionDict.keys():
    #    connectionDict[key] = list(connectionDict[key])
    
    # print(connectionDict)
    
    path = []
    cave = 'start'

    numPaths = calculateNumPaths(cave,path,connectionDict)

    return numPaths

def calculateNumPaths(currentCave,path,connectionDict):

    newPath = copy.deepcopy(path)
    numPaths = 0
    newPath.append(currentCave)
    curCave = copy.deepcopy(currentCave)

    # print(connectionDict[curCave])

    for connectingCave in connectionDict[curCave]:
        
        stringPath = ''
        for x in newPath:
            stringPath += x + ' -> '
        stringPath += connectingCave

        # print('checking ' + stringPath)

        endCave = False
        smallCave = connectingCave.islower()
        alreadyVisited = False

        if(connectingCave == 'end'):
            endCave = True
        if(connectingCave in newPath):
            alreadyVisited = True
        
        # print('End: ' + str(endCave) + ', Small: ' + str(smallCave) + ' Already Visited: ' + str(alreadyVisited))

        if(endCave):
            # print('-> END')
            numPaths += 1
        elif(smallCave and not alreadyVisited):
                numPaths += calculateNumPaths(connectingCave,newPath,connectionDict)
        elif(not smallCave):
            numPaths += calculateNumPaths(connectingCave,newPath,connectionDict)
        # elif(smallCave and alreadyVisited):
            # print('deadEnd')
    
    return numPaths

if __name__ == '__main__':
    print(calculatePaths(importData()))
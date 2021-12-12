def importData():
    with open('input.txt') as input_file:
        inputDataArray = input_file.readlines()
    return inputDataArray

def calculateFlashes(inputDataArray):

    cleanInputArray = []

    for line in inputDataArray:
        if (line[-1] == '\n'):
            cleanInputArray.append(line[:-1])
        else:
            cleanInputArray.append(line)

    octopusArray = []

    for y in cleanInputArray:
        xArray = []
        for x in list(y):
            xArray.append(int(x))
        octopusArray.append(xArray)
    
    tmpArray = []

    for x in range(10):
        tmpYArray = []
        for y in range(10):
            tmpYArray.append(octopusArray[y][x])
        tmpArray.append(tmpYArray)

    octopusArray = tmpArray

    del tmpArray

    #for line in octopusArray:
    #    print(line)
    #print('= = = = = = = = = =')

    steps = 100
    flashes = 0

    for step in range(steps):
        flashes, octopusArray = calcStep(flashes,octopusArray)
        #for line in octopusArray:
        #    print(line)
        #print(flashes)
        #print('= = = = = = = = = =')
    
    return flashes

def calcStep(flashes,octopusArray):

    tens = 0

    for x in range(10):
        for y in range(10):
            octopusArray[x][y] += 1
            if(octopusArray[x][y] > 9):
                tens += 1

    while (tens > 0):
        tens = 0
        for x in range(10):
            for y in range(10):
                if(octopusArray[x][y] > 9):
                    octopusArray[x][y] = 0
                    flashes += 1
                    neighbours = getNeighbours(x,y)
                    #print(neighbours)
                    for nbr in neighbours:
                        if(octopusArray[nbr[0]][nbr[1]] > 0):
                            octopusArray[nbr[0]][nbr[1]] += 1
                            if (octopusArray[nbr[0]][nbr[1]] > 9):
                                tens += 1
            
    return flashes,octopusArray
        

def getNeighbours(x,y):
    neighbourList = []
    for xcount in range(3):
        for ycount in range(3):
            nx = x + (xcount-1)
            ny = y + (ycount-1)
            if(nx >= 0 and nx <= 9 and ny >= 0 and ny <= 9):
                nbr = [nx,ny]
                neighbourList.append(nbr)

    return neighbourList


if __name__ == '__main__':
    print(calculateFlashes(importData()))
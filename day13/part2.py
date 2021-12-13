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
    
    points = []
    folds = []

    for x in cleanInputArray:
        if('fold along' in x):
            # print(f"{x[11:]} from {x}")
            folds.append(x[11:].split('='))
        elif(len(x)>0):
            points.append(x.split(','))
    
    # print(points)
    # print(folds)

    xlen = 0
    ylen = 0

    for x in points:
        if(int(x[0]) > xlen ):
            xlen = int(x[0])
        if(int(x[1]) > ylen ):
            ylen = int(x[1])
    
    # print(str(xlen) + ' ' + str(ylen))

    pointGrid = []

    for x in range(xlen + 1):
        tmpYarray = []
        for y in range(ylen + 1):
            tmpYarray.append(0)
        pointGrid.append(tmpYarray)

    for x in points:
        pointGrid[int(x[0])][int(x[1])] = 1

    # print(pointGrid)

    for x in folds:
        pointGrid = fold(pointGrid,x)

    count = 0

    for x in pointGrid:
        for y in x:
            if(y > 0):
                count += 1

    output = '\n'
    
    for y in range(len(pointGrid[0])):
        tmpLine = ''
        for x in range(len(pointGrid)):
            if pointGrid[x][y] > 0:
                tmpLine += 'X'
            else:
                tmpLine += ' '
        tmpLine += '\n'
        output += tmpLine
    
    # print(output)
            
    return output

def fold(pointGrid,fold):

    # pointgridA = copy.deepcopy(pointGrid)
    pointgridB = copy.deepcopy(pointGrid)

    foldHeight = int(fold[1])
    foldAxis = fold[0]

    if(foldAxis == 'x'):
        # print('fold X')

        for x in range(len(pointgridB)):
            for y in range(len(pointgridB[0])):
                if(x < foldHeight and (foldHeight + (foldHeight - x)) < len(pointgridB) ):
                    pointgridB[x][y] += pointgridB[foldHeight + (foldHeight - x)][y]
                    # print(f'{x},{y} -> {x},{foldHeight + (foldHeight - y)}')
        
        for x in range(len(pointgridB)):
            for y in range(len(pointgridB[0])):
                if(x > foldHeight):
                    pointgridB[x][y] = 0
        
        newArray = []
        lenX = foldHeight
        lenY = len(pointgridB[0])

        for x in range(lenX):
            tmpLine = []
            for y in range(lenY):
                tmpLine.append(pointgridB[x][y])
            newArray.append(tmpLine)
        
        pointgridB = newArray
    
    elif(foldAxis == 'y'):
        # print('fold y')

        for x in range(len(pointgridB)):
            for y in range(len(pointgridB[0])):
                if(y < foldHeight and (foldHeight + (foldHeight - y)) < len(pointgridB[0]) ):
                    pointgridB[x][y] += pointgridB[x][foldHeight + (foldHeight - y)]
                    # print(f'{x},{y} -> {x},{foldHeight + (foldHeight - y)}')
        
        for x in range(len(pointgridB)):
            for y in range(len(pointgridB[0])):
                if(y > foldHeight):
                    pointgridB[x][y] = 0
        
        newArray = []
        lenX = len(pointgridB)
        lenY = foldHeight

        for x in range(lenX):
            tmpLine = []
            for y in range(lenY):
                tmpLine.append(pointgridB[x][y])
            newArray.append(tmpLine)
        
        pointgridB = newArray


    # print(pointgridB)
    return pointgridB

if __name__ == '__main__':
    print(calculatePaths(importData()))
import copy

def importData():
    with open('input.txt') as input_file:
        inputDataArray = input_file.readlines()
    return inputDataArray

def calculateFolds(inputDataArray):

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

    pointGrid = fold(pointGrid,folds[0])

    count = 0

    for x in pointGrid:
        for y in x:
            if(y > 0):
                count += 1

    return count

def fold(pointGrid,fold):

    pointgridA = copy.deepcopy(pointGrid)
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
    
    elif(foldAxis == 'y'):
        # print('fold y')

        # for x in range(len(pointgridA)):
        #     for y in range(len(pointgridA[0])):
        #         if(y > foldHeight):
        #             pointgridA[x][y] = 0

        # for x in range(len(pointgridB)):
        #     for y in range(len(pointgridB[0])):
        #         if(y <= foldHeight):
        #             pointgridB[x][y] = 0

        # flip B

        for x in range(len(pointgridB)):
            for y in range(len(pointgridB[0])):
                if(y < foldHeight and (foldHeight + (foldHeight - y)) < len(pointgridB[0]) ):
                    pointgridB[x][y] += pointgridB[x][foldHeight + (foldHeight - y)]
                    # print(f'{x},{y} -> {x},{foldHeight + (foldHeight - y)}')
        
        for x in range(len(pointgridB)):
            for y in range(len(pointgridB[0])):
                if(y > foldHeight):
                    pointgridB[x][y] = 0

    # print(pointgridB)
    return pointgridB

if __name__ == '__main__':
    print(calculateFolds(importData()))
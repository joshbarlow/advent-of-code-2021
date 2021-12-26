import copy, string, os, time

def importData():
    with open('input.txt') as input_file:
        inputDataArray = input_file.readlines()
    return inputDataArray

def calculateCucumberSteps(inputDataArray):

    cleanInputArray = []

    for line in inputDataArray:
        if (line[-1] == '\n'):
            cleanInputArray.append(line[:-1])
        else:
            cleanInputArray.append(line)
    
    seaFloorArray = []

    for y in range(len(cleanInputArray)):
        seaFloorArray.append(list(cleanInputArray[y]))
    
    # for y in range(len(seaFloorArray)):
    #     line = ''
    #     for x in range(len(seaFloorArray[0])):
    #         line += seaFloorArray[y][x]
    #     print(line)

    Turns = 0
    Finished = False

    while (Finished == False):
        Turns += 1
        seaFloorArray, Finished = cucumberProcess(seaFloorArray)

        os.system('clear')

        for y in range(len(seaFloorArray)):
            line = ''
            for x in range(len(seaFloorArray[0])):
                line += seaFloorArray[y][x]
            print(line)

        # time.sleep(0.1)
    
    print('\n')

    # for y in range(len(seaFloorArray)):
    #     line = ''
    #     for x in range(len(seaFloorArray[0])):
    #         line += seaFloorArray[y][x]
    #     print(line)

    return Turns

def cucumberProcess(seaFloorArray):

    newSeaFloorArray = copy.deepcopy(seaFloorArray)

    finished = True

    # East cucumbers

    for y in range(len(seaFloorArray)):
        for x in range(len(seaFloorArray[0])):
            # check if it's an '>'
            if (seaFloorArray[y][x] == '>'):
                # check the next space is free
                newX = x + 1
                if(newX > (len(seaFloorArray[0])-1)):
                    newX = 0
                
                if (seaFloorArray[y][newX] == '.'):
                    # update the 'new' array
                    newSeaFloorArray[y][x] = '.'
                    newSeaFloorArray[y][newX] = '>'

                    # set finished to False?
                    finished = False
    
    seaFloorArray = copy.deepcopy(newSeaFloorArray)

    for y in range(len(seaFloorArray)):
        for x in range(len(seaFloorArray[0])):
            # check if it's an '>'
            if (seaFloorArray[y][x] == 'v'):
                # check the next space is free
                newY = y + 1
                if(newY > (len(seaFloorArray)-1)):
                    newY = 0
                
                if (seaFloorArray[newY][x] == '.'):
                    # update the 'new' array
                    newSeaFloorArray[y][x] = '.'
                    newSeaFloorArray[newY][x] = 'v'

                    # set finished to False?
                    finished = False
    
    return newSeaFloorArray, finished

if __name__ == '__main__':
    print(calculateCucumberSteps(importData()))
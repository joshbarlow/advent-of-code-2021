def importData():
    with open('input.txt') as input_file:
        inputDataArray = input_file.readlines()
    return inputDataArray

def calculateDepth(inputDataArray):

    depth = 0
    horizontal = 0
    aim = 0

    for inputLine in range(len(inputDataArray)):

        splitInput = inputDataArray[inputLine].split()

        if (splitInput[0] == 'forward'):
            horizontal += int(splitInput[1])
            depth += int(splitInput[1]) * aim
        elif (splitInput[0] == 'down'):
            aim += int(splitInput[1])
        elif (splitInput[0] == 'up'):
            aim -= int(splitInput[1])
    
    return depth * horizontal
        
if __name__ == '__main__':
    print(calculateDepth(importData()))
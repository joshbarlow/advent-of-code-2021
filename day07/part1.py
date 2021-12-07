def importData():
    with open('input.txt') as input_file:
        inputDataArray = input_file.readlines()
    return inputDataArray

def calculateMinFuelSpend(inputDataArray):

    cleanInputArray = []

    for line in inputDataArray:
        if (line[-1] == '\n'):
            cleanInputArray.append(line[:-1])
        else:
            cleanInputArray.append(line)

    days = 80

    linesplit = inputDataArray[0].split(',')

    crabs = []

    for value in linesplit:
        crabs.append(int(value))
    
    min = 0
    max = 0

    for crab in crabs:
        if(crab > max):
            max = crab
        elif(crab<min):
            min = crab
    
    minfuel = 10000000000

    for x in range(min,max):
        totalfuel = 0
        for crab in crabs:
            totalfuel += abs(x-crab)
        
        if (totalfuel < minfuel):
            minfuel = totalfuel
    
    return minfuel

    
        
if __name__ == '__main__':
    print(calculateMinFuelSpend(importData()))
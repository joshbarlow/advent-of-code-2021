def importData():
    with open('input.txt') as input_file:
        inputDataArray = input_file.readlines()
    return inputDataArray

def calculatePopulation(inputDataArray, days):

    cleanInputArray = []

    for line in inputDataArray:
        if (line[-1] == '\n'):
            cleanInputArray.append(line[:-1])
        else:
            cleanInputArray.append(line)

    #days = 256

    linesplit = inputDataArray[0].split(',')

    ########################################

    lanternFishArray = [0,0,0,0,0,0,0,0,0,0]

    for value in linesplit:
        lanternFishArray[int(value)] +=1

    newFish = 0

    for day in range(days):

        workingFishArray = lanternFishArray

        newFish = lanternFishArray[0]

        #print( 'number of 0s: ' + str(workingFishArray[0]))

        for y in range(len(workingFishArray)-1):
            #print('element: ' + str(y))
            lanternFishArray[y] = workingFishArray[y+1]

        lanternFishArray[8] = newFish
        lanternFishArray[6] += newFish

        lanternFishArray

        fishString = ''
        for z in lanternFishArray:
            fishString += str(z) + ','
        #print('Day ' + str(day) + ': ' + str(fishString))
        
    total = 0

    for x in lanternFishArray:
        total += x

    return total
            
if __name__ == '__main__':
    print(calculatePopulation(importData(),256))
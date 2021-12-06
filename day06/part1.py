def importData():
    with open('input.txt') as input_file:
        inputDataArray = input_file.readlines()
    return inputDataArray

def calculatePopulation(inputDataArray):

    cleanInputArray = []

    for line in inputDataArray:
        if (line[-1] == '\n'):
            cleanInputArray.append(line[:-1])
        else:
            cleanInputArray.append(line)

    days = 80

    linesplit = inputDataArray[0].split(',')

    lanternFishArray = []

    for value in linesplit:
        lanternFishArray.append(lanternFish(int(value)))

    for x in range(days):
        workingFishArray = lanternFishArray

        #arrayStr = ''
        #for x in workingFishArray:
        #    arrayStr += str(x.time())
        ##print('Day ' + str(x) + arrayStr)

        for fish in workingFishArray:
            if (fish.increment()):
                lanternFishArray.append(lanternFish(9))

    return len(lanternFishArray)


class lanternFish:

    def __init__(self, timer):
        self.timer = timer
    
    def increment(self):
        if (self.timer == 0):
            self.timer = 6
            return True
        else:
            self.timer -= 1
    
    def time(self):
        return self.timer
    
        
if __name__ == '__main__':
    print(calculatePopulation(importData()))
def importData():
    with open('input.txt') as input_file:
        inputDataArray = input_file.readlines()
    return inputDataArray

def calculateOverlaps(inputDataArray):

    cleanInputArray = []

    plotDict = {}

    for line in inputDataArray:
        if (line[-1] == '\n'):
            cleanInputArray.append(line[:-1])
        else:
            cleanInputArray.append(line)
    
    lineArray = []

    for line in cleanInputArray:
        lineArray.append(lineObject(line))
    
    for lineObj in lineArray:
        for point in lineObj.listPoints():
            if point in plotDict:
                plotDict[point] += 1
            else:
                plotDict[point] = 1
    
    for ket in plotDict:
        print(key)

    

class lineObject:

    def __init__(self, lineInfo):

        splitPts = lineInfo.split(' -> ')
        ptA = splitPts[0].split(',')
        ptB = splitPts[1].split(',')

        self.x1 = int(ptA[0])
        self.y1 = int(ptA[1])
        self.x2 = int(ptB[0])
        self.y2 = int(ptB[1])

        self.pointList = []

        if (self.x1 == self.x2):
            if ()
        else if (self.y1 == self.y2):
            print('aaa')
    
    def listPoints(self):
        print('aaa')


    


        
if __name__ == '__main__':
    print(calculateWinningBoard(importData()))
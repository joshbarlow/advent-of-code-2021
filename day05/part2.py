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
    
    count = 0

    for key in plotDict:
        if (plotDict[key] > 1):
            count += 1
    
    return count

    

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
            if (self.y1 < self.y2):
                current = self.y1
                while (current < self.y2 + 1):
                    self.pointList.append(str(self.x1) + ',' + str(current))
                    current += 1
            elif (self.y2 < self.y1):
                current = self.y2
                while (current < self.y1 + 1):
                    self.pointList.append(str(self.x1) + ',' + str(current))
                    current += 1

        elif (self.y1 == self.y2):
            if (self.x1 < self.x2):
                current = self.x1
                while (current < self.x2 + 1):
                    self.pointList.append(str(current) + ',' + str(self.y1))
                    current += 1
            elif (self.x2 < self.x1):
                current = self.x2
                while (current < self.x1 + 1):
                    self.pointList.append(str(current) + ',' + str(self.y1))
                    current += 1
        ## diagonal
        else:
            Yincrement = 1
            Xincrement = 1

            if (self.x1 > self.x2):
                Xincrement = -1
            if (self.y1 > self.y2):
                Yincrement = -1
                
            currentX = self.x1
            currentY = self.y1
            while (currentX != self.x2):
                self.pointList.append(str(currentX) + ',' + str(str(currentY)))
                currentX += Xincrement
                currentY += Yincrement

            self.pointList.append(str(self.x2) + ',' + str(self.y2))

    
    def listPoints(self):
        return self.pointList


    


        
if __name__ == '__main__':
    print(calculateOverlaps(importData()))
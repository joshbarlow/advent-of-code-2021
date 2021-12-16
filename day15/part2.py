import copy, string

def importData():
    with open('input.txt') as input_file:
        inputDataArray = input_file.readlines()
    return inputDataArray

def calculateShortestPath(inputDataArray):

    cleanInputArray = []

    for line in inputDataArray:
        if (line[-1] == '\n'):
            cleanInputArray.append(line[:-1])
        else:
            cleanInputArray.append(line)
    
    nodeList = []

    for lineNum in range(len(cleanInputArray)):
        new4Lines = cleanInputArray[lineNum]
        for x in range(4):
            newLine = ''
            lineList = list(cleanInputArray[lineNum])
            for z in lineList:
                intWrangle = int(z) + (x+1)
                if(intWrangle>9):
                    intWrangle = intWrangle - 9
                newLine += str(intWrangle)
            new4Lines += newLine
        cleanInputArray[lineNum] = new4Lines
    
    cleanInputArrayCopy = copy.deepcopy(cleanInputArray)

    for x in range(4):
        for lineNum in range(len(cleanInputArrayCopy)):
            newLine = ''
            lineList = list(cleanInputArrayCopy[lineNum])
            for z in lineList:
                intWrangle = int(z) + (x+1)
                if(intWrangle>9):
                    intWrangle = intWrangle - 9
                newLine += str(intWrangle)
            cleanInputArray.append(newLine)

    for y in range(len(cleanInputArray)):
        # print(cleanInputArray[y])
        for x in range(len(cleanInputArray[0])):
            nodeList.append(node(cleanInputArray[y][x],x,y,len(cleanInputArray[0]),len(cleanInputArray)))
    
    # print(len(nodeList))
    for x in nodeList:
        if(x.id == 0):
            x.pathCost = 0
            x.active = True
    
    count = 0
    lock = True
    FinalCost = 0

    activeNodes = [0]

    while lock:

        lowestActiveNode = -1
        lowestActiveRisk = 100000

        for x in activeNodes:
            if(nodeList[x].active == True):
                if(nodeList[x].pathCost < lowestActiveRisk):
                    lowestActiveNode = nodeList[x].id
                    lowestActiveRisk = nodeList[x].pathCost
                # print(f"{x.id} - {x.neighbours}")

        # this was too slowwww

        # for x in nodeList:
        #     if(x.active == True):
        #         if(x.pathCost < lowestActiveRisk):
        #             lowestActiveNode = x.id
        #             lowestActiveRisk = x.pathCost
        
        for nNode in nodeList[lowestActiveNode].neighbours:
            neighbourCurrentCost = nodeList[nNode].pathCost
            neighbourNodeRisk = nodeList[nNode].risk
            activePathCost = nodeList[lowestActiveNode].pathCost
            if(neighbourCurrentCost > activePathCost + neighbourNodeRisk):
                nodeList[nNode].pathCost = activePathCost + neighbourNodeRisk
                nodeList[nNode].previousNode = lowestActiveNode
                nodeList[nNode].active = True
                activeNodes.append(nodeList[nNode].id)
            
            if(nodeList[nNode].id == (len(nodeList) - 1)):
                # print('Found Path')
                # print(f"Cost is {nodeList[nNode].pathCost}")
                FinalCost = nodeList[nNode].pathCost
                lock = False
        
        # print(f"LowestActive = {lowestActiveNode}")
        
        nodeList[lowestActiveNode].active = False
        activeNodes.remove(nodeList[lowestActiveNode].id)

        count += 1
    
    return FinalCost
    
class node:

    def __init__(self, risk, x, y, lenX, lenY):
        
        self.x = x
        self.y = y
        self.risk = int(risk)

        self.pathCost = 100000000
        self.previousNode = -1
        self.active = False

        self.id = idGen(x,y,lenX)

        self.neighbours = []

        if(self.x > 0):
            self.neighbours.append(idGen(x-1,y,lenX))
        if(self.x < lenX-1):
            self.neighbours.append(idGen(x+1,y,lenX))
        if(self.y > 0):
            self.neighbours.append(idGen(x,y-1,lenX))
        if(self.y < lenY-1):
            self.neighbours.append(idGen(x,y+1,lenX))

def idGen(x,y,lenX):
    return x + (y*lenX)

if __name__ == '__main__':
    print(calculateShortestPath(importData()))
def importData():
    with open('input.txt') as input_file:
        inputDataArray = input_file.readlines()
    return inputDataArray

def calculateSyntaxError(inputDataArray):

    cleanInputArray = []

    for line in inputDataArray:
        if (line[-1] == '\n'):
            cleanInputArray.append(line[:-1])
        else:
            cleanInputArray.append(line)
    
    scoreDict = {'(':1,'[':2,'{':3,'<':4}
    syntaxError = 0
    lineScores = []
    
    for line in cleanInputArray:
        illegal = findIllegalCharacter(line)
        score = 0
        if(len(illegal) > 0):
            illegal.reverse()
            for x in illegal:
                score = score * 5
                score += scoreDict[x]
            lineScores.append(score)

    lineScores.sort()

    middleIndex = int((len(lineScores)-1)/2)

    return lineScores[middleIndex]

def findIllegalCharacter(line):
    matchingPairs = {'{':'}','(':')','[':']','<':'>'}
    reverseMatching = {'}':'{',')':'(',']':'[','>':'<'}
    openArray = []

    lineList = list(line)

    for x in lineList:
        if x in matchingPairs.keys():
            openArray.append(x)
        else:
            if(len(openArray) == 0):
                return []
            if(openArray[-1] == reverseMatching[x]):
                del openArray[-1]
            else:
                #print(openArray)
                #print('illegal: ' + x)
                return []
    
    #print('ok')
    return openArray

if __name__ == '__main__':
    print(calculateSyntaxError(importData()))
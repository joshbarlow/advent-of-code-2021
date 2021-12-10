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
    
    scoreDict = {')':3,']':57,'}':1197,'>':25137,'0':0}
    syntaxError = 0
    
    for line in cleanInputArray:
        syntaxError += scoreDict[findIllegalCharacter(line)]

    return syntaxError

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
                return x
            if(openArray[-1] == reverseMatching[x]):
                del openArray[-1]
            else:
                #print(openArray)
                #print('illegal: ' + x)
                return x
    
    #print('ok')
    return '0'

if __name__ == '__main__':
    print(calculateSyntaxError(importData()))
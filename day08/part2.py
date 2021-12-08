def importData():
    with open('input.txt') as input_file:
        inputDataArray = input_file.readlines()
    return inputDataArray

def calculateOutput(inputDataArray):

    cleanInputArray = []

    for line in inputDataArray:
        if (line[-1] == '\n'):
            cleanInputArray.append(line[:-1])
        else:
            cleanInputArray.append(line)

    finalTotal = 0

    for line in cleanInputArray:
        linesplit = line.split('|')
        refSplit = linesplit[0].split()

        refList = [''] * 10

        refDict = {}

        for x in refSplit:
            #1
            if (len(x) == 2):
                refList[1] = x
            #4
            if (len(x) == 4):
                refList[4] = x
            #7
            if (len(x) == 3):
                refList[7] = x
            #8
            if (len(x) == 7):
                refList[8] = x
        
        #9
        for x in refSplit:
            if (x not in refList):
                if (matches(x,refList[4])):
                    refList[9] = x
        
        #6 + 0
        for x in refSplit:
            if (x not in refList):
                if(len(x) == 6):
                    if (matches(x,refList[1])):
                        refList[0] = x
                    else:
                        refList[6] = x

        #3
        for x in refSplit:
            if (x not in refList):
                if (matches(x,refList[1])):
                    refList[3] = x

        #5 + 2
        for x in refSplit:
            if (x not in refList):
                if (matches(refList[9],x)):
                    refList[5] = x
                else:
                    refList[2] = x

        for x in range(len(refList)):
            refDict[refList[x]] = x

        lineNumber = ''

        outputSplit = linesplit[1].split()
        for digit in outputSplit:
            refdig = ''
            for dictDigit in refDict.keys():
                if(len(digit) == len(dictDigit)):
                    if(matches(digit, dictDigit)):
                        refdig = dictDigit
            lineNumber += str(refDict[refdig])
        
        finalTotal += int(lineNumber)
            
    return finalTotal

def matches(ref, new):
    splitRef = list(ref)
    splitNew = list(new)

    match = True

    for x in splitNew:
        if (x not in splitRef):
            match = False
    
    return match
        
if __name__ == '__main__':
    print(calculateOutput(importData()))
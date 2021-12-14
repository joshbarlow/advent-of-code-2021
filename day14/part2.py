import copy, string

def importData():
    with open('input.txt') as input_file:
        inputDataArray = input_file.readlines()
    return inputDataArray

def calculateSequence(inputDataArray):

    cleanInputArray = []

    for line in inputDataArray:
        if (line[-1] == '\n'):
            cleanInputArray.append(line[:-1])
        else:
            cleanInputArray.append(line)
    
    sequence = []
    rules = []

    for x in cleanInputArray:
        if('->' in x):
            rules.append(x.split(' -> '))
        elif(len(x)>0):
            sequence = (list(x))
    
    chars = list(string.ascii_uppercase)

    charsDict = {}
    for x in chars:
        charsDict[x] = 0
    
    for x in sequence:
        charsDict[x] += 1
    
    pairsDict = {}

    for rule in rules:
        pairsDict[rule[0]] = 0
    
    for x in range(len(sequence) - 1):
        combo = f"{sequence[x]}{sequence[x+1]}"
        pairsDict[combo] += 1

    rulesDict = {}

    outputsDict ={}

    for rule in rules:
        rulesDict[rule[0]] = rule[1]
    
    for rule in rules:
        outputsDict[rule[0]] = [rule[0][0] + rule[1], rule[1] + rule[0][1]]

    # print(pairsDict)

    # charsDict, pairsDict, rulesDict, outputsDict

    for x in range(40):
        # print(x)
        charsDict, pairsDict = sequenceInsert(charsDict, pairsDict, rulesDict, outputsDict)
    
    # print(sequence)

    values = []

    for key in charsDict.keys():
        if (charsDict[key] > 0):
            values.append(charsDict[key])
    
    # print(charsDict)
    values.sort()
    # print(values)
    
    return values[len(values)-1] - values[0]

def sequenceInsert(charsDict, pairsDict, rulesDict, outputsDict):

    newPairDict = copy.deepcopy(pairsDict)
    for key in newPairDict.keys():
        newPairDict[key] = 0

    for key in pairsDict.keys():
        if (pairsDict[key] > 0):
            # print(charsDict[rulesDict[key]])
            charsDict[rulesDict[key]] += pairsDict[key]
            for pair in outputsDict[key]:
                newPairDict[pair] += pairsDict[key]
            # print(key)

    
    return charsDict, newPairDict



if __name__ == '__main__':
    print(calculateSequence(importData()))
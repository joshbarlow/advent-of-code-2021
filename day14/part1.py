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
    
    # print(sequence)
    # print(rules)

    for x in range(10):
        # print(x)
        sequence = sequenceInsert(sequence,rules)
    
    # print(sequence)
    
    chars = list(string.ascii_uppercase)
    values = []
    for char in chars:
        if(sequence.count(char) > 0):
            values.append(sequence.count(char))

    values.sort()

    # print(values)

    return values[len(values)-1] - values[0]

def sequenceInsert(sequence,rules):

    seqLen = len(sequence)

    newSeq = ['0'] * ((seqLen*2)-1)
    # print(newSeq)
    
    for x in range(seqLen - 1):
        # print(f"{sequence[x]} {sequence[x+1]}")
        newChar = '0'
        combo = f"{sequence[x]}{sequence[x+1]}"
        for y in rules:
            if(y[0] == combo):
                newChar = y[1]
        # print((x*2)+1)
        newSeq[(x*2)+1] = newChar
    
    for x in range(seqLen):
        newSeq[(x*2)] = sequence[x]
    
    return newSeq



if __name__ == '__main__':
    print(calculateSequence(importData()))
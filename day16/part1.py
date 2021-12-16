import copy, string, hexToBin

def importData():
    with open('test_input.txt') as input_file:
        inputDataArray = input_file.readlines()
    return inputDataArray

def calculateShortestPath(inputDataArray):

    cleanInputArray = []

    for line in inputDataArray:
        if (line[-1] == '\n'):
            cleanInputArray.append(line[:-1])
        else:
            cleanInputArray.append(line)
    
    inputHex = cleanInputArray[0]
    inputBinary = hexToBin.convert(inputHex)

    # print(inputHex)
    # print(inputBinary)

    packets = splitPackets(inputBinary)

    versionSum = 0

    for x in packets:
        version = x[0:3]
        print(f"{version} - {int(version, 2)}")
        versionSum += int(version, 2)

    # print(packets)

    return versionSum

def splitPackets(inputBinary):

    binaryLen = len(inputBinary)-1
    binaryList = list(inputBinary)

    print(f"{binaryList} - {binaryLen}")

    currentBit = 0

    packets = []
    packetString = ''
    packetStart = True

    while(currentBit < binaryLen):
        if(packetStart == True):
            
            if((currentBit + 6) > binaryLen):
                break

            for x in range(6):
                print(f"{x} - {currentBit + x}")
                packetString += binaryList[currentBit + x]
            currentBit += 6
            print(currentBit)
            packetStart = False
        elif(packetStart == False):
            packetNumber = ''
            print(currentBit)
            for x in range(5):
                packetNumber += binaryList[currentBit + x]
            currentBit += 5
            print(packetNumber)
            if(packetNumber[0] == '1'):
                packetString += packetNumber
            if(packetNumber[0] == '0'):
                packetString += packetNumber
                packets.append(packetString)
                packetString = ''
                packetStart = True
    
    return packets

if __name__ == '__main__':
    print(calculateShortestPath(importData()))
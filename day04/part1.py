def importData():
    with open('input.txt') as input_file:
        inputDataArray = input_file.readlines()
    return inputDataArray

def calculateWinningBoard(inputDataArray):

    cleanInputArray = []

    for line in inputDataArray:
        if (line[-1] == '\n'):
            cleanInputArray.append(line[:-1])
        else:
            cleanInputArray.append(line)
    
    numbers = cleanInputArray[0].split(',')
    
    numBoards = int((len(cleanInputArray) - 1)/6)

    boards = []

    for x in range(numBoards):
        boardNumArray = []
        for y in range(5):
            lineNum = 2 + (x * 6) + y
            lineSplit = inputDataArray[lineNum].split()
            for num in lineSplit:
                boardNumArray.append(int(num))
        
        boards.append(bingoBoard(boardNumArray))

    return getWinningBoard(numbers, boards)
    

def getWinningBoard(numbers, boards):
    for x in numbers:
        for board in boards:
            board.addNumber(int(x))
            if (board.checkWin()):
                print('winner found')
                print(board.getUnmarkedTotal())
                print(x)
                return board.getUnmarkedTotal() * int(x)

class bingoBoard:

    def __init__(self, boardArray):
        self.boardNumArray = boardArray
        self.boardWinArray = [0] * 25

    
    def addNumber(self,inputNumber):
        for x in range(25):
            if (self.boardNumArray[x] == inputNumber):
                self.boardWinArray[x] = 1

    def checkWin(self):
        #check rows
        for x in range(5):
            count = 0
            for y in range(5):
                position = (x * 5) + y
                if(self.boardWinArray[position] == 1):
                    count += 1
            if (count == 5):
                return True
        
        #check columns
        for x in range(5):
            count = 0
            for y in range(5):
                position = (y * 5) + x
                if(self.boardWinArray[position] == 1):
                    count += 1
            if (count == 5):
                return True
        
        return False
    
    def getUnmarkedTotal(self):
        total = 0
        for x in range(25):
            if (self.boardWinArray[x] == 0):
                total += self.boardNumArray[x]
        return total
    
    def printBoard(self):
        boardWinArray = self.boardWinArray
        print(str(boardWinArray[0]) + str(boardWinArray[1]) + str(boardWinArray[2]) + str(boardWinArray[3]) + str(boardWinArray[4]))
        print(str(boardWinArray[5]) + str(boardWinArray[6]) + str(boardWinArray[7]) + str(boardWinArray[8]) + str(boardWinArray[9]))
        print(str(boardWinArray[10]) + str(boardWinArray[11]) + str(boardWinArray[12]) + str(boardWinArray[13]) + str(boardWinArray[14]))
        print(str(boardWinArray[15]) + str(boardWinArray[16]) + str(boardWinArray[17]) + str(boardWinArray[18]) + str(boardWinArray[19]))
        print(str(boardWinArray[20]) + str(boardWinArray[21]) + str(boardWinArray[22]) + str(boardWinArray[23]) + str(boardWinArray[24]))
        print(' ')


        
if __name__ == '__main__':
    print(calculateWinningBoard(importData()))
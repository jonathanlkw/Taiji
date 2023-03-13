class Game:
    def __init__(self):
        self.__board = [[0 for x in range(9)] for y in range(9)]
        self.__tiles = []
        self.__player = 0

    def setBoard(self, board):
        self.__board = board

    def setTiles(self, tiles):
        self.__tiles = tiles

    def setPlayer(self, player):
        self.__player = player

    def isTerminal(self):
        for i in range(len(self.__board)):
            for j in range(len(self.__board)-1):
                if self.__board[i][j] == 0 and self.__board[i][j+1] == 0:
                    return False
        for i in range(len(self.__board)-1):
            for j in range(len(self.__board)):
                if self.__board[i][j] == 0 and self.__board[i+1][j] == 0:
                    return False
        return True

    def checkValidMove(self, tileRep):
        pos_x = tileRep[0]
        pos_y = tileRep[1]
        orientation = tileRep[2]

        if orientation == 0:
            isXWithinRange = pos_x >= 0 and pos_x < 9
            isYWithinRange = pos_y >= 0 and pos_y < 8
            isUnoccupied = self.board[pos_x][pos_y] == 0 and self.board[pos_x][pos_y+1] == 0
            return isXWithinRange and isYWithinRange and isUnoccupied
        elif orientation == 1:
            isXWithinRange = pos_x >= 0 and pos_x < 8
            isYWithinRange = pos_y >= 0 and pos_y < 9
            isUnoccupied = self.board[pos_x][pos_y] == 0 and self.board[pos_x+1][pos_y] == 0
            return isXWithinRange and isYWithinRange and isUnoccupied
        elif orientation == 2:
            isXWithinRange = pos_x >= 0 and pos_x < 9
            isYWithinRange = pos_y >= 1 and pos_y < 9
            isUnoccupied = self.board[pos_x][pos_y] == 0 and self.board[pos_x][pos_y-1] == 0
            return isXWithinRange and isYWithinRange and isUnoccupied
        elif orientation == 3:
            isXWithinRange = pos_x >= 1 and pos_x < 9
            isYWithinRange = pos_y >= 0 and pos_y < 9
            isUnoccupied = self.board[pos_x][pos_y] == 0 and self.board[pos_x-1][pos_y] == 0
            return isXWithinRange and isYWithinRange and isUnoccupied
                
    def update(self, tileRep):
        if self.checkValidMove(tileRep):
            pos_x = tileRep[0]
            pos_y = tileRep[1]
            orientation = tileRep[2]
            self.__board[pos_x][pos_y] = 1
            if orientation == 0:
                self.__board[pos_x][pos_y+1] = 2
            elif orientation == 1:
                self.__board[pos_x+1][pos_y] = 2
            elif orientation == 2:
                self.__board[pos_x][pos_y-1] = 2
            elif orientation == 3:
                self.__board[pos_x-1][pos_y] = 2

    def __evaluateScore(self, pos_x, pos_y, player, score):
        '''
        searched = [[0 for x in range(9)] for y in range(9)]
        for i in range(len(self.__board)-1):
            for j in range(len(self.__board)-1):
                if searched[i][j] == 0 and self.board[i][j] != 0:
                    return
        '''
        if pos_x == 8:
            if pos_y == 8:
                if self.__board[pos_x][pos_y] == player:
                    return 1
                return 0
            
            
        

    def __str__(self):
        printedBoard = ""
        for i in range(len(self.__board)):
            printedBoard += str(self.__board[i])
            printedBoard += '\n'
        return printedBoard
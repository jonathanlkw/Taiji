import copy

NLARGESTGROUPS = 2

class Game:
    def __init__(self, board=[[0 for x in range(9)] for y in range(9)], tiles=[], player=1):
        self.board = copy.deepcopy(board)
        self.tiles = copy.deepcopy(tiles)
        self.player = player

    def setBoard(self, board):
        self.board = board

    def setTiles(self, tiles):
        self.tiles = tiles

    def setPlayer(self, player):
        self.player = player

    def getBoard(self):
        return self.board
    
    def getTiles(self):
        return self.tiles

    def getPlayer(self):
        return self.player

    def isTerminal(self):
        for i in range(len(self.board)):
            for j in range(len(self.board)-1):
                if self.board[i][j] == 0 and self.board[i][j+1] == 0:
                    return False
        for i in range(len(self.board)-1):
            for j in range(len(self.board)):
                if self.board[i][j] == 0 and self.board[i+1][j] == 0:
                    return False
        return True

    def checkValidMove(self, tileRep):
        pos_x = tileRep[0]
        pos_y = tileRep[1]
        orientation = tileRep[2]

        if orientation == 0:
            isXWithinRange = pos_x >= 0 and pos_x < 9
            isYWithinRange = pos_y >= 0 and pos_y < 8
            if isXWithinRange and isYWithinRange:
                isUnoccupied = self.board[pos_x][pos_y] == 0 and self.board[pos_x][pos_y+1] == 0
                return isUnoccupied
        elif orientation == 1:
            isXWithinRange = pos_x >= 0 and pos_x < 8
            isYWithinRange = pos_y >= 0 and pos_y < 9
            if isXWithinRange and isYWithinRange:
                isUnoccupied = self.board[pos_x][pos_y] == 0 and self.board[pos_x+1][pos_y] == 0
                return isUnoccupied
        elif orientation == 2:
            isXWithinRange = pos_x >= 0 and pos_x < 9
            isYWithinRange = pos_y >= 1 and pos_y < 9
            if isXWithinRange and isYWithinRange:
                isUnoccupied = self.board[pos_x][pos_y] == 0 and self.board[pos_x][pos_y-1] == 0
                return isUnoccupied
        elif orientation == 3:
            isXWithinRange = pos_x >= 1 and pos_x < 9
            isYWithinRange = pos_y >= 0 and pos_y < 9
            if isXWithinRange and isYWithinRange:
                isUnoccupied = self.board[pos_x][pos_y] == 0 and self.board[pos_x-1][pos_y] == 0
                return isUnoccupied
        return False
                
    def update(self, tileRep):
        if self.checkValidMove(tileRep):
            pos_x = tileRep[0]
            pos_y = tileRep[1]
            orientation = tileRep[2]
            self.board[pos_x][pos_y] = 1
            if orientation == 0:
                self.board[pos_x][pos_y+1] = 2
            elif orientation == 1:
                self.board[pos_x+1][pos_y] = 2
            elif orientation == 2:
                self.board[pos_x][pos_y-1] = 2
            elif orientation == 3:
                self.board[pos_x-1][pos_y] = 2
            self.player = 3 - self.player
        else:
            print("Invalid move, please try again")

    def calcGroupSize(self, pos_x, pos_y, player, searched):
        isConnected = self.board[pos_x][pos_y] == player
        if isConnected == 0:
            return 0
        else:
            searched[pos_x][pos_y] = 1
            if pos_x == 8:
                if pos_y == 8:
                    return 1
                return 1 + self.calcGroupSize(pos_x, pos_y+1, player, searched)
            elif pos_y == 8:
                return 1 + self.calcGroupSize(pos_x+1, pos_y, player, searched)
            else:
                return self.calcGroupSize(pos_x+1, pos_y, player, searched) + self.calcGroupSize(pos_x, pos_y+1, player, searched)
            
    def generateScoreList(self, player):
        searched = [[0 for x in range(9)] for y in range(9)]
        scoreList = []
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if searched[i][j] == 0 and self.board[i][j] != 0:
                    score = self.calcGroupSize(i, j, player, searched)
                    scoreList.append(score)
        scoreList.sort(reverse=True)
        return scoreList

    def calculateScore(self, p1_scoreList, p2_scoreList):
        p1_score = 0
        p2_score = 0
        for i in range(NLARGESTGROUPS):
            p1_score += p1_scoreList[i]
            p2_score += p2_scoreList[i]
        return [p1_score, p2_score]
    
    def evaluateWinner(self, scores):
        if scores[0] > scores[1]:
            return 1
        elif scores [0] < scores[1]:
            return 2
        else:
            return 0

    def __str__(self):
        printedBoard = ""
        for i in range(len(self.board)):
            printedBoard += str(self.board[i])
            printedBoard += '\n'
        return printedBoard
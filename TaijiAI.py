from Game import *
from Tile import *
import random
import numpy as np
import math

NITERATIONS = 100000
UCT_CONSTANT = 1
LOG_BASE = 10

def enumeratePossibleMoves(game):
    possibleMoves = []
    for i in range(9):
        for j in range(9):
            for o in range(4):
                if o == 0:
                    isXWithinRange = i >= 0 and i < 9
                    isYWithinRange = j >= 0 and j < 8
                    if isXWithinRange and isYWithinRange:
                        isUnoccupied = game.board[i][j] == 0 and game.board[i][j+1] == 0
                        if isUnoccupied:
                            possibleMoves.append(Tile(i, j, o))
                elif o == 1:
                    isXWithinRange = i >= 0 and i < 8
                    isYWithinRange = j >= 0 and j < 9
                    if isXWithinRange and isYWithinRange:
                        isUnoccupied = game.board[i][j] == 0 and game.board[i+1][j] == 0
                        if isUnoccupied:
                            possibleMoves.append(Tile(i, j, o))
                elif o == 2:
                    isXWithinRange = i >= 0 and i < 9
                    isYWithinRange = j >= 1 and j < 9
                    if isXWithinRange and isYWithinRange:
                        isUnoccupied = game.board[i][j] == 0 and game.board[i][j-1] == 0
                        if isUnoccupied:
                            possibleMoves.append(Tile(i, j, o))
                elif o == 3:
                    isXWithinRange = i >= 1 and i < 9
                    isYWithinRange = j >= 0 and j < 9
                    if isXWithinRange and isYWithinRange:
                        isUnoccupied = game.board[i][j] == 0 and game.board[i-1][j] == 0
                        if isUnoccupied:
                            possibleMoves.append(Tile(i, j, o))
    return possibleMoves

def pickRandomMove(possibleMoves):
    moveIndex = random.randint(0, len(possibleMoves)-1)
    return moveIndex

def makeRandomMove(game):
    tile = Tile(random.randint(0,8), random.randint(0,8), random.randint(0,3))
    while not(game.checkValidMove(tile.getRepresentation())):
        tile = Tile(random.randint(0,8), random.randint(0,8), random.randint(0,3))
    return tile

class Node:
    def __init__(self, game, parent=None, tile=None):
        self.parent = parent
        self.children = []
        self.score = 0
        self.played = 0
        self.game = Game(game.getBoard(), game.getTiles(), game.getPlayer())
        self.tile = tile

    def addChild(self):
        possibleMoves = enumeratePossibleMoves(self.game)
        moveIndex = pickRandomMove(possibleMoves)
        tile = possibleMoves[moveIndex]
        newGame = Game(self.game.getBoard(), self.game.getTiles(), self.game.getPlayer())
        newGame.update(tile.getRepresentation())
        child = Node(newGame, self, tile)
        self.children.append(child)
        return child
        
# main function for the Monte Carlo Tree Search
def MCTS(startNode):
    N = NITERATIONS
    while isResourceLeft(N):
        selectedChild = select(startNode)
        if selectedChild.game.isTerminal():
            return selectedChild.tile
        newLeaf = expand(selectedChild)
        if newLeaf.game.isTerminal():
            return newLeaf.tile
        simulationResult = simulate(newLeaf)
        backPropagate(newLeaf, simulationResult)
        N -= 1
    print(bestChild(startNode).tile.getRepresentation())
    return bestChild(startNode).tile
 
# function for selection of best leaf
def traverse(parent, uctList, nodeList):
    uctList.append(calcUCT(parent))
    nodeList.append(parent)

    if len(parent.children) != 0:
        for node in parent.children:
            uctList.append(calcUCT(node))
            nodeList.append(node)
            traverse(node, uctList, nodeList)
    return

def select(node):
    uctList = []
    nodeList = []
    traverse(node, uctList, nodeList)
    maxIndex = np.argmax(uctList)
    return nodeList[maxIndex]

# function for the result of the simulation
def expand(node):
    return node.addChild()

# function for randomly selecting a child node
def simulate(node):
    # return win or lose of the game
    notSimEnded = True
    duplicateGame = Game(node.game.board, node.game.tiles, node.game.player)
    while (notSimEnded):
        possibleMoves = enumeratePossibleMoves(duplicateGame)
        moveIndex = pickRandomMove(possibleMoves)
        tile = possibleMoves[moveIndex]
        duplicateGame.update(tile.getRepresentation())
        notSimEnded = not duplicateGame.isTerminal()
    p1_scoreList = duplicateGame.generateScoreList(1)
    p2_scoreList = duplicateGame.generateScoreList(2)
    finalScores = duplicateGame.calculateScore(p1_scoreList, p2_scoreList)
    winner = duplicateGame.evaluateWinner(finalScores)
    return winner
 
# function for backpropagation
def backPropagate(node, result):
    player = node.game.getPlayer
    if player == 1:
        if result == 1:
            node.score += 1
    elif player == 2:
        if result == 2:
            node.score += 1
    node.played += 1
    if node.parent == None:
        return
    else:
        backPropagate(node.parent, result)
 
# function for selecting the best child
def calcUCT(node):
    if node.parent != None:
        exploitation = node.score/node.played
        exploration = UCT_CONSTANT * math.sqrt(math.log(node.parent.played, LOG_BASE)/node.played)
        utility = exploitation + exploration
        return utility
    else:
        return 0

def bestChild(node):
    maxPlayout = 0
    selectedNode = None
    for child in node.children:
        if maxPlayout < child.played:
            maxPlayout = child.played
            selectedNode = child
    return selectedNode

def isResourceLeft(N):
    if N == 0:
        return False
    else:
        return True


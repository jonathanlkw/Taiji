from Game import *
from Tile import *
from TaijiAI import *
import multiprocessing

NUMTESTS = 10

lock = multiprocessing.Lock()

def updateCurrentNode(node, tile):
    for child in node.children:
        if child.tile == tile:
            return child
    return node.addSpecificChild(tile)

def simSingleGame(i):
    print(f"Running game {i+1}")

    if i < NUMTESTS*0.5:
        playerToStart = 1
    else: 
        playerToStart = 2

    game = Game()
    notGameEnded = True
    game.setPlayer(int(playerToStart))

    rootNode = Node(game)
    currentNode = rootNode

    while (notGameEnded):
        if game.getPlayer() == 1:
            possibleMoves = enumeratePossibleMoves(game, currentNode.tile)
            moveIndex = pickRandomMove(possibleMoves)
            tile = possibleMoves[moveIndex]
            game.update(tile.getRepresentation())
            currentNode = updateCurrentNode(currentNode, tile)
            notGameEnded = not game.isTerminal()
            
        elif game.getPlayer() == 2:
            newTile = MCTS(currentNode)
            game.update(newTile.getRepresentation())
            currentNode = updateCurrentNode(currentNode, newTile)
            notGameEnded = not game.isTerminal()
            #print(f"Game {i+1}")
            #print(game)

    lock.acquire()
    print("\n")
    print(f"Game {i+1}")
    print(game)
    p1_scoreList = game.generateScoreList(1)
    print(f"Game {i+1} p1_scoreList: {p1_scoreList}")
    p2_scoreList = game.generateScoreList(2)
    print(f"Game {i+1} AI_scoreList: {p2_scoreList}")
    lock.release()
    finalScores = game.calculateScore(p1_scoreList, p2_scoreList)
    winner = game.evaluateWinner(finalScores)
    return winner

if __name__ == "__main__":

    winCount = 0
    drawCount = 0
    loseCount = 0

#     for i in range (NUMTESTS):
#         print(f"Running game {i+1}")

#         if i < NUMTESTS*0.5:
#             playerToStart = 1
#         else: 
#             playerToStart = 2

#         game = Game()
#         notGameEnded = True
#         game.setPlayer(int(playerToStart))

#         rootNode = Node(game)
#         currentNode = rootNode

#         while (notGameEnded):
#             if game.getPlayer() == 1:
#                 possibleMoves = enumeratePossibleMoves(game, currentNode.tile)
#                 moveIndex = pickRandomMove(possibleMoves)
#                 tile = possibleMoves[moveIndex]
#                 game.update(tile.getRepresentation())
#                 currentNode = updateCurrentNode(currentNode, tile)
#                 notGameEnded = not game.isTerminal()
                
#             elif game.getPlayer() == 2:
#                 newTile = MCTS(currentNode)
#                 game.update(newTile.getRepresentation())
#                 currentNode = updateCurrentNode(currentNode, newTile)
#                 notGameEnded = not game.isTerminal()

#         print(game)
#         p1_scoreList = game.generateScoreList(1)
#         print(f"p1_scoreList: {p1_scoreList}")
#         p2_scoreList = game.generateScoreList(2)
#         print(f"p2_scoreList: {p2_scoreList}")
#         finalScores = game.calculateScore(p1_scoreList, p2_scoreList)
#         winner = game.evaluateWinner(finalScores)
#         if winner == 0:
#             drawCount += 1
#         elif winner == 1:
#             loseCount += 1 #From AI perspective
#         else:
#             winCount += 1 #From AI perspective
    
    with multiprocessing.Pool() as pool:
        for result in pool.map(simSingleGame, range(NUMTESTS)):
            if result == 0:
                drawCount += 1
            elif result == 1:
                loseCount += 1 #From AI perspective
            else:
                winCount += 1 #From AI perspective

    winRate = winCount / NUMTESTS
    drawRate = drawCount / NUMTESTS
    loseRate = loseCount / NUMTESTS
    print("\n")
    print(f"AI Win Rate: {winRate}")
    print(f"Draw Rate: {drawRate}")
    print(f"AI Lose Rate: {loseRate}")

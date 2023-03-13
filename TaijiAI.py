from Game import *
from Tile import *
import random

def taijiAI(game):
    tile = Tile(random.randint(0,8), random.randint(0,8), random.randint(0,3))
    while not(game.checkValidMove(tile.getRepresentation())):
                tile = Tile(random.randint(0,8), random.randint(0,8), random.randint(0,3))
    return tile

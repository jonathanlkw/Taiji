from Game import *
from Tile import *
import random

def taijiAI(game):
    tile = Tile(random.randint(0,8), random.randint(0,8), random.randint(0,3))
    while not(game.checkValidMove(tile.getRepresentation())):
                tile = Tile(random.randint(0,8), random.randint(0,8), random.randint(0,3))
    return tile

Class Node:
    def _init_(self):
        self.parent=None
        self.child=[]
        self.win=0
        self.played=0
        self.state=[[],[],[]]

root=Node()
# add node function to add children to the node,

def add_node(parent, child):
    parent.child.append(child)
    return parent 

    
# main function for the Monte Carlo Tree Search
def monte_carlo_tree_search(root):
     
    while resources_left(time, computational power):
        leaf = select(root)
        new_child=expand(leaf)
        simulation_result = simulate(new_child)
        backpropagate(leaf, simulation_result)
         
    return best_child(root)
 
# function for selection of best leaf
def select(node):
    while fully_expanded(node):
        node = best_uct(node)
        node = worst_uct(node)
         
    # in case no children are present / node is terminal
    return pick_unvisited(node.children) or leaf
 
# function for the result of the simulation
def expand(leaf):
    new_child=Node()
    new_child.parent=leaf
    # the random move generate a random valid next move, and add that game state to the node
    new_child.state=random_move(new_child)
    return new_child
 
# function for randomly selecting a child node
def simulate(new_child):
    # return win or lose of the game
    
    return random_game(new_child)
 
# function for backpropagation
def backpropagate(node, result):
    if is_root(node) return
    node.stats = update_stats(node, result)
    backpropagate(node.parent)
 
# function for selecting the best child
def best_uct(node):
    highest=0
    best_child=None
    for i in node.children:
        exploitation=node.win/node.played
        exploration=C*math.sqrt(node.parent.played/node.played)
        utility=exploitation+exploration
        if utility>highest:
            highest=utility
            best_child=i
    return i
# function for selecting the worst uct
def worst_uct(node):
    highest=0
    best_child=None
    for i in node.children:
        exploitation=node.win/node.played
        exploration=C*math.sqrt(node.parent.played/node.played)
        utility=exploitation+exploration
        if utility>highest:
            highest=utility
            best_child=i
    return i

def best_child(root)

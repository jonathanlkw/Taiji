from Game import *
from Tile import *
from TaijiAI import *
from tkinter import *
from tkinter import ttk

NLARGESTGROUPS = 2
BOARDSIZE = 9

def parseMove(pos_x, pos_y, o):
    moveList = []
    try:
        moveList[0] = int(pos_x)
        moveList[1] = int(pos_y)
        moveList[2] = int(o)
    except:
        print("Invalid input, please try again")
    return moveList

if __name__ == "__main__":
    root = Tk()
    root.title("Taiji")
    buttons = [[0 for x in range(9)] for y in range(9)]
    frm = ttk.Frame(root, padding=10)
    frm.grid()

    style = ttk.Style()
    style.map("C.TButton", foreground=[('pressed', 'white'), ('active', 'beige')], background=[('pressed', 'beige'), ('active', 'beige')])
    for i in range(BOARDSIZE):
        for j in range(BOARDSIZE):
            buttons[i][j] = ttk.Button(frm, style="C.TButton", width=4, command = lambda pos_x=i, pos_y=j, o=0 : parseMove(pos_x, pos_y, o))
            buttons[i][j].grid(row = i, column = j)
    
    root.mainloop()
  
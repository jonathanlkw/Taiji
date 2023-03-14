class Tile:
    def __init__(self, pos_x, pos_y, orientation):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.orientation = orientation

    def getPos_x(self):
        return self.pos_x

    def getPos_y(self):
        return self.pos_y

    def getOrientation(self):
        return self.orientation

    def getRepresentation(self):
        return [self.pos_x, self.pos_y, self.orientation]
    
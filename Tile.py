class Tile:
    def __init__(self, pos_x, pos_y, orientation):
        self.__pos_x = pos_x
        self.__pos_y = pos_y
        self.__orientation = orientation

    def getPos_x(self):
        return self.__pos_x

    def getPos_y(self):
        return self.__pos_y

    def getOrientation(self):
        return self.__orientation

    def getRepresentation(self):
        return [self.__pos_x, self.__pos_y, self.__orientation]
    
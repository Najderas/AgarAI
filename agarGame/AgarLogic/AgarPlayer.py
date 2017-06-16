__author__ = 'Grzegorz'


class AgarPlayer:
    def __init__(self, pos_x=-1, pos_y=-1):
        self.x = pos_x
        self.y = pos_y
        self.radius = 1


    def isActive(self):
        if self.x < 0 or self.y < 0:
            return False
        return True

    def setX(self, x):
        """ should be called from AgarBoard """     #TODO: surely?
        self.x = x

    def setY(self, y):
        """ should be called from AgarBoard """     #TODO: surely?
        self.y = y


__author__ = 'Grzegorz'

import random
import math

class AgarPlayer:
    def __init__(self, pos_x=-1, pos_y=-1):
        self.x = pos_x
        self.y = pos_y
        self.mass = 2 + random.randint(0, 3)
        self.radius = 1
        self.movement_vector = [0, 0]

        ######### CONSTANTS ############
        self.negativeRevardForBeingEaten = -500
        self.logCollisions = True
        ###########################


    def isActive(self):
        if self.x < 0 or self.y < 0:
            return False
        return True

    def deactivate(self):
        self.x = -1
        self.y = -1

    def makeDecision(self, neighbours):

        # example random decision
        self.movement_vector[0] = random.random()*2 - 1
        # self.movement_vector[1] = math.sqrt(1 - self.movement_vector[0]*self.movement_vector[0])
        self.movement_vector[1] = random.random()*2 - 1

    # def setX(self, x):
    #     """ should be called from AgarBoard """     #TODO: surely?
    #     self.x = x
    #     # wanted to add sth here? The board is deciding if player collides and eats someone.
    #
    # def setY(self, y):
    #     """ should be called from AgarBoard """     #TODO: surely?
    #     self.y = y

    def isColliding(self, another_cell):
        dx = abs(self.x - another_cell.x)
        dy = abs(self.y - another_cell.y)
        if self.radius + another_cell.radius > math.sqrt(dx*dx + dy*dy):
            if self.logCollisions:
                print("Cell in ("+ str(self.x) + "," + str(self.y) + ") r=" + str(self.radius) + " collides cell (" + str(another_cell.x) + "," + str(another_cell.y) + ") r=" + str(another_cell.radius) )
            return True
        return False

    def calculateReward(self, reward):
        pass

    def eatenSth(self, cell):
        if self.logCollisions:
            print("Cell in ("+ str(self.x) + "," + str(self.y) + ") r=" + str(self.radius) + " ate cell (" + str(cell.x) + "," + str(cell.y) + ") r=" + str(cell.radius) )
        self.mass += cell.mass
        self.radius = math.sqrt(self.mass/math.pi)
        self.calculateReward(cell.mass)

    def haveBeenEaten(self):
        self.mass = 1
        self.calculateReward(self.negativeRevardForBeingEaten)







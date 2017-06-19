__author__ = 'Grzegorz'

import math
from .AgarPlayer import AgarPlayer

class AgarPlayer2(AgarPlayer):
    def makeDecision(self, neighbours):
        if not self.isActive():
            return

        # # example random decision
        # self.movement_vector[0] = random.random()*2 - 1
        # # self.movement_vector[1] = math.sqrt(1 - self.movement_vector[0]*self.movement_vector[0])
        # self.movement_vector[1] = random.random()*2 - 1

        print("self.x= ", self.x)
        print("neighbours: ", [(n.x, n.y) for n in neighbours])
        # max_l = reduce(lambda x, y: x if x>y else y, [ math.sqrt((n.x-self.x)*(n.x-self.x) + (n.y-self.y)*(n.y-self.y))  for n in neighbours])    # get max seen distance
        print( [ math.sqrt((n.x-self.x)*(n.x-self.x) + (n.y-self.y)*(n.y-self.y)) for n in neighbours])    # get max seen distance
        max_l = max( [ math.sqrt((n.x-self.x)*(n.x-self.x) + (n.y-self.y)*(n.y-self.y)) for n in neighbours] or [10, 0])    # get max seen distance


        for neighbour in neighbours:
            #             vov_v    =   dx scaled: near-strong, far-light)
            self.movement_vector[0] += ((max_l - (neighbour.x-self.x)) if (neighbour.x-self.x)>0 else ((-1)*max_l - (neighbour.x-self.x))) * (-1 if neighbour.mass > self.mass else 1)
            self.movement_vector[1] += ((max_l - (neighbour.y-self.y)) if (neighbour.y-self.y)>0 else ((-1)*max_l - (neighbour.y-self.y))) * (-1 if neighbour.mass > self.mass else 1)







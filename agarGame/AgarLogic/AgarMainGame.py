__author__ = 'Grzegorz'

import math

from .AgarPlayer import AgarPlayer
from .AgarBoard import AgarBoard

class AgarMainGame():
    def __init__(self, agarBoard):
        self.playersDecideEveryXRounds = 10
        self.agarBoard = agarBoard
        self.maxDistancePerFrame = 2.
        self.sqrt05 = math.sqrt(0.5)

        self.agarBoard.populateBoardWithPlayers()

    def calculateCellMovementDistancePerFrame(self, player):
        return self.maxDistancePerFrame * self.sqrt05 / math.sqrt(0.5 * player.mass)

    def askPlayersForDecisions(self):
        for player in self.agarBoard.players:
            player.makeDecision(self.agarBoard.getNeighboursForPlayer(player))

    def eatingTime(self, eater, eaten):
        self.agarBoard.removePlayer(eaten)
        eater.eatenSth(eaten)
        eaten.haveBeenEaten()
        self.agarBoard.addPlayer(eaten)

    def movePlayer(self, player):
        # damn you python, where are 2d vector calculations??
        # calculate direction
        dir_vector = player.movement_vector
        dir_vector_len = math.sqrt(dir_vector[0]*dir_vector[0] + dir_vector[1]*dir_vector[1])
        move_distance = self.calculateCellMovementDistancePerFrame(player)
        d = move_distance/dir_vector_len
        # move player
        self.agarBoard.movePlayerToPosition(player, player.x+dir_vector[0]*d, player.y+dir_vector[1]*d)
        # check collisions
        for neighbour in self.agarBoard.getNeighboursForPlayer(player):
            if player.isColliding(neighbour):
                if player.mass > neighbour.mass:
                    self.eatingTime(player, neighbour)
                else:
                    self.eatingTime(player, neighbour)


    def movePlayers(self):
        for player in self.agarBoard.players:
            self.movePlayer(player)

    def makeRound(self):
        self.askPlayersForDecisions()
        for i in range(self.playersDecideEveryXRounds):
            self.movePlayers()





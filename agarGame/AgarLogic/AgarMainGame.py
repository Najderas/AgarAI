__author__ = 'Grzegorz'

import math
import matplotlib.pyplot as plt

class AgarMainGame():
    def __init__(self, agarBoard):
        self.playersDecideEveryXRounds = 10
        self.agarBoard = agarBoard
        self.maxDistancePerFrame = 2.
        self.sqrt05 = math.sqrt(0.5)
        self.displayPlot = True

        self.agarBoard.populateBoardWithPlayers()

        if self.displayPlot:
            x = [player.x for player in self.agarBoard.players]
            y = [player.y for player in self.agarBoard.players]
            sizes = [player.mass for player in self.agarBoard.players]

            self.fig, self.ax = plt.subplots()
            self.ax.scatter(x, y, s=sizes)
            print(zip(x, y, sizes))
            self.ax.set_xlim(0, 1000)
            self.ax.set_ylim(0, 1000)

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

    def plotBoard(self):
        x = [player.x for player in self.agarBoard.players]
        y = [player.y for player in self.agarBoard.players]
        sizes = [player.mass for player in self.agarBoard.players]
        self.ax.cla()
        print(zip(x, y, sizes))
        self.ax.scatter(x, y, s=sizes)
        plt.pause(0.1)

    def makeRound(self):
        self.askPlayersForDecisions()
        for i in range(self.playersDecideEveryXRounds):
            self.movePlayers()
        if self.displayPlot:
            self.plotBoard()





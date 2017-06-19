import math
import matplotlib.pyplot as plt

class AgarMainGame():
    def __init__(self, agarBoard):
        self.agarBoard = agarBoard

        ######### CONSTANTS #########
        self.playersDecideEveryXRounds = 10
        self.maxDistancePerFrame = 2.
        self.displayPlot = True
        self.plotPauseInterval = 0.1
        #############################

        self.sqrt05 = math.sqrt(0.5)
        self.agarBoard.populateBoardWithPlayers()

        if self.displayPlot:
            self.fig, self.ax = plt.subplots()
            self.plotBoard()

    def calculateCellMovementDistancePerFrame(self, player):
        return self.maxDistancePerFrame * self.sqrt05 / math.sqrt(0.5 * player.mass)

    def askPlayersForDecisions(self):
        for player in self.agarBoard.players:
            player.makeDecision(self.agarBoard.getNeighboursForPlayer(player))

    def eatingTime(self, eater, eaten):
        self.agarBoard.removePlayer(eaten)
        eater.eatenSth(eaten)
        eaten.haveBeenEaten()
        # self.agarBoard.addPlayer(eaten)

    def movePlayer(self, player):
        if not player.isActive():
            return
        # damn you python, where are 2d vector calculations??
        # calculate direction
        dir_vector = player.movement_vector
        dir_vector_len = math.sqrt(dir_vector[0]*dir_vector[0] + dir_vector[1]*dir_vector[1])
        if dir_vector_len == 0:
            return
        move_distance = self.calculateCellMovementDistancePerFrame(player)
        d = move_distance/dir_vector_len
        # move player
        self.agarBoard.movePlayerToPosition(player, player.x+dir_vector[0]*d, player.y+dir_vector[1]*d)
        # # check collisions
        # for neighbour in self.agarBoard.getNeighboursForPlayer(player):
        #     if player.isColliding(neighbour):
        #         if player.mass > neighbour.mass:
        #             self.eatingTime(player, neighbour)
        #         else:
        #             self.eatingTime(neighbour, player)

    def movePlayers(self):
        for player in self.agarBoard.players:
            self.movePlayer(player)

    def collidePlayer(self, player):
        if not player.isActive():
            return
        # check collisions
        for neighbour in self.agarBoard.getNeighboursForPlayer(player):
            if player.isColliding(neighbour):
                if player.mass > neighbour.mass:
                    self.eatingTime(player, neighbour)
                elif player.mass < neighbour.mass:
                    self.eatingTime(neighbour, player)
    def collidePlayers(self):
        for player in self.agarBoard.players:
            self.collidePlayer(player)


    def plotBoard(self, print_info=False):
        x = [player.x for player in self.agarBoard.players]
        y = [player.y for player in self.agarBoard.players]
        sizes = [player.mass for player in self.agarBoard.players]
        numberOfPlayers = len(self.agarBoard.players)
        # colors = ['red' if i < numberOfPlayers/2 else 'white' for i in xrange(numberOfPlayers)]
        # markers = ['.' if i < 10 else 'o' for i in xrange(len(self.agarBoard.players))]
        # colors[0] = 'red'
        self.ax.cla()
        if print_info:
            print(zip(x, y, sizes))
        self.ax.scatter(x, y, s=sizes, c='white')

        x = [player.x for player in self.agarBoard.getIntelligentPlayers()]
        y = [player.y for player in self.agarBoard.getIntelligentPlayers()]
        sizes = [player.mass for player in self.agarBoard.getIntelligentPlayers()]
        self.ax.scatter(x, y, s=sizes, c='red')

        self.ax.set_xlim(0, self.agarBoard.size_x)
        self.ax.set_ylim(0, self.agarBoard.size_y)
        plt.pause(self.plotPauseInterval)

    def makeRound(self):
        self.askPlayersForDecisions()
        for i in range(self.playersDecideEveryXRounds):
            self.movePlayers()
            self.collidePlayers()
        if self.displayPlot:
            self.plotBoard()





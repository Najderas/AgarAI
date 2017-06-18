__author__ = 'Grzegorz'

import logging
from .AgarPlayer import AgarPlayer
import random

class AgarBoard:
    """
    class ensures basic optimisation
    """
    def __init__(self, size_x=1000, size_y=1000, bucket_matrix_density_x=10, bucket_matrix_density_y=10):
        self.size_x = size_x
        self.size_y = size_y
        self.bucket_matrix_density_x = bucket_matrix_density_x
        self.bucket_matrix_density_y = bucket_matrix_density_y
        self.logger = logging.getLogger(__name__)

        self.players = set()
        self.bucket_matrix = [ [ set() for y in range(self.bucket_matrix_density_y) ] for x in range(self.bucket_matrix_density_x) ]
        # now call self.bucket_matrix[x][y]
        self.seingRadiusMultiplier = 10

    def calculateViewRadius(self, radius):
        return radius*self.seingRadiusMultiplier

    def _getBucketsSliceX(self, x, radius):
        left_slice = int(max(x-radius, 0) * self.bucket_matrix_density_x / self.size_x)
        right_slice = int(min(x+radius, self.size_x-0.01) * self.bucket_matrix_density_x / self.size_x)
        return range(left_slice, right_slice+1)

    def _getBucketsSliceY(self, y, radius):
        top_slice = int(max(y-radius, 0) * self.bucket_matrix_density_y / self.size_y)
        bottom_slice = int(min(y+radius, self.size_y-0.01) * self.bucket_matrix_density_y / self.size_y)
        return range(top_slice, bottom_slice+1)

    def getBucketsFromPositionAndRadius(self, x, y, radius):
        """
        Big player can be in many buckets in one moment. Even the smallest one could be in up to 4 buckets
        returns (buckets_x_list, buckets_y_list) or None
        """
        if x<0 or y<0:
            self.logger.error("getBucketsFromPosition got incorrect coordinates - x: %s y: %s "%(x,y))
            return None
        #this is not proper, because player can be in more than one "zone" (bucket) simultanously
        # bucket_x_ = int( x * self.bucket_matrix_density_x / self.size_x )
        # bucket_y = int( y * self.bucket_matrix_density_y / self.size_y )
        buckets_x_list = self._getBucketsSliceX(x, radius)
        buckets_y_list = self._getBucketsSliceY(y, radius)
        return buckets_x_list, buckets_y_list

    def _removeFromUnusedBucketsAddToNew(self, player, old_buckets_x_list, old_buckets_y_list, new_buckets_x_list, new_buckets_y_list):
        # for old_x in old_buckets_x_list:
        #     if old_x not in new_buckets_x_list:
        #         for y in old_buckets_y_list
        for bx in old_buckets_x_list:
            if bx not in new_buckets_x_list:
                for by in old_buckets_y_list:
                    self.bucket_matrix[bx][by].discard(player)
        for by in old_buckets_y_list:
            if by not in new_buckets_y_list:
                for bx in old_buckets_x_list:
                    self.bucket_matrix[bx][by].discard(player)

        for bx in new_buckets_x_list:
            if bx not in old_buckets_x_list:
                for by in new_buckets_y_list:
                    self.bucket_matrix[bx][by].add(player)

        for by in new_buckets_y_list:
            if by not in old_buckets_y_list:
                for bx in new_buckets_x_list:
                    self.bucket_matrix[bx][by].add(player)

    def getNeighboursForPlayer(self, player):
        buckets_x_list, buckets_y_list = self.getBucketsFromPositionAndRadius(player.x, player.y, player.radius)
        neighbours = set()
        for bx in buckets_x_list:
            for by in buckets_y_list:
                neighbours.update(self.bucket_matrix[bx][by])
        return neighbours

    def getNeighboursSeenByPlayer(self, player):
        view_radius = self.calculateViewRadius(player.radius)
        buckets_x_list, buckets_y_list = self.getBucketsFromPositionAndRadius(player.x, player.y, player.radius)
        neighbours = set()
        for bx in buckets_x_list:
            for by in buckets_y_list:
                neighbours.update(self.bucket_matrix[bx][by])
        return neighbours

    def movePlayerToPosition(self, player, new_x, new_y):
        """
        player shouldn't know anything about "buckets" (optimisation mechanism)
        """
        old_buckets_x_list, old_buckets_y_list = self.getBucketsFromPositionAndRadius(player.x, player.y, player.radius)
        new_x = 0 if new_x<0 else self.size_x if new_x>self.size_x else new_x
        new_y = 0 if new_y<0 else self.size_y if new_y>self.size_y else new_y

        player.x = new_x
        player.y = new_y
        new_buckets_x_list, new_buckets_y_list = self.getBucketsFromPositionAndRadius(player.x, player.y, player.radius)

        self._removeFromUnusedBucketsAddToNew(player, old_buckets_x_list, old_buckets_y_list, new_buckets_x_list, new_buckets_y_list)

    def randomizePosition(self, player):
        while True:
            player.x = random.randrange(self.size_x)
            player.y = random.randrange(self.size_y)
            # is colliding with anybody?
            collides = False
            for neighbour in self.getNeighboursForPlayer(player):
                if player.isColliding(neighbour):
                    collides = True
                    break
            if not collides:
                break

    def addPlayer(self, player):
        self.players.add(player)
        if player.x<0 or player.y<0:
            self.randomizePosition(player)
        new_buckets_x_list, new_buckets_y_list = self.getBucketsFromPositionAndRadius(player.x, player.y, player.radius)
        for bx in new_buckets_x_list:
            for by in new_buckets_y_list:
                self.bucket_matrix[bx][by].add(player)

    def removePlayer(self, player):
        old_buckets_x_list, old_buckets_y_list = self.getBucketsFromPositionAndRadius(player.x, player.y, player.radius)
        self._removeFromUnusedBucketsAddToNew(player, old_buckets_x_list, old_buckets_y_list, [], [])

    def populateBoardWithPlayers(self, number = 50):
        for i in range(number):
            player = AgarPlayer()
            # random place
            self.randomizePosition(player)
            self.addPlayer(player)













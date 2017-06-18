__author__ = 'Grzegorz'

from agarGame.AgarLogic.AgarBoard import AgarBoard

import agarGame.AgarLogic.AgarMainGame

if __name__ == "__main__":
    print("Hellooo from main")
    
    board = AgarBoard()

    game = agarGame.AgarLogic.AgarMainGame.AgarMainGame(board)
    game.makeRound()




# class A:
#     def __init__(self):
#         self.a = 1
#         self.b = 2
# a = A()
# b = A()
# c = set([a,b])
# print(c)
# print("a in c:", a in c)


from AgarLogic.AgarBoard import AgarBoard
import AgarLogic.AgarMainGame

if __name__ == "__main__":
    print("Hellooo from main")

    board = AgarBoard()

    game = AgarLogic.AgarMainGame.AgarMainGame(board)

    for i in xrange(100):
        game.makeRound()

    game.plotBoard(print_info=True)




# class A:
#     def __init__(self):
#         self.a = 1
#         self.b = 2
# a = A()
# b = A()
# c = set([a,b])
# print(c)
# print("a in c:", a in c)


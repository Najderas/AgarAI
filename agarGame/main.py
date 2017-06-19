from AgarLogic.AgarBoard import AgarBoard
import AgarLogic.AgarMainGame

ROUNDS_NUMBER = 200
BOARD_SIZE = 300

if __name__ == "__main__":

    board = AgarBoard(BOARD_SIZE, BOARD_SIZE)
    game = AgarLogic.AgarMainGame.AgarMainGame(board)

    for i in xrange(ROUNDS_NUMBER):
        game.makeRound()

    game.plotBoard(print_info=True)

    print(filter(lambda x: x.isActive(), board.players))
    print("Firstly there were " + str(board.defaultPlayerNumber) + " players.")
    print("Players left: " + str(len(filter(lambda x: x.isActive(), board.players) ) ) )
    print("mases: ", sorted([pl.mass for pl in filter(lambda x: x.isActive(), board.players)], reverse=True) )





# class A:
#     def __init__(self):
#         self.a = 1
#         self.b = 2
# a = A()
# b = A()
# c = set([a,b])
# print(c)
# print("a in c:", a in c)


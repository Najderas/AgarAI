from AgarLogic.AgarBoard import AgarBoard
import AgarLogic.AgarMainGame

ROUNDS_NUMBER = 2000
BOARD_SIZE = 300

if __name__ == "__main__":

    board = AgarBoard(BOARD_SIZE, BOARD_SIZE)
    game = AgarLogic.AgarMainGame.AgarMainGame(board)

    for i in xrange(ROUNDS_NUMBER):
        game.makeRound()

    game.plotBoard(print_info=True)

    left_alive = filter(lambda x: x.isActive(), board.players)
    left_alive_repr = [(p.__str__(), p.mass) for p in left_alive]
    print(left_alive_repr)
    print("Firstly there were " + str(board.defaultPlayerNumber) + " players.")
    print("Players left: " + str(len(left_alive) ) )
    print("mases: ", sorted([pl.mass for pl in left_alive], reverse=True) )

    sorted_by_second = sorted(left_alive_repr, key=lambda tup: tup[1], reverse=True)
    print(sorted_by_second)






# class A:
#     def __init__(self):
#         self.a = 1
#         self.b = 2
# a = A()
# b = A()
# c = set([a,b])
# print(c)
# print("a in c:", a in c)


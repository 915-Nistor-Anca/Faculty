from board.board import Board
from game.game import Game
from player.computer import Computer
from player.human import Human
from strategy.strategy import Strategy
from validators.validators import Validators

if __name__ == '__main__':
    v = Validators()
    B1 = Board(10, 10, v)
    B2 = Board(10, 10, v)
    B3 = Board(10, 10, v)
    B4 = Board(10, 10, v)
    s = Strategy()
    p1 = Human("Alexia", B1, B3)
    p2 = Computer("Computer", B2, B4, s)

    G = Game(p1, p2, v)
    G.play()


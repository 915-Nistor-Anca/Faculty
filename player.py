from abc import abstractmethod

from board.cell import Cell


class Player:
    def __init__(self, name, board1, board2):
        self.__name = name
        self._board_ships = board1
        self._board_shots = board2

    @abstractmethod
    def move(self, *args) -> Cell:
        pass

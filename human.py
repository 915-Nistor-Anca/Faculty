from board.cell import Cell
from player.player import Player


class Human(Player):
    def move(self, line, column, value):
        self._board_shots.set_value(line, column, value)
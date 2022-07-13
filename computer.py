from player.player import Player


class Computer(Player):
    def __init__(self, name, board1, board2, strategy):
        super().__init__(name, board1, board2)
        self.__strategy = strategy

    def move(self):
        """
        :return: the line and the column where the computer should shoot, based on the given strategy
        """
        l, c = self.__strategy.move(self._board_shots)
        return l, c
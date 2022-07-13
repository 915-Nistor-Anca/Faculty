import random

from player.human import Human
from validators.validators import ShipValidator


class Game:
    def __init__(self, player1, player2, validator):
        self.__player1 = player1 #human
        self.__player2 = player2 #computer
        self.__validator = validator

    def place_ships_human(self):
        """
        This function places all the ships the human has. For a ship to be placed, the user has to
        enter the line and the column where the ships starts and the direction it goes.
        """
        print('BATTLESHIP GAME')
        print(self.__player1._board_ships.__str__())
        print('Firstly, you need to arrange five ships on the board.')
        print('You can place them vertically or horizontally.')
        print('Please enter the data for:')
        ok = 0
        while ok == 0:
            try:
                print('-the first ship: AIRCRAFT CARRIER (occupies 5 spaces).')
                line = int(input('Enter the line:'))
                column = int(input('Enter the column:'))
                direction = input('Enter the direction the ship will be placed (left, right, up or down):')
                self.__player1._board_ships.create_ship(5, direction, line - 1, column - 1, "🚢")
                ok = 1
            except ShipValidator as s:
                print(str(s))
                print('Try again:', '\n')
            print(self.__player1._board_ships.__str__())

        ok = 0
        while ok == 0:
            try:
                print('-the second ship: BATTLESHIP (occupies 4 spaces).')
                line = int(input('Enter the line:'))
                column = int(input('Enter the column:'))
                direction = input('Enter the direction the ship will be placed (left, right, up or down):')
                self.__player1._board_ships.create_ship(4, direction, line - 1, column - 1, "🛥️")
                ok = 1
            except ShipValidator as s:
                print(str(s))
                print('Try again:', '\n')
            print(self.__player1._board_ships.__str__())

        ok = 0
        while ok == 0:
            try:
                print('-the third ship: CRUISER (occupies 3 spaces).')
                line = int(input('Enter the line:'))
                column = int(input('Enter the column:'))
                direction = input('Enter the direction the ship will be placed (left, right, up or down):')
                self.__player1._board_ships.create_ship(3, direction, line - 1, column - 1, "🛳️")
                ok = 1
            except ShipValidator as s:
                print(str(s))
                print('Try again:', '\n')
            print(self.__player1._board_ships.__str__())

        ok = 0
        while ok == 0:
            try:
                print('-the fourth ship: SUBMARINE (occupies 3 spaces).')
                line = int(input('Enter the line:'))
                column = int(input('Enter the column:'))
                direction = input('Enter the direction the ship will be placed (left, right, up or down):')
                self.__player1._board_ships.create_ship(3, direction, line - 1, column - 1, "🛶")
                ok = 1
            except ShipValidator as s:
                print(str(s))
                print('Try again:', '\n')
            print(self.__player1._board_ships.__str__())

        ok = 0
        while ok == 0:
            try:
                print('-the fifth ship: DESTROYER (occupies 2 spaces).')
                line = int(input('Enter the line:'))
                column = int(input('Enter the column:'))
                direction = input('Enter the direction the ship will be placed (left, right, up or down):')
                self.__player1._board_ships.create_ship(2, direction, line - 1, column - 1, "⛴")
                ok = 1
            except ShipValidator as s:
                print(str(s))
                print('Try again:', '\n')
            print(self.__player1._board_ships.__str__())

    def place_ships_computer(self):
        """
        This function places the ships for the computer (they are placed randomly) and then prints the board.
        """
        k = 0
        l = ["⛴", "🛶", "🛳️", "🛥️", "🚢"]
        for i in [2, 3, 3, 4, 5]:
            ok = 0
            while ok == 0:
                try:
                    line = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
                    column = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
                    direction = random.choice(["left", "right", "up", "down"])
                    self.__player2._board_ships.create_ship(i, direction, line - 1, column - 1, l[k])
                    k += 1
                    ok = 1
                except ShipValidator:
                    pass
        print(self.__player2._board_ships.__str__())

    def __is_over(self, board):
        """
        This function checks if the game is over, depending on the number of occupied cells.
        :param board: a 10x10 matrix where the shots of the player are
        :return: True, if the game is over and False, if it isn't
        """
        if board.count_occupied_cells() == 17:
            return True
        return False

    def shot(self, board_with_ships, board_with_shots, line, column):
        """
        This function shots at the given (line, column).
        If there is a ship, the value becomes "💣", else, "⭕".
        :param board_with_ships: matrix 10x10, the board with ships
        :param board_with_shots: matrix 10x10, the board where the player shoots
        :param line: int
        :param column: int
        """
        self.__validator.shot_validator(line, column, board_with_shots)
        if board_with_ships.get_value(line, column) == "💦":
            board_with_shots.set_value(line, column, "⭕")
        else:
            board_with_shots.set_value(line, column, "💣")

    def check_if_ship_completely_destroyed(self, sign, player1, player2):
        """
        This function checks if a ship is completely destroyed. If a ship is destroyed, it is marked entirely
        with "💣".
        :param sign: the sign of the ship (each ship has a different one)
        :param player1: the player who has the ship
        :param player2: the player who shoots
        :return: 1, if the ship is completely destroyed or 0, if not
        """
        for line in range(0, 10):
            for column in range(0, 10):
                if player1._board_ships.get_value(line, column) == sign and player2._board_shots.get_value(line, column) \
                    != "💣":
                    return 0
        return 1

    def change_sign(self, sign, player1, player2):
        """

        :param sign: the sign of the ship which is completely destroyed
        :param player1: the player who has the ships
        :param player2: the player who shoots
        """
        for line in range(0, 10):
            for column in range(0, 10):
                if player1._board_ships.get_value(line, column) == sign:
                    player2._board_shots.set_value(line, column, "🚩")

    def mark_destroyed_ships(self, player1, player2):
        """
        This function prints what ship has been destroyed.
        :param player1: the player with the ships
        :param player2: the player who shoots
        """
        for sign in ["⛴", "🛶", "🛳️", "🛥️", "🚢"]:
            if self.check_if_ship_completely_destroyed(sign, player1, player2):
                self.change_sign(sign, player1, player2)
                print(player1._board_shots.recognize_ship(sign), 'destroyed!')


    def __move(self, player1, player2, line, column):
        """
        This function shoots at the given coordinates (if the player is the human), or
        at the coordinates calculated by the strategy of the computer
        :param player1: the first player
        :param player2: the second player
        :param line: the line where the player wants to move
        :param column: the column where the player wants to move
        :return: 1, if the computer has shot
        """
        if type(player1) is Human:
            try:
                self.shot(player2._board_ships, player1._board_shots, line, column)
            except ShipValidator as s:
                print(str(s))
        else: #i need to find the line and the column where it s ok to shoot as a computer
            line, column = self.__player2.move()
            if line != -1 and column != -1:
                self.shot(player2._board_ships, player1._board_shots, int(line), int(column))
                return 1



    def __read_data(self):
        """
        This function reads the line and the column given by the human.
        :return: the values - 1, because positions start from 0
        """
        line = input('Enter the line:')
        column = input('Enter the column:')
        return int(line)-1, int(column)-1

    def play(self):
        """
        This is the main function which makes the game happen.
        Firstly, both human and computer place their ships.
        Then, they shoot on each other boards until one of them has completely shot all the other's ships.
        The one which is done first wins.
        """
        self.place_ships_computer()
        self.place_ships_human()
        print('\n')
        print("Time to shoot the computer's ships!")

        ok = 1
        while self.__is_over(self.__player1._board_shots) is False and \
            self.__is_over(self.__player2._board_shots) is False:

            if ok == 1: #human`s turn
                line, column = self.__read_data()
                self.__move(self.__player1, self.__player2, line, column)
                ok = 0

            else:
                ok = 1
                k = -1
                done = 0
                while done == 0 and k == -1:
                    try:
                        k = self.__move(self.__player2, self.__player1, -1, -1)
                        done = 1
                    except ShipValidator as s:
                        print(str(s))

            self.mark_destroyed_ships(self.__player1, self.__player2)
            self.mark_destroyed_ships(self.__player2, self.__player1)

            if ok == 0:
                print(self.__player1._board_shots.__str__())
            else:
                print("Game shot:")
                print(self.__player2._board_shots.__str__())

        if self.__is_over(self.__player2._board_shots) is True:
            print("Computer wins!")
        else:
            print("You win! Yay!")

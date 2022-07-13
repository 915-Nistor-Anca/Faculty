from board.cell import Cell


class Board:
    def __init__(self, lines, columns, validator, empty_value="💦"):
        self.__lines = lines
        self.__columns = columns
        self.__empty_value = empty_value
        self.__validator = validator

        self.__cells = self.__create_board()

    def __create_board(self):
        """
        This function creates a board with (lines) lines and (columns) columns.
        :return: the empty board
        """
        return [[Cell(line, column, self.__empty_value) for column in range(self.__columns)]
                for line in range(self.__lines)]

    def __str__(self):
        """
        This function is used when printing the board.
        :return: the board in a nice way
        """
        res = ""
        for line in self.__cells:
            s = " ".join([str(cell.value) for cell in line]) + "\n"
            res += s
        return res

    def set_value(self, line, column, value):
        self.__cells[line][column].value = value

    def get_nr_lines(self):
        return self.__lines

    def get_nr_columns(self):
        return self.__columns

    def get_value(self, line, column):
        return self.__cells[line][column].value

    def create_ship(self, size, direction, line, column, sign):
        """
        This function marks the new ship on the board with ships.
        It starts from the point (line, column) and it goes in the specified direction.
        :param size: int
        :param direction: up, down, left or right
        :param line: int
        :param column: int
        :param sign: the sign of the ship we save
        """
        self.__validator.ship_placement_validator(size, direction, line, column, self.get_nr_lines(), self.get_nr_columns(), self)
        if direction == "left":
            while size != 0:
                self.set_value(line, column, sign)
                column -= 1
                size -= 1
        elif direction == "right":
            while size != 0:
                self.set_value(line, column, sign)
                column += 1
                size -= 1
        elif direction == "up":
            while size != 0:
                self.set_value(line, column, sign)
                line -= 1
                size -= 1
        elif direction == "down":
            while size != 0:
                self.set_value(line, column, sign)
                line += 1
                size -=1

    def count_occupied_cells(self):
        """
        This function counts the number of bombs in the board.
        :return: the number of "🚩" found
        """
        k = 0
        for line in range(0, 10):
            for column in range(0, 10):
                if self.get_value(line, column) == "🚩":
                    k += 1
        return k

    def count_bombs(self):
        """
        This function counts the number of bombs in the board.
        :return: the number of "💣" found
        """
        k = 0
        for line in range(0, 10):
            for column in range(0, 10):
                if self.get_value(line, column) == "💣":
                    k += 1
        return k

    def recognize_ship(self, sign):
        """
        This function recognizes a certain ship, depending on the sign.
        :param sign: char
        :return: the name of the ship which has that sign
        """
        if sign == "⛴":
            return "DESTROYER"
        if sign == "🛶":
            return "SUBMARINE"
        if sign == "🛳️":
            return "CRUISER"
        if sign == "🛥️":
            return "BATTLESHIP"
        if sign == "🚢":
            return "AIRCRAFT CARRIER"

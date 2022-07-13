import random

class Position:
    def __init__(self, line, column):
        self.__line = line
        self.__column = column

    def line(self):
        return self.__line

    def column(self):
        return self.__column

class Strategy:
    def __init__(self):
        self.__start_position = Position(-1, -1)
        self.__direction = ""

    def bomb_placement(self, board):
        """
        This function returns the line and the column of the first cell which contains a bomb.
        :param board: a matrix
        :return: the line and the column, or (-1, -1), if there is no bomb
        """
        for line in range(0, 10):
            for column in range(0, 10):
                if board.get_value(line, column) == "💣":
                    return line, column
        return -1, -1

    def find_direction(self, board):
        """
        This function gives the direction (horrizontally/vertically) a ship is placed.
        If starts from the first bomb found. If there is another bomb in its left, right => horizontally.
        Else, the direction is vertically.
        :param board: a matrix
        :return: the direction
        """
        line, column = self.bomb_placement(board)
        if line > 0:
            if board.get_value(line-1, column) == "💣":
                return "vertically"
        if line < 9:
            if board.get_value(line + 1, column) == "💣":
                return "vertically"
        if column > 0:
            if board.get_value(line, column - 1) == "💣":
                return "horizontally"
        if column < 9:
            if board.get_value(line, column + 1) == "💣":
                return "horizontally"
        return None

    def find_next_target(self, board, direction):
        """
        Based on the direction, the function tries to find the next potential cell which might be part of a ship.
        If the direction is vertically, it goes on that column and shoots the next cell which hasn't been shot.
        If it's horizontally, it moves on the line of the first found bomb.
        :param board: a matrix
        :param direction: "vertically" or "horizontally"
        :return: the line and the column chosen to be the next target
        """
        line = self.__start_position.line()
        column = self.__start_position.column()
        if direction == "vertically":
            line -= 1
            ok = 1
            while line >= 0 and ok == 1:
                if board.get_value(line, column) == "💦":
                    return line, column
                elif board.get_value(line, column) != "💣":
                    ok = 0
                line -= 1
            line = self.__start_position.line()
            line += 1
            ok = 1
            while line <= 9 and ok == 1:
                if board.get_value(line, column) == "💦":
                    return line, column
                elif board.get_value(line, column) != "💣":
                    ok = 0
                line += 1
        line = self.__start_position.line()
        column = self.__start_position.column()
        if direction == "horizontally":
            column -= 1
            ok = 1
            while column >= 0 and ok == 1:
                if board.get_value(line, column) == "💦":
                    return line, column
                elif board.get_value(line, column) != "💣":
                    ok = 0
                column -= 1
            column = self.__start_position.column()
            column += 1
            ok = 1
            while column <= 9 and ok == 1:
                if board.get_value(line, column) == "💦":
                    return line, column
                elif board.get_value(line, column) != "💣":
                    ok = 0
                column += 1
        return None

    def move(self, board): #this is the board where the computer sees its shots
        bombs = board.count_bombs()
        line = -1
        column = -1
        if bombs == 0:
            line = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
            column = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
            while board.get_value(line, column) != "💦":
                line = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
                column = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
            self.__start_position = Position(line, column)
            self.__direction = "up"
        else:
            if bombs == 1: #we found a place
                if self.__direction == "up" and \
                        (self.__start_position.line() >= 1 and
                         board.get_value(self.__start_position.line() - 1, self.__start_position.column()) == "💦"):
                    line = self.__start_position.line() - 1
                    column = self.__start_position.column()
                    self.__direction = "right"
                elif self.__direction == "right" and \
                        (self.__start_position.column() <= 8 and
                         board.get_value(self.__start_position.line(), self.__start_position.column() + 1) == "💦"):
                    line = self.__start_position.line()
                    column = self.__start_position.column() + 1
                    self.__direction = "down"
                elif self.__direction == "down" and \
                        (self.__start_position.line() <= 8 and
                        board.get_value(self.__start_position.line() + 1, self.__start_position.column()) == "💦"):
                    line = self.__start_position.line() + 1
                    column = self.__start_position.column()
                    self.__direction = "left"
                else:
                    line = self.__start_position.line()
                    column = self.__start_position.column() - 1
                    self.__direction = ""
            elif bombs >= 2: #we found a place and a direction (horizontally / vertically)
                    print(self.find_direction(board))
                    direction = self.find_direction(board)
                    line, column = self.find_next_target(board, direction)


        return int(line), int(column)


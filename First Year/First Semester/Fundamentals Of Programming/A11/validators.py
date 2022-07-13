class Error(Exception):
    pass

class ShipValidator(Error):
    pass

class VE(Error):
    pass

class Validators:
    def ship_placement_validator(self, size, direction , line, column, l, c, board):
        if direction not in ["left", "right", "up", "down"]:
            raise ShipValidator('Invalid direction.')
        if int(line) < 0 or int(line) > 9:
            raise ShipValidator('The line value can only be from 1 to 10.')
        if int(column) < 0 or int(column) > 9:
            raise ShipValidator('The column value can only be from 1 to 10.')
        if direction == "left":
            if size > column:
                raise ShipValidator("Ship doesn't fit there!")
            while size != 0:
                if board.get_value(line, column) != "💦":
                    raise ShipValidator("Cannot place ship on another one.")
                column -= 1
                size -= 1
        elif direction == "right":
            if size >= c - column + 1:
                raise ShipValidator("Ship doesn't fit there!")
            while size != 0:
                if board.get_value(line, column) != "💦":
                    raise ShipValidator("Cannot place ship on another one.")
                column += 1
                size -= 1
        elif direction == "up":
            if size > line:
                raise ShipValidator("Ship doesn't fit there!")
            while size != 0:
                if board.get_value(line, column) != "💦":
                    raise ShipValidator("Cannot place ship on another one.")
                line -= 1
                size -= 1
        elif direction == "down":
            if size >= l - line + 1:
                raise ShipValidator("Ship doesn't fit there!")
            while size != 0:
                if board.get_value(line, column) != "💦":
                    raise ShipValidator("Cannot place ship on another one.")
                line += 1
                size -= 1

    def shot_validator(self, line, column, board):
        if board.get_value(line, column) in ["⭕", "💣"]:
            raise ShipValidator("You have already shot here! Try somewhere else.")


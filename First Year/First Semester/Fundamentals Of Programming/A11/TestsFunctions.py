import unittest

from board.board import Board
from strategy.strategy import Strategy
from validators.validators import Validators, ShipValidator


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.__validators = Validators()

    def tearDown(self) -> None:
        pass

    def testValidators(self):
        b = Board(10, 10, self.__validators)
        with self.assertRaises(ShipValidator):
            self.__validators.ship_placement_validator(11, "abc", 3, 4, 5, 1, b)
        with self.assertRaises(ShipValidator):
            self.__validators.ship_placement_validator(11, "down", 3, 4, 5, 1, b)
        with self.assertRaises(ShipValidator):
            self.__validators.ship_placement_validator(10, "down", 30, 4, 5, 1, b)
        with self.assertRaises(ShipValidator):
            self.__validators.ship_placement_validator(10, "down", 3, 40, 5, 1, b)

        with self.assertRaises(ShipValidator):
            self.__validators.ship_placement_validator(10, "left", 9, 4, 5, 1, b)
        with self.assertRaises(ShipValidator):
            self.__validators.ship_placement_validator(10, "down", 9, 4, 5, 1, b)
        with self.assertRaises(ShipValidator):
            self.__validators.ship_placement_validator(10, "left", 9, 4, 5, 1, b)
        with self.assertRaises(ShipValidator):
            self.__validators.ship_placement_validator(10, "right", 9, 4, 5, 1, b)

        self.__validators.ship_placement_validator(1, "left", 1, 5, 5, 1, b)
        self.__validators.ship_placement_validator(1, "down", 1, 5, 5, 1, b)
        self.__validators.ship_placement_validator(1, "left", 1, 5, 5, 1, b)
        with self.assertRaises(ShipValidator):
            self.__validators.ship_placement_validator(1, "right", 1, 5, 5, 1, b)

        b1 = Board(10, 10, self.__validators)
        b1.set_value(1,1,'a')
        with self.assertRaises(ShipValidator):
            self.__validators.ship_placement_validator(1, "left", 1, 1, 1, 1, b1)
        with self.assertRaises(ShipValidator):
            self.__validators.ship_placement_validator(2, "right", 1, 1, 1, 4, b1)
        self.__validators.ship_placement_validator(1, "right", 3, 2, 5, 4, b1)

        with self.assertRaises(ShipValidator):
            self.__validators.ship_placement_validator(1, "up", 1, 1, 1, 1, b1)
        with self.assertRaises(ShipValidator):
            self.__validators.ship_placement_validator(2, "left", 1, 1, 1, 1, b1)
        with self.assertRaises(ShipValidator):
            self.__validators.ship_placement_validator(1, "up", 1, 1, 1, 1, b1)

        self.__validators.ship_placement_validator(1, "right", 3, 2, 5, 4, b1)
        with self.assertRaises(ShipValidator):
            self.__validators.ship_placement_validator(8, "up", 3, 2, 5, 4, b1)
        self.__validators.ship_placement_validator(1, "up", 3, 2, 5, 4, b1)

        b1 = Board(10, 10, self.__validators)
        b1.set_value(1, 1, 'a')
        with self.assertRaises(ShipValidator):
            self.__validators.ship_placement_validator(1, "down", 1, 1, 1, 1, b1)
        with self.assertRaises(ShipValidator):
            self.__validators.ship_placement_validator(1, "down", 1, 1, 4, 1, b1)

        b1 = Board(10, 10, self.__validators)
        b1.set_value(1, 1, 'a')
        self.__validators.shot_validator(1,1,b1)

    def testBoard(self):
        b1 = Board(10, 10, self.__validators)
        k = b1.count_occupied_cells()
        self.assertEqual(k, 0)
        b = b1.__str__()
        c = b1.get_nr_columns()
        l = b1.get_nr_lines()
        self.assertEqual(c, 10)
        self.assertEqual(l, 10)
        k = b1.count_bombs()
        self.assertEqual(k, 0)
        s = b1.recognize_ship("⛴")
        self.assertEqual(s, "DESTROYER")

    def testStrategy(self):
        b1 = Board(10, 10, self.__validators)
        s = Strategy()
        l, c = s.bomb_placement(b1)
        self.assertEqual(l, -1)
        d = s.find_direction(b1)
        self.assertEqual(d, None)
        t = s.find_next_target(b1, "left")
        self.assertEqual(t, None)


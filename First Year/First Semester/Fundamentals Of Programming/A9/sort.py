from abc import ABC, abstractmethod
from enum import Enum


class GenericSort(ABC):

    def __init__(self, col, key, reverse):
        self.__col = col
        self.__key = key
        self.__reverse = reverse

    @property
    def col(self):
        return self.__col

    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key):
        self.__key = key

    @property
    def reverse(self):
        return self.__reverse

    @abstractmethod
    def sort(self):
        pass

    def _in_order(self, e1, e2):
        if self.key is None:
            self.key = lambda x: x
        if self.reverse:
            return self.key(e1) > self.key(e2)
        return self.key(e1) < self.key(e2)

class GnomeSort(GenericSort):
    def __init__(self, col, key, reverse):
        super().__init__(col, key, reverse)

    def sort(self):
        """
        Gnome Sort is based on the technique used by the standard Dutch Garden Gnome.
        Here is how a garden gnome sorts a line of flower pots.
        Basically, he looks at the flower pot next to him and the previous one;
        if they are in the right order he steps one pot forward, otherwise, he swaps them and steps one pot backward.
        Boundary conditions: if there is no previous pot, he steps forwards; if there is no pot next to him, he is done.
        """
        pos = 0
        while pos < len(self.col):
            if (pos == 0 or not self._in_order(self.col[pos], self.col[pos-1])):
                pos += 1
            else:
                self.col[pos], self.col[pos-1] = self.col[pos - 1], self.col[pos]
                pos -= 1

class Algorithm(Enum):
    GNOME_SORT = GnomeSort

class Sorting(object):
    @staticmethod
    def sort(col, key=None, reverse=False, algorithm=Algorithm.GNOME_SORT):
        sorting_alg = algorithm.value(col, key, reverse)
        sorting_alg.sort()

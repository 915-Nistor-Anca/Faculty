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

class Filter:
    @staticmethod
    def filter(function, list):
        new_list = []
        for s in list:
            if function(s) is True:
                new_list.append(s)
        list = new_list
        return list

class Structure:
    def __init__(self):
        self.__data = []

    def __len__(self):
        return len(self.__data)

    def add(self, x):
        self.__data.append(x)

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        if self.__index == len(self.__data):
            raise StopIteration()
        self.__index += 1
        return self.__data[self.__index - 1]

    def __setitem__(self, key, value):
        self.__data[key] = value

    def __getitem__(self, index):
        return self.__data[index]

    def __delitem__(self, index):
        del self.__data[index]


if __name__ == '__main__':
    pass
    #list = [5, 3, 2, 4]
    #Sorting.sort(list)
    #print('list:', list)

    #def person_less_than(p1, p2):
    #    if p1.name == p2.name:
    #        return p1.student_id > p2.student_id
    #    return p1.name < p2.name

    #s1 = Student(1, 'ana', 1)
    #s2 = Student(2, 'bogdan', 2)
    #s3 = Student(3, 'bianca', 3)
    #s4 = Student(4, 'alexandra', 1)
    #list = [s3, s2, s4, s1]
    #Student.__lt__ = person_less_than
    #Student.__gt__ = lambda x, y: person_less_than(x,y)
    #Sorting.sort(list)
    #for s in list:
    #    print(s.name, s.group)
    #print('---------------------')
    #s1 = Student(1, 'ana', 1)
    #s2 = Student(2, 'bogdan', 2)
    #s3 = Student(3, 'bianca', 3)
    #s4 = Student(4, 'alexandra', 1)
    #list = [s3, s2, s4, s1]

    #def group_is_one(x):
    #    return x.student_id == 1

    #Filter.filter(group_is_one, list)
    #for s in list:
    #    print(s.name, s.group)



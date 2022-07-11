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

    def __delitem__(self, x):
        del self.__data[x]
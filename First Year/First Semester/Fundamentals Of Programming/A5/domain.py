class Student:
    def __init__(self, id, name, group):
        self.__id = id
        self.__name = name
        self.__group = group

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def group(self):
        return self.__group

    @id.setter
    def id(self, value):
        self.__id = value

    @name.setter
    def name(self, value):
        self.__name = value

    @group.setter
    def group(self, value):
        self.__group = value


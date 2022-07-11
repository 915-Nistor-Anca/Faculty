class Student:
    def __init__(self, student_id, name, group):
        self.__student_id = student_id
        self.__name = name
        self.__group = group

    @property
    def student_id(self):
        """
        :return: the id of the student
        """
        return self.__student_id

    @property
    def name(self):
        """
        :return: the name of the student
        """
        return self.__name

    @property
    def group(self):
        """
        :return: the group to which the student belongs
        """
        return self.__group

    @student_id.setter
    def student_id(self, value):
        """
        This function gives the student's id the given value.
        :param value: integer
        """
        self.__student_id = value

    @name.setter
    def name(self, value):
        """
        This function gives the given value to the student's name.
        :param value: string
        """
        self.__name = value

    @group.setter
    def group(self, value):
        """
        This function gives the given value to the student's group.
        :param value: integer
        """
        self.__group = value

    def __repr__(self):
        """
        :return: all the data of a student
        """
        return "Id: % s, Name: % s, Group: % s" % (self.student_id, self.name, self.group)



class Assignment:
    def __init__(self, assignment_id, description, deadline):
        self.__assignment_id = assignment_id
        self.__description = description
        self.__deadline = deadline

    @property
    def assignment_id(self):
        """
        :return: the assignment's id
        """
        return self.__assignment_id

    @property
    def description(self):
        """
        :return: the assignment's description
        """
        return self.__description

    @property
    def deadline(self):
        """
        :return: the assignment's deadline
        """
        return self.__deadline

    @assignment_id.setter
    def assignment_id(self, value):
        """
        This function gives the assignment's id the given value.
        :param value: integer
        """
        self.__assignment_id = value

    @description.setter
    def description(self, value):
        """
        This function gives the assignment's description the given value.
        :param value: string
        :return:
        """
        self.__description = value

    @deadline.setter
    def deadline(self, value):
        """
        This function gives the assignment's deadline the given value.
        :param value: string
        """
        self.__deadline = value

    def __repr__(self):
        """
        :return: all the data for an assignment
        """
        return "Id: % s, Description: % s, Deadline: % s" % (self.assignment_id, self.description, self.deadline)

class Grade:
    def __init__(self, assignment_id, student_id, grade_value):
        self.__assignment_id = assignment_id
        self.__student_id = student_id
        self.__grade_value = grade_value

    @property
    def assignment_id(self):
        """
        :return: the assignment's id
        """
        return self.__assignment_id

    @property
    def student_id(self):
        """
        :return: the student's id
        """
        return self.__student_id

    @property
    def grade_value(self):
        """
        :return: the grade value
        """
        return self.__grade_value

    @assignment_id.setter
    def assignment_id(self, value):
        """
        This function gives the assignment's id the given value.
        :param value: integer
        """
        self.__assignment_id = value

    @student_id.setter
    def student_id(self, value):
        """
        This function gives the student's id the given value.
        :param value: integer
        """
        self.__student_id = value

    @grade_value.setter
    def grade_value(self, value):
        """
        This function gives the grade's value the given value.
        :param value:
        :return:
        """
        self.__grade_value = value

    def __repr__(self):
        """
        :return: the list of grades
        """
        return "Assignment id: % s, Student id: % s, Grade: % s" % (self.assignment_id, self.student_id, self.grade_value)


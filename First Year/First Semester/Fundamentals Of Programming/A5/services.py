
from src.domain.domain import Student
class StudentsServices:
    def __init__(self):
        self.students = []
        self.changes = []

#for the ADD functionality
    def add_student(self, id, name, group):
        """
        This function adds a new student to the list.
        :param id: an integer
        :param name: a string
        :param group: an integer
        """
        s = Student(id, name, group)
        self.students.append(s)

    def test_add_student(self):
        s = self.add_student(10, 'Maria', 914)
        student = self.students[-1]
        if int(student.id) != 10 or student.name != 'Maria' or int(student.group) != 914:
            raise ValueError()
        self.students.pop()

#for the DISPLAY functionality

    def display(self):
        """
        This function displays the students in a nice way.
        """
        for i in range(0, len(self.students)):
            print('ID:', self.students[i].id)
            print('NAME:', self.students[i].name)
            print('GROUP:', self.students[i].group, '\n')

#for the FILTER functionality

    def filter(self, given_group):
        """
        This function removes the students which are part of the given group.
        :param given_group: an integer
        """
        i = 0
        n = len(self.students)
        while(i<n):
            if int(self.students[i].group) == int(given_group):
                self.students.remove(self.students[i])
                n-=1
            else:
                i+=1
            n = len(self.students)

    def test_filter(self):
        self.add_student(1, 'Ana', 912)
        self.add_student(2, 'Bianca', 914)
        self.filter(912)
        if len(self.students) != 1 or self.students[0].name != 'Bianca':
            raise ValueError()
        self.students.pop()

#for the UNDO functionality

    def add_list_to_changes(self):
        list = self.students.copy()
        self.changes.append(list)

    def undo(self):
        """
        """
        self.changes.pop()
        self.students[:] = self.changes[-1].copy()

    def test_add_list_to_changes(self):
        self.add_list_to_changes()
        if self.changes[-1] != self.students:
            raise ValueError()
        self.changes.pop()

    def test_undo(self):
        list1 = self.students
        self.add_list_to_changes()
        self.add_student(1,'Ioana', 913)
        self.add_list_to_changes()
        self.undo()
        assert list1 == self.students

    def remove_useless_spaces(self, command_line):
        new_command_line = ' '
        for i in range(0, len(command_line)):
            if (command_line[i] >= 'a' and command_line[i] <= 'z') or (
                    command_line[i] >= 'A' and command_line[i] <= 'Z') or (
                    command_line[i] == '<' or command_line[i] == '>' or command_line[i] == '=') or (
                    command_line[i] >= '0' and command_line[i] <= '9') or (
                    command_line[i] == ' ' and new_command_line[-1] != ' '):
                new_command_line = new_command_line + command_line[i]
        if new_command_line[0] == ' ':
            new_command_line = new_command_line.removeprefix(' ')
        if new_command_line[-1] == ' ':
            new_command_line = new_command_line.removesuffix(' ')
        return new_command_line

    def test_remove_useless_spaces(self):
        assert self.remove_useless_spaces(' add            2        gas    30  ') == 'add 2 gas 30'

    def get_command_and_args(self, command_line):
        command_line = self.remove_useless_spaces(command_line)
        position = command_line.find(' ')
        if position == -1:
            return command_line, []
        command = command_line[:position]
        args = command_line[position + 1:]
        args = args.split(' ')
        for word in args:
            word = word.replace(' ', '')
        return command, args

    def test_get_command_and_args(self):
        assert self.get_command_and_args('add      2 gas 30   ') == ('add', ['2', 'gas', '30'])

    def test_everything(self):
        self.test_add_student()
        self.test_filter()
        self.test_add_list_to_changes()
        self.test_remove_useless_spaces()
        self.test_get_command_and_args()
        self.test_undo()
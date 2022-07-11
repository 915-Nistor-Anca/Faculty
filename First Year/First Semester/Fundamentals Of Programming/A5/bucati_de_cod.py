from src.services.services import StudentsServices

class Console:
    def __init__(self):
        self.services = StudentsServices()
        self.commands = {'add': self.services.add_student, 'display': self.services.display, 'filter': self.services.filter, 'undo':self.services.undo}
    def show_menu(self):
        print('1. add: add a student;')
        print('2. display: display all students;')
        print('3. filter <group>: the students from that group are deleted;')
        print('4. undo;')
        print('5. exit.')

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

    def get_command_and_args(self, command_line):
        command_line = self.remove_useless_spaces(self, command_line)
        position = command_line.find(' ')
        if position == -1:
            return command_line, []
        command = command_line[:position]
        args = command_line[position + 1:]
        args = args.split(' ')
        for word in args:
            word = word.replace(' ', '')
        return command, args

    def run(self):
        while True:
            students = []
            changes = []
            self.show_menu(self)
            command_line = input('Enter command line:')
            if command_line == 'exit':
                break
            command, args = self.get_command_and_args(self, command_line)
            try:
                if command != 'undo':
                    self.commands[command](students, *args)
                    if command == 'add' or command == 'filter':
                        changes = self.add_list_to_changes(students, changes)
                else:
                    students = self.commands[command](students, changes)
            except KeyError:
                print('This option is not yet implemented.', '\n')
            except IndexError:
                print('The application does not know what it should do.', '\n')
            except ValueError:
                print('It cannot do that.')
            except TypeError:
                print('This operation is not supported.')




c = Console
c.run(c)

from src.services.services import StudentsServices
import random
class Console:
    def __int__(self):
        pass
    st = StudentsServices()
    def show_menu(self):
        print('1. add: add a student;')
        print('2. display: display all students;')
        print('3. filter <group>: the students from that group are deleted;')
        print('4. undo;')
        print('5. exit.')

    def ui_display(self):
        print('The students are:')
        self.st.display()

    def ui_undo(self):
        if len(self.st.changes) <= 1:
            print('Cannot undo operation.')
        else:
            self.st.undo()
            print('Operation reversed.')

    def first_ten_students(self):
        names = ['Anna', 'Mary', 'Elena', 'Fiona', 'Tiana', 'Susan', 'Sabrina', 'Tony', 'Jack', 'Tom', 'Ben', 'Dan', 'Lana']
        groups = [911, 912, 913, 914, 915, 916, 917]
        used_names = []
        used_numbers = []
        k = 0
        while(k<10):
            number = random.randint(1000, 9999)
            name = random.choice(names)
            group = random.choice(groups)
            if not number in used_numbers and not name in used_names:
                self.st.add_student(number, name, group)
                used_numbers.append(number)
                used_names.append(name)
                k += 1


    def run(self):
        self.st.changes.pop()
        self.first_ten_students()
        self.st.add_list_to_changes()
        commands = {'add': self.st.add_student, 'filter': self.st.filter, 'display': self.ui_display}
        while True:
            self.show_menu()
            command_line = input('Enter the command line:')
            if command_line == 'exit':
                break
            try:
                if command_line != 'undo':
                    command, args = self.st.get_command_and_args(command_line)
                    commands[command](*args)
                    if command == 'add' or command == 'filter':
                        self.st.add_list_to_changes()
                else:
                    self.ui_undo()
            except KeyError:
                print('This option is not yet implemented.', '\n')
            except IndexError:
                print('The application does not know what it should do.', '\n')
            except ValueError:
                print('It cannot do that.')
            except TypeError:
                print('This operation is not supported.')

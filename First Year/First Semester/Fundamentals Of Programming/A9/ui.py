from src.validators.validators import UnexistingCommand, NotTheRightNumberOfArgs, StudentValidatorException, \
    AssignmentValidatorException, GradeValidatorException, DeadlineValidator, TimeDataNotMatchFormat, StudentValidator, AssignmentValidator
from datetime import datetime, date

from src.undo_redo.undo import UndoManager
from src.undo_redo.redo import RedoManager

class Console:
    def __init__(self, general_services, student_service, assignment_service, grade_service):
        self.__general_services = general_services
        self.__student_service = student_service
        self.__assignment_service = assignment_service
        self.__grade_service = grade_service

    def print_main_menu(self):
        print('What do you want to do?')
        print('1.  manage students or assignments;')
        print('2.  give assignments;')
        print('3.  grade student;')
        print('3*. undo - undo the last given grade;')
        print('3**.redo;')
        print('4.  view statistics;')
        print('5.  exit.')

    def print_menu_1(self):
        print('- What do you want to manage?', '\n', '1. students', '\n', '2. assignments', '\n', '3. back')

    def show_menu_students(self):
        print('1. add: add a new student;')
        print('2. remove: remove an existing student;')
        print('3. update: update the informations for a student;')
        print('4. list: list all students;')
        print('5. back: go back to the previous menu;')
        print('*. undo - undo the last operation;')
        print('*. redo - cancel the last undo operation.')

    def show_menu_assignments(self):
        print('1. add: add a new assignment;')
        print('2. remove: remove an existing assignment;')
        print('3. update: update the informations for an assignment;')
        print('4. list: list all assignments;')
        print('5. back: go back to the previous menu.')
        print('*. undo - undo the last operation;')
        print('*. redo - cancel the last undo operation.')

    def run_menu_students(self):
        commands_student = {'add': self.__student_service.add_student, 'remove': self.__student_service.remove_student_and_delete_assignments,
                            'update': self.__student_service.update_student, 'list': self.print_students}
        while True:
            self.show_menu_students()
            command_line = input('Enter the command line:')

            if command_line == 'back':
                break
            elif command_line == 'undo':
                UndoManager.undo()
                RedoManager.save_last_operation(command_line)
            elif command_line == 'redo':
                if RedoManager.return_last_operation() != "undo" and RedoManager.return_last_operation() != 'list':
                    print('Cannot redo operation anymore.')
                    RedoManager.empty_list()
                else:
                    RedoManager.redo()
            else:
                try:
                    command, args = self.__general_services.get_command_and_args(command_line)
                    RedoManager.save_last_operation(command)
                    if command not in commands_student:
                        raise UnexistingCommand
                    elif command == 'add' and len(args) != 3 \
                        or command == 'remove' and len(args) != 1 \
                        or command == 'update' and len(args) != 4 \
                        or command == 'list' and len(args) != 0:
                        raise NotTheRightNumberOfArgs
                    commands_student[command](*args)
                except UnexistingCommand:
                    print('This command is not implemented.')
                except NotTheRightNumberOfArgs:
                    print('Too many/few arguments!')
                except StudentValidatorException as s:
                    print(str(s))
                except IndexError:
                    print('Nothing to change.')
                print('\n')

    def run_menu_assignments(self):
        commands_assignment = {'add': self.__assignment_service.add_assignment,
                               'remove': self.__assignment_service.remove_assignment_delete_grades,
                               'update': self.__assignment_service.update_assignment, 'list': self.print_assignments}
        while True:
            self.show_menu_assignments()
            command_line = input('Enter the command line:')
            if command_line == 'back':
                break
            elif command_line == 'undo':
                UndoManager.undo()
                RedoManager.save_last_operation(command_line)
            elif command_line == 'redo':
                if RedoManager.return_last_operation() != "undo" and RedoManager.return_last_operation() != 'list':
                    print('Cannot redo operation anymore.')
                    RedoManager.empty_list()
                else:
                    RedoManager.redo()
            else:
                try:
                    command, args = self.__general_services.get_command_and_args(command_line)
                    if command not in commands_assignment:
                        raise UnexistingCommand
                    elif command == 'remove' and len(args) != 1 \
                        or command == 'list' and len(args) != 0:
                        raise NotTheRightNumberOfArgs

                    if command != 'add' and command != 'update':
                        RedoManager.save_last_operation(command)
                        commands_assignment[command](*args)

                    else:
                        if command == 'add':
                            id = input('Enter the assignment id:')
                            description = input('Enter the assignment description:')
                            deadline = input('Enter the assignment deadline:')
                            v = DeadlineValidator()
                            v.validate_deadline(deadline)
                            deadline = datetime.strptime(deadline, "%d %B, %Y")
                            RedoManager.save_last_operation(command)
                            commands_assignment[command](id, description, deadline)

                        elif command == 'update':
                            id = input('Enter the assignment id:')
                            new_id = input('Enter the assignment new id:')
                            description = input('Enter the assignment new description:')
                            deadline = input('Enter the assignment new deadline:')
                            v = DeadlineValidator()
                            v.validate_deadline(deadline)
                            deadline = datetime.strptime(deadline, "%d %B, %Y")
                            RedoManager.save_last_operation(command)
                            commands_assignment[command](id, new_id, description, deadline)

                except UnexistingCommand:
                    print('This command is not implemented.')
                except NotTheRightNumberOfArgs:
                    print('Too many/few arguments!')
                except AssignmentValidatorException as a:
                    print(str(a))
                except TimeDataNotMatchFormat as t:
                    print(str(t))
                except IndexError:
                    print('Cannot undo/redo operations.')
                print('\n')

    def run_menu_1(self):
        while True:
            self.print_menu_1()
            choice = input('Choice:')
            if not choice in ['students', 'assignments', 'back']:
                print('Invalid choice!')
            print('\n')
            if choice == 'back':
                break
            elif choice == 'students':
                self.run_menu_students()
            elif choice == 'assignments':
                self.run_menu_assignments()
            print('\n')


    def print_menu_2(self):
        print('- Do you want to give an assignment to:')
        print('1. a student?')
        print('2. a group of students?')
        print('3. back')
        print('*. undo - undo the last given assignment')
        print('**.redo')

    def print_grades(self):
        list_of_grades = self.__grade_service.get_list_of_grades()
        for grade in list_of_grades:
            print(grade)

    def run_menu_2(self):
        print("The existing assignments are:")
        self.print_assignments()
        print('\n')
        print("The students are:")
        self.print_students()
        print('\n')
        self.print_grades()
        print('\n')
        while True:
            self.print_menu_2()
            choice = input()
            if choice == 'back':
                break
            elif choice == 'undo':
                UndoManager.undo()
                RedoManager.save_last_operation(choice)
            elif choice == 'redo':
                if RedoManager.return_last_operation() != "undo":
                    print('Cannot redo operation anymore.')
                    RedoManager.empty_list()
                else:
                    RedoManager.redo()
            elif choice in ['student', 'a student', 'to a student']:
                try:
                    si = input('Enter the student id:')
                    ai = input('Enter the assignment id:')
                    print('\n')
                    n = len(self.__grade_service.get_list_of_grades())
                    self.__grade_service.give_assignment_student(ai, si)
                    m = len(self.__grade_service.get_list_of_grades())
                    if n != m:
                        RedoManager.save_last_operation("give")
                    self.print_grades()
                except GradeValidatorException as g:
                    print(str(g))
            elif choice in ['group', 'a group', 'to a group']:
                try:
                    g = input('Enter the group:')
                    ai = input('Enter the assignment id:')
                    n = len(self.__grade_service.get_list_of_grades())
                    self.__grade_service.give_assignment_group(ai, g)
                    m = len(self.__grade_service.get_list_of_grades())
                    if n != m:
                        RedoManager.save_last_operation("give")
                    self.print_grades()
                except GradeValidatorException as g:
                    print(str(g))
            else:
                print('Invalid choice!')
            print('\n')

    def print_a_students_assignments(self, student_id):
        sv = StudentValidator()
        students = self.__student_service.get_list_of_students()
        try:
            sv.remove_validate(students, student_id)
            list = self.__grade_service.create_list_assignments_for_student(student_id)
            if len(list) !=0:
                print(f"Student {student_id} has the following assignments:")
                for assignment in list:
                    print(assignment.assignment_id)
            else:
                print(f"Student {student_id} has no assignments given.")
        except StudentValidatorException as sve:
            print(str(sve))

    def run_menu_3(self):
        print("The existing assignments are:")
        self.print_grades()
        print('\n')
        student_id = input("Enter the student's id:")
        self.print_a_students_assignments(student_id)
        assignment_id = input("Enter the assignment's id:")
        new_grade_value = input("Enter the grade:")
        try:
            self.__grade_service.grade_student(student_id, assignment_id, new_grade_value)
            self.print_grades()
            print('\n')
        except GradeValidatorException as g:
            print(str(g))

    def print_students(self):
        students = self.__student_service.get_list_of_students()
        for student in students:
            print(student)

    def print_assignments(self):
        assignments = self.__assignment_service.get_list_of_assignments()
        for assignment in assignments:
            print(assignment)

    def print_statistics(self):
        print("1. All students who received a given assignment, ordered descending by grade.")
        print("2. All students who are late in handing in at least one assignment.")
        print("3. Students with the best school situation, sorted in descending order.")
        print("4. back")

    def print_students_with_assignment(self, assignment_id):
        list = self.__grade_service.students_with_given_assignment(assignment_id)
        for student in list:
            print('Id:', student, ', Name:', self.__student_service.get_name_from_id(int(student)),
                  ', Grade:', self.__grade_service.get_grade_value(assignment_id, student))

    def print_late_students(self):
        list = self.__grade_service.late_students()
        print("Today is", date.today(), '.')
        if len(list) > 0:
            print('The students who are late with the assignments are:')
            for grade in list:
                print('Id student:', grade.student_id, ', Id assignment:', grade.assignment_id, ', Deadline:', self.__assignment_service.get_deadline(grade.assignment_id))
        else:
            print('There is no student who is late with at least one assignment.')

    def print_students_situation(self):
        list_of_students = self.__grade_service.sort_students_by_their_grades()
        for student in list_of_students:
            grade = self.__grade_service.average_grade_for_student(student.student_id)
            if grade != -1:
                print(f'The average grade for {student.student_id} is', grade, '.')
            else:
                print(f'Student {student.student_id} has no grades.')

    def run_menu_4(self):
        while True:
            self.print_statistics()
            choice = input('Enter your choice:')
            if choice == '1':
                given_id = input("The assignment id:")
                try:
                    a = AssignmentValidator()
                    a.validate_assignment_id(given_id)
                    self.print_students_with_assignment(given_id)
                except AssignmentValidatorException as av:
                    print(str(av))
            elif choice == '2':
                self.print_late_students()
            elif choice == '3':
                self.print_students_situation()
            elif choice == 'back':
                break
            else:
                print('Invalid choice!')

    def run(self):
        #self.__student_service.first_20_students()
        #self.__assignment_service.first_20_assignments()
        #self.__grade_service.first_10_assignments()
        #self.__grade_service.first_5_grades()
        while True:
            try:
                self.print_main_menu()
                first_choice = input('Choice:')
                print('\n')
                if first_choice == 'exit':
                    break
                elif first_choice == 'manage':
                    self.run_menu_1()
                elif first_choice == 'give':
                    self.run_menu_2()
                elif first_choice == 'grade':
                    self.run_menu_3()
                elif first_choice == 'view':
                    self.run_menu_4()
                elif first_choice == 'undo':
                    RedoManager.save_last_operation(first_choice)
                    UndoManager.undo()
                elif first_choice == 'redo':
                    if RedoManager.return_last_operation() != "undo":
                        print('Cannot redo operation anymore.')
                        RedoManager.empty_list()
                    else:
                        RedoManager.redo()
                else:
                    print('Invalid choice!')
            except IndexError:
                print('Cannot undo/redo operation.')
            except GradeValidatorException as g:
                print(str(g))
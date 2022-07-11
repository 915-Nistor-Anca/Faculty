from src.domain.domain import Student, Assignment, Grade
import random
from datetime import datetime, date

from src.undo_redo.undo import UndoManager
from src.undo_redo.redo import RedoManager
from src.undo_redo.handlers import UndoHandlers, RedoHandlers

class StudentService:
    def __init__(self, s_repository, g_repository):
        self.__s_repository = s_repository
        self.__g_repository = g_repository

    def add_student_undo(self, student_id, name, group):
        """
        This function creates a student with the given information and adds it to the list.
        :param student_id: integer
        :param name: string
        :param group: integer
        """
        new_student = Student(student_id, name, group)
        self.__s_repository.add(new_student)
        #RedoManager.register_operation(self, RedoHandlers.ADD_S, student_id)

    def add_student(self, student_id, name, group):
        """
        This function creates a student with the given information and adds it to the list.
        :param student_id: integer
        :param name: string
        :param group: integer
        """
        new_student = Student(student_id, name, group)
        self.__s_repository.add(new_student)
        UndoManager.register_operation(self, UndoHandlers.ADD_STUDENT, student_id)

    def update_student_undo(self, student_id, new_student_id, new_name, new_group):
        """
        This function modifies a student.
        If it finds a student with the given id, it changes its old id, name and group with the new ones.
        :param student_id: integer
        :param new_student_id: integer
        :param new_name: string
        :param new_group: integer
        """
        name = self.__s_repository.find_name_from_id(student_id)
        group = self.__s_repository.find_group_from_id(student_id)
        new_student_data = Student(new_student_id, new_name, new_group)
        self.__s_repository.update(student_id, new_student_data)
        RedoManager.register_operation(self, RedoHandlers.UPDATE_S, new_student_id, student_id, name, group)

    def update_student(self, student_id, new_student_id, new_name, new_group):
        """
        This function modifies a student.
        If it finds a student with the given id, it changes its old id, name and group with the new ones.
        :param student_id: integer
        :param new_student_id: integer
        :param new_name: string
        :param new_group: integer
        """
        name = self.__s_repository.find_name_from_id(student_id)
        group = self.__s_repository.find_group_from_id(student_id)
        new_student_data = Student(new_student_id, new_name, new_group)
        self.__s_repository.update(student_id, new_student_data)
        UndoManager.register_operation(self, UndoHandlers.UPDATE_STUDENT, new_student_id, student_id, name, group)

    def remove_student_undo(self, student_id):
        """
        This function removes the student whose id is the same as the given one.
        :param student_id: integer
        """
        name = self.__s_repository.find_name_from_id(student_id)
        group = self.__s_repository.find_group_from_id(student_id)
        self.__s_repository.remove(student_id)
        self.delete_assignments_of_a_deleted_student_undo(student_id)
        RedoManager.register_operation(self, RedoHandlers.REMOVE_S, student_id, name, group)

    def remove_student(self, student_id):
        """
        This function removes the student whose id is the same as the given one.
        :param student_id: integer
        """
        name = self.__s_repository.find_name_from_id(student_id)
        group = self.__s_repository.find_group_from_id(student_id)
        self.__s_repository.remove(student_id)
        #UndoManager.register_operation(self, UndoHandlers.REMOVE_STUDENT, student_id, name, group)

    def get_list_of_students(self):
        """
        :return: the list of students
        """
        list = self.__s_repository.get_all()
        return list

    def delete_assignments_of_a_deleted_student_undo(self, student_id):
        list = self. __g_repository.get_all()
        list_of_grades = []
        for grade in list:
            if str(student_id) == str(grade.student_id):
                list_of_grades.append(grade)
                self.__g_repository.remove(grade.assignment_id, student_id)

    def delete_assignments_of_a_deleted_student(self, student_id):
        list = self. __g_repository.get_all()
        list_of_grades = []
        for grade in list:
            if str(student_id) == str(grade.student_id):
                list_of_grades.append(grade)
                self.__g_repository.remove(grade.assignment_id, student_id)
        return list_of_grades

    def remove_student_and_delete_assignments(self, student_id):
        name = self.__s_repository.find_name_from_id(student_id)
        group = self.__s_repository.find_group_from_id(student_id)
        self.remove_student(student_id)
        list_of_grades = self.delete_assignments_of_a_deleted_student(student_id)
        UndoManager.register_operation(self, UndoHandlers.DELETE_ASSIGNMENTS, student_id, name, group, self.__g_repository,
                                       list_of_grades)

    def remove_student_and_delete_assignments_redo(self, student_id):
        RedoManager.register_operation(self, RedoHandlers.REMOVE_STUDENT_DELETE_ASSIGNMENTS, student_id)

    def first_20_students(self):
        """
        This function randomly generates the first 20 students of the list.
        It takes a name and a group from the corresponding lists, generates a random number and makes sure that the number
        and the name are unique. If they are, it adds a new student. The number will be the id.
        In order not to be repeated, the number and the name are stored.
        This process is done 20 times.
        """
        names = ['Anna', 'Mary', 'Elena', 'Fiona', 'Tiana', 'Susan', 'Sabrina', 'Tony', 'Jack', 'Tom', 'Ben', 'Dan',
                 'Lana', 'Steve', 'Zoe', 'Amy', 'Roger', 'Aurora', 'Liam', 'Emma', 'Nicholas', 'Andrew', 'Lily']
        groups = [911, 912, 913, 914, 915, 916, 917]
        used_names = []
        used_numbers = []
        k = 0
        while (k < 20):
            number = random.randint(1000, 9999)
            name = random.choice(names)
            group = random.choice(groups)
            if not number in used_numbers and not name in used_names:
                self.add_student(number, name, group)
                used_numbers.append(number)
                used_names.append(name)
                k += 1

    def get_name_from_id(self, student_id):
        list = self.__s_repository.get_all()
        for s in list:
            if str(s.student_id) == str(student_id):
                return s.name

class AssignmentService:
    def __init__(self, a_repository, s_repository, g_repository):
        self.__a_repository = a_repository
        self.__s_repository = s_repository
        self.__g_repository = g_repository

    def add_assignment_undo(self, assignment_id, description, deadline):
        """
        This function adds a new assignment.
        :param assignment_id: integer
        :param description: string
        :param deadline: string
        """
        new_assignment = Assignment(assignment_id, description, str(deadline))
        self.__a_repository.add(new_assignment)
        #RedoManager.register_operation(self, RedoHandlers.ADD_A, assignment_id)

    def add_assignment(self, assignment_id, description, deadline):
        """
        This function adds a new assignment.
        :param assignment_id: integer
        :param description: string
        :param deadline: string
        """
        new_assignment = Assignment(assignment_id, description, str(deadline))
        self.__a_repository.add(new_assignment)
        UndoManager.register_operation(self, UndoHandlers.ADD_ASSIGNMENT, assignment_id)

    def update_assignment_undo(self, assignment_id, new_assignment_id, new_description, new_deadline):
        """
        This function updates an assignment.
        :param assignment_id: an integer
        :param new_assignment_id: an integer
        :param new_description: a string
        :param new_deadline: a date
        """
        new_assignment_data = Assignment(new_assignment_id, new_description, new_deadline)
        description = self.__a_repository.get_description_of_an_assignment(assignment_id)
        deadline = self.__a_repository.get_deadline_of_an_assignment(assignment_id)
        self.__a_repository.update(assignment_id, new_assignment_data)
        RedoManager.register_operation(self, RedoHandlers.UPDATE_A, new_assignment_id, assignment_id, description, deadline)

    def update_assignment(self, assignment_id, new_assignment_id, new_description, new_deadline):
        """
        This function updates an assignment.
        :param assignment_id: an integer
        :param new_assignment_id: an integer
        :param new_description: a string
        :param new_deadline: a date
        """
        new_assignment_data = Assignment(new_assignment_id, new_description, new_deadline)
        description = self.__a_repository.get_description_of_an_assignment(assignment_id)
        deadline = self.__a_repository.get_deadline_of_an_assignment(assignment_id)
        self.__a_repository.update(assignment_id, new_assignment_data)
        UndoManager.register_operation(self, UndoHandlers.UPDATE_ASSIGNMENT, new_assignment_id, assignment_id, description, deadline)

    def remove_assignment_undo(self, assignment_id):
        """
        This function removes the assignment which has the given id.
        :param assignment_id: integer
        """
        description = self.__a_repository.get_description_of_an_assignment(assignment_id)
        deadline = self.__a_repository.get_deadline_of_an_assignment(assignment_id)
        self.__a_repository.remove(assignment_id)
        #RedoManager.register_operation(self, RedoHandlers.REMOVE_A, assignment_id, description, deadline)

    def remove_assignment(self, assignment_id):
        """
        This function removes the assignment which has the given id.
        :param assignment_id: integer
        """
        description = self.__a_repository.get_description_of_an_assignment(assignment_id)
        deadline = self.__a_repository.get_deadline_of_an_assignment(assignment_id)
        self.__a_repository.remove(assignment_id)
        #UndoManager.register_operation(self, UndoHandlers.REMOVE_ASSIGNMENT, assignment_id, description, deadline)

    def delete_grades_for_deleted_assignment(self, assignment_id):
        """
        This function deletes the grades which have the given assignment.
        :param assignment_id: an integer
        """
        list = self.__g_repository.get_all()
        list_of_removed_grades = []
        for grade in list:
            if str(assignment_id) == str(grade.assignment_id):
                list_of_removed_grades.append(grade)
                self.__g_repository.remove(assignment_id, grade.student_id)
        return list_of_removed_grades
        #UndoManager.register_operation(self, UndoHandlers.DELETE_ASSIGNMENTS, self.__g_repository, list_of_removed_grades)

    def remove_assignment_delete_grades(self, assignment_id):
        """
        This function removes an assignment and then all the grades which were given for that assignment.
        :param assignment_id: an integer
        """
        description = self.__a_repository.get_description_of_an_assignment(assignment_id)
        deadline = self.__a_repository.get_deadline_of_an_assignment(assignment_id)
        self.remove_assignment(assignment_id)
        list_of_grades = self.delete_grades_for_deleted_assignment(assignment_id)
        UndoManager.register_operation(self, UndoHandlers.DELETE_ASSIGNMENT_GRADES, assignment_id, description,
                                       deadline, self.__g_repository, list_of_grades)

    def remove_assignment_delete_grades_undo(self, assignment_id):
        RedoManager.register_operation(self, RedoHandlers.REMOVE_ASSIGNMENTS_DELETE_GRADES, assignment_id)

    def first_20_assignments(self):
        """
        This function creates the first 20 assignments.
        :return:
        """
        descriptions = ['Find 10 animals which hibernate.', 'Draw a pyramid.',
                        'Prove that any even number > 2 is not prime.', 'Make a PowerPoint presentation about Ireland.',
                        'Write an essay about human rights.', 'Compose a song.',
                        'Draw the components of a human cell.', 'Find a ∈ R such that a+ 130 = 14a - 20.',
                        'Write a C++ program which checks if a number is prime or not.',
                        'Imagine you are a bird for a day. Write 5 things you would want to try.',
                        'Film yourself while doing 50 genuflexions.', 'Draw a cow.',
                        'Record yourself while singing a song.', 'Try to reproduce Mona Lisa painting.',
                        'Open the dictionary and write 15 unknown words and their meaning.',
                        'Write an essay about Albert Einstein.', 'Create your own blog.',
                        'Make a list of all european countries and their capital.',
                        'Write the solution to the next problem: What is the energy of an electron in the 𝑛=3 energy state of a hydrogen atom?',
                        'Study The Collatz Conjecture and implement a Python program for it.', 'Write an essay about global warming.']
        deadlines = ['19 December, 2021', '21 August, 2020', '1 January, 2022', '13 January, 2022', '20 December, 2021', '23 January, 2022',
                     '15 November, 2021', '15 September, 2020', '12 August, 2018', '13 September, 2021', '20 October, 2021']
        used_descriptions = []
        used_ids = []
        k = 0
        while k < 20:
            id = random.randint(100, 999)
            description =random.choice(descriptions)
            deadline = random.choice(deadlines)
            deadline = datetime.strptime(deadline, "%d %B, %Y")
            if not id in used_ids and not description in used_descriptions:
                self.add_assignment(id, description, deadline)
                used_ids.append(id)
                used_descriptions.append(description)
                k += 1

    def get_list_of_assignments(self):
        """
        :return: the list of assignments
        """
        list = self.__a_repository.get_all()
        return list

    def get_deadline(self, assignment_id):
        """
        :param assignment_id: an integer
        :return: the deadline of an assignment
        """
        return self.__a_repository.get_deadline_of_an_assignment(assignment_id)


class GradeService:
    def __init__(self, s_repo, a_repo, g_repo):
        self.__s_repo = s_repo
        self.__a_repo = a_repo
        self.__g_repo = g_repo

    def add_grade(self, assignment_id, student_id, grade_value):
        """
        This function adds a grade to the list of grades.
        :param assignment_id: integer
        :param student_id: integer
        :param grade_value: integer
        """
        grade = Grade(assignment_id, student_id, grade_value)
        self.__g_repo.add(grade)
        if int(grade_value) != -1 and str(assignment_id).isdigit() and str(student_id).isdigit():
            UndoManager.register_operation(self, UndoHandlers.ADD_GRADE, student_id, assignment_id)

    def make_minus_one(self, student_id, assignment_id):
        self.__g_repo.change_a_grade(student_id, assignment_id, -1)

    def remove_grade(self, assignment_id, student_id):
        """
        This function removes a grade from the list.
        The grade's assignment id and the student id are given. It eliminates the grade which has the same value as those.
        :param assignment_id: integer
        :param student_id: integer
        """
        self.__g_repo.remove(assignment_id, student_id)

    def get_list_of_grades(self):
        """
        :return: the list of grades
        """
        list = self.__g_repo.get_all()
        return list

    def check_if_assignment_not_given_to_student(self, assignment_id, student_id):
        """
        This function checks if the assignment the user wants to give to a student isn't already given to him.
        :param assignment_id: integer
        :param student_id: integer
        :return: True, if the assignment is not given to the student and False, if it is
        """
        list = self.get_list_of_grades()
        for grade in list:
            if str(grade.assignment_id) == str(assignment_id) and str(grade.student_id) == str(student_id):
                return False
        return True

    def check_if_assignment_exists(self, id):
        """
        This function checks if there exists an assignment with the given id.
        :param id: integer
        :return: True, if the assingment exists and False, if not
        """
        for assignment in self.__a_repo.get_all():
            if str(assignment.assignment_id) == str(id):
                return True
        return False

    def check_if_student_exists(self, id):
        """
        This function checks if there exists a student with the given id.
        :param id: integer
        :return: True, if the student exists and False, if not
        """
        for student in self.__s_repo.get_all():
            if str(student.student_id) == str(id):
                return True
        return False

    def give_assignment_student(self, assignment_id, student_id):
        """
        This function gives an assignment to a student, if the assignment and the student exist and the student didn't
        already received that particular assignment.
        :param assignment_id: integer
        :param student_id: integer
        """
        if (self.check_if_assignment_not_given_to_student(assignment_id, student_id)):
            if self.check_if_student_exists(student_id) and self.check_if_assignment_exists(assignment_id):
                self.add_grade(assignment_id, student_id, -1)
                UndoManager.register_operation(self, UndoHandlers.DELETE_GIVEN_ASSIGNMENT, student_id, assignment_id)

    def give_assignment_student_redo(self, assignment_id, student_id):
        RedoManager.register_operation(self, RedoHandlers.GIVE_ASSIGNMENT_STUDENT, assignment_id, student_id)

    def give_assignment_student0(self, assignment_id, student_id):
        """
        This function gives an assignment to a student, if the assignment and the student exist and the student didn't
        already received that particular assignment.
        :param assignment_id: integer
        :param student_id: integer
        """
        if (self.check_if_assignment_not_given_to_student(assignment_id, student_id)):
            if self.check_if_student_exists(student_id) and self.check_if_assignment_exists(assignment_id):
                self.add_grade(assignment_id, student_id, -1)

    def delete_given_assignment(self, student_id, assignment_id):
        self.__g_repo.remove_last_given_assignment_ungraded()

    def give_assignment_group(self, assignment_id, group):
        """
        This function gives an assignment to every student which is part of the given group.
        :param assignment_id: integer
        :param group: integer
        """
        list = self.__s_repo.get_all()
        l = [] #in order to undo the operation only for the students which were given the assignment the last time
        #(a student who had received an assignment before won't be removed the assignment)
        n = len(self.__g_repo.get_all())
        for student in list:
            if str(student.group) == str(group):
                self.give_assignment_student0(assignment_id, student.student_id)
                if len(self.__g_repo.get_all()) > n:
                    n+=1
                    l.append(student.student_id)
        if len(l)>0: #if there exists a modification which has to be saved
            UndoManager.register_operation(self, UndoHandlers.GIVE_ASSIGNMENT_GROUP, assignment_id, group, l)

    def give_assignment_group_undo(self, assignment_id, group):
        RedoManager.register_operation(self, RedoHandlers.GIVE_ASSIGNMENT_GROUP, assignment_id, group)

    def remove_assignment_group(self, assignment_id, group, l):
        list = self.__g_repo.get_all()
        for grade in list:
            g = self.__s_repo.find_group_from_id(grade.student_id)
            if str(grade.assignment_id) == str(assignment_id) and str(g) == str(group) and grade.student_id in l:
                self.remove_grade(assignment_id, grade.student_id)


    def create_list_assignments_for_student(self, student_id):
        """
        This function creates a list with all the assignments a student has (and their grade, if it's graded).
        :param student_id: an integer
        :return: the list of assignments (both graded and ungraded)
        """
        grades = self.__g_repo.get_all()
        list = []
        for grade in grades:
            if str(grade.student_id) == str(student_id):
                list.append(grade)
        return list

    def get_deadline(self, assignment_id):
        list = self.__a_repo.get_all()
        for a in list:
            if str(a.assignment_id) == str(assignment_id):
                return a.deadline

    def grade_student0(self, student_id, assignment_id, grade_value):
        """
        This function grades an assignment a student has.
        It searches in the list of assignments a student has and grades the one which has the same id as the given
        assignment id. The grade will have now the given value.
        :param student_id: an integer
        :param assignment_id: an integer
        :param grade_value: an integer
        """
        list = self.create_list_assignments_for_student(student_id)
        for grade in list:
            if str(grade.assignment_id) == str(assignment_id):
                self.__g_repo.grade(grade, grade_value)
                break


    def grade_student(self, student_id, assignment_id, grade_value):
        """
        This function grades an assignment a student has.
        It searches in the list of assignments a student has and grades the one which has the same id as the given
        assignment id. For this function, it is important that the student is not late with the assignment.
        Only the assignments which aren't turned in late can be graded. The grade will have now the given value.
        :param student_id: an integer
        :param assignment_id: an integer
        :param grade_value: an integer
        """
        list = self.create_list_assignments_for_student(student_id)
        for grade in list:
            if str(grade.assignment_id) == str(assignment_id) and self.deadline_has_passed(self.get_deadline(assignment_id))==0:
                self.__g_repo.grade(grade, grade_value)
                UndoManager.register_operation(self, UndoHandlers.ADD_GRADE, student_id, assignment_id, grade_value)
                break

    def grade_student_undo(self, student_id, assignment_id, grade_value):
        list = self.create_list_assignments_for_student(student_id)
        for grade in list:
            if str(grade.assignment_id) == str(assignment_id) and self.deadline_has_passed(
                    self.get_deadline(assignment_id)) == 0:
                self.__g_repo.grade(grade, grade_value)
                UndoManager.register_operation(self, UndoHandlers.ADD_GRADE, student_id, assignment_id, grade_value)
                break

    def grade_student_redo(self, student_id, assignment_id, grade_value):
        RedoManager.register_operation(self, RedoHandlers.CHANGE_GRADE_HANDLER, student_id, assignment_id, grade_value)

    def first_10_assignments(self):
        """
        This function randomly generates the first 10 assignments for some students.
        """
        students_list = self.__s_repo.get_all()
        assignments_list = self.__a_repo.get_all()
        k = len(self.__g_repo.get_all())
        while k < 10:
            student = random.choice(students_list)
            assignment = random.choice(assignments_list)
            self.give_assignment_student(assignment.assignment_id, student.student_id)
            k = len(self.__g_repo.get_all())

    def first_5_grades(self):
        """
        This function grades 5 random assignments. An assignment can be graded if and only if it wasn't graded before.
        """
        grades_list = self.__g_repo.get_all()
        grades = [5, 6, 7, 8, 9, 10]
        k = 0
        while k < 5:
            random_assignment_to_be_graded = random.choice(grades_list)
            if int(random_assignment_to_be_graded.grade_value) == int(-1):
                self.grade_student0(int(random_assignment_to_be_graded.student_id),
                                   int(random_assignment_to_be_graded.assignment_id), int(random.choice(grades)))
                k += 1

    def get_grade_value(self, assignment_id, student_id):
        """
        This function receives as parameters an assignment id and a student id and searches (in the list of grades) an
        assignment which has the same ids as the given ones. If it finds it, it returns its grade value.
        :param assignment_id: an integer
        :param student_id: an integer
        :return: the grade value, if the grade can be found, or -1
        """
        grades = self.__g_repo.get_all()
        for g in grades:
            if str(g.assignment_id) == str(assignment_id) and g.student_id == student_id:
                return g.grade_value

    def students_with_given_assignment(self, assignment_id):
        """
        This function uses bubble sort to create a list with the students who have received the assignment which has the
        given id. It sorts the list descending by their grades.
        :param assignment_id: an integer
        :return: the ordered list of students which have the assignment given.
        """
        grades = self.__g_repo.get_all()
        students_with_this_assignment = []
        for grade in grades:
            if str(grade.assignment_id) == str(assignment_id):
                students_with_this_assignment.append(grade.student_id)

        ok = 1
        for i in range(0, len(students_with_this_assignment)-1):
            if int(self.get_grade_value(assignment_id, students_with_this_assignment[i])) \
                < int(self.get_grade_value(assignment_id, students_with_this_assignment[i+1])):
                ok = 0
                aux = students_with_this_assignment[i]
                students_with_this_assignment[i] = students_with_this_assignment[i+1]
                students_with_this_assignment[i+1] = aux
        while ok == 0:
            ok = 1
            for i in range(0, len(students_with_this_assignment) - 1):
                if int(self.get_grade_value(assignment_id, students_with_this_assignment[i])) \
                        < int(self.get_grade_value(assignment_id, students_with_this_assignment[i + 1])):
                    ok = 0
                    aux = students_with_this_assignment[i]
                    students_with_this_assignment[i] = students_with_this_assignment[i + 1]
                    students_with_this_assignment[i + 1] = aux
        return students_with_this_assignment


    def deadline_has_passed(self, deadline):
        """
        This function checkes if the given deadline has passed.
        A deadline has passed if it is smaller than today's date.
        :param deadline: a date
        :return: True, if the deadline has passed and False, in the contrary
        """
        today = date.today()
        today = today.strftime("%Y-%m-%d %H:%M:%S")
        if deadline < today:
            return 1
        else:
            return 0

    def late_students(self):
        """
        This function creates a list with the students who are late in turning in their assignments.
        A student is late with an assignment if its deadline has passed and it is still not graaded (grade value is -1).
        :return: the list of late students
        """
        list = []
        list_of_grades = self.get_list_of_grades()
        for grade in list_of_grades:
            assignment = grade.assignment_id
            deadline = self.__a_repo.get_deadline_of_an_assignment(assignment)
            if self.deadline_has_passed(deadline) and int(grade.grade_value) == int(-1):
                list.append(grade)
        return list


    def average_grade_for_student(self, student_id):
        """
        This function calculates the average grade for a student.
        It counts how many assignments he/she has which are graded and sums them, but also it takes in consideration those
        assignments who are not graded and for which their deadline has passed (meaning the student didn't turn in that
        assignment when he/she should. An ungraded delayed assignment is equivalent to the grade 0.
        :param student_id: an integer
        :return: the average grade for a student, type float
        """
        list_of_grades = self.get_list_of_grades()
        number_of_grades = 0
        grades = 0
        for grade in list_of_grades:
            if str(grade.student_id) == str(student_id):
                deadline = self.__a_repo.get_deadline_of_an_assignment(grade.assignment_id)
                if self.deadline_has_passed(deadline) and int(grade.grade_value) == -1:
                    number_of_grades += 1
                else:
                    if int(grade.grade_value) != -1:
                        number_of_grades += 1
                        grades += int(grade.grade_value)
        if number_of_grades != 0:
            return float(float(grades)/float(number_of_grades))
        else:
            return -1

    def sort_students_by_their_grades(self):
        """
        This function uses bubble sort to order the existing students. It orders them descending by their average grade.
        :return: the list of sorted students
        """
        list_of_students = self.__s_repo.get_all()
        ok = 1
        for i in range(0, len(list_of_students)-1):
            if self.average_grade_for_student(list_of_students[i].student_id) < \
                self.average_grade_for_student(list_of_students[i+1].student_id):
                ok = 0
                aux = list_of_students[i]
                list_of_students[i] = list_of_students[i+1]
                list_of_students[i+1] = aux
        while ok == 0:
            ok = 1
            for i in range(0, len(list_of_students)-1):
                if self.average_grade_for_student(list_of_students[i].student_id) < \
                        self.average_grade_for_student(list_of_students[i + 1].student_id):
                    ok = 0
                    aux = list_of_students[i]
                    list_of_students[i] = list_of_students[i + 1]
                    list_of_students[i + 1] = aux
        return list_of_students

class GeneralServices:
    def remove_useless_spaces(self, command_line):
        """
        This function receives a command line and removes any extra space which might appear between words or at the
        beggining / end of the command.
        :param command_line: string
        :return: the new command line, without the useless spaces
        """
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
        """
        This function separates the command from the args from a command line.
        :param command_line: string
        :return: the command and the arguments
        """
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


class StudentRepository:
    def __init__(self, validator):
        self.__students = []
        self.__validator = validator

    def add(self, student):
        """
        This function receives a student and adds it to the list of students.
        :param student: a class
        """
        self.__validator.validate(student, self.__students)
        self.__students.append(student)

    def remove(self, student_id):
        """
        This function searches for the student which has the given id in the list of students and deletes it (if it can be found).
        :param student_id: an integer
        """
        self.__validator.remove_validate(self.__students, student_id)
        for student in self.__students:
            if str(student.student_id) == str(student_id):
                self.__students.remove(student)
                break

    def update(self, student_id, student):
        """
        This function receives an id and the new student and replaces the data of the student which has the given id
        with the new student's data.
        :param student_id: an integer
        :param student: a class
        """
        self.__validator.validate_update(student.student_id, student.group, self.__students)
        for s in self.__students:
            if str(s.student_id) == str(student_id):
                s.student_id = student.student_id
                s.name = student.name
                s.group = student.group
                break

    def get_all(self):
        """
        :return: the list of students
        """
        return list(self.__students)

    def __len__(self):
        return len(self.__students)

    def find_name_from_id(self, student_id):
        for s in self.__students:
            if str(s.student_id) == str(student_id):
                return s.name

    def find_group_from_id(self, student_id):
        for s in self.__students:
            if str(s.student_id) == str(student_id):
                return s.group

class AssignmentRepository:
    def __init__(self, validator):
        self.__assignments = []
        self.__validator = validator

    def add(self, assignment):
        """
        This function adds the received assignment to the list of assignments.
        :param assignment: a class
        """
        self.__validator.validate(assignment, self.__assignments)
        self.__assignments.append(assignment)

    def remove(self, assignment_id):
        """
        This function removes the assignment which has the given id.
        :param assignment_id: an integer
        """
        self.__validator.remove_validate(self.__assignments, assignment_id)
        for assignment in self.__assignments:
            if int(assignment.assignment_id) == int(assignment_id):
                self.__assignments.remove(assignment)
                break

    def update(self, assignment_id, assignment):
        """
        This function modifies an assignment. It is given the id of the assignment which has to be modified.
        The assignment will have the same informations as the given assignment.
        :param assignment_id:
        :param assignment:
        :return:
        """
        self.__validator.validate_update(assignment.assignment_id, self.__assignments)
        for a in self.__assignments:
            if int(a.assignment_id) == int(assignment_id):
                a.assignment_id = assignment.assignment_id
                a.description = assignment.description
                a.deadline = assignment.deadline
                break

    def get_all(self):
        """
        :return: the list of assignments
        """
        return list(self.__assignments)

    def get_deadline_of_an_assignment(self, assignment_id):
        list = self.__assignments
        self.__validator.remove_validate(list, assignment_id)
        for assignment in list:
            if str(assignment.assignment_id) == str(assignment_id):
                return assignment.deadline

    def get_description_of_an_assignment(self, assignment_id):
        list = self.__assignments
        self.__validator.remove_validate(list, assignment_id)
        for assignment in list:
            if str(assignment.assignment_id) == str(assignment_id):
                return assignment.description

    def __len__(self):
        return len(self.__assignments)

class GradeRepository:
    def __init__(self, validator):
        self.__grades = []
        self.__validator = validator

    def add(self, grade):
        """
        This function adds a grade to the list of grades.
        :param grade: a class
        """
        self.__validator.validate(grade)
        self.__grades.append(grade)


    def find_grade_value(self, student_id, assignment_id):
        for grade in self.__grades:
            if int(grade.assignment_id) == int(assignment_id) and int(grade.student_id) == int(student_id):
                return grade.grade_value

    def change_a_grade(self, student_id, assignment_id, new_grade_value):
        for grade in self.__grades:
            if int(grade.assignment_id) == int(assignment_id) and int(grade.student_id) == int(student_id):
                grade.grade_value = new_grade_value

    def remove(self, assignment_id, student_id):
        """
        This function removes one of the assignments given to a student.
        :param assignment_id: an integer
        :param student_id: an integer
        """
        for grade in self.__grades:
            if int(grade.assignment_id) == int(assignment_id) and int(grade.student_id) == int(student_id):
                self.__grades.remove(grade)
                break

    def remove_last_given_assignment_ungraded(self):
        self.__grades.pop()

    def grade(self, grade, new_value):
        self.__validator.grade_assignment_validate(grade.student_id, grade.assignment_id, self.__grades, new_value)
        for g in self.__grades:
            if str(g.assignment_id) == str(grade.assignment_id) and str(g.student_id) == str(grade.student_id):
                g.grade_value = new_value
                break


    def get_all(self):
        """
        :return: the list of grades
        """
        return list(self.__grades)

    def __len__(self):
        return len(self.__grades)
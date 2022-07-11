class Error(Exception):
    pass

class UnexistingCommand(Error):
    pass

class NotTheRightNumberOfArgs(Error):
    pass

class TimeDataNotMatchFormat(Error):
    pass

class DeadlineValidator:
    def validate_deadline(self, deadline):
        """
            This function checks if the written deadline is valid or not.
    A valid deadline has the format 'day Month, year'.
    The day should not be grater than 31 or smaller than 1.
    The month has to be an existing one.
        :param deadline: string
        """
        pos = deadline.find(' ')
        day = deadline[:pos]

        deadline = deadline[pos+1:]
        pos = deadline.find(' ')
        month = deadline[:pos-1]

        deadline =deadline[pos+1:]
        year = deadline

        if str(day).isdigit() == False or str(year).isdigit() == False:
            raise TimeDataNotMatchFormat('The day and the year of the deadline must be integers!')

        if int(day) < 1 or int(day) > 31:
            raise TimeDataNotMatchFormat("There is no such day as the deadline's day.")

        if str(month) not in ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']:
            raise TimeDataNotMatchFormat("The deadline's month does not exist.")


class StudentValidatorException(Error):
    pass

class StudentValidator:
    def validate(self, student, students):
        """
        This function validates the student's data.
        The id and the value must be integers.
        Two students cannot have the same id.
        """
        if not str(student.student_id).isdigit() or not str(student.group).isdigit():
            raise StudentValidatorException('The student id and the group must be integers!')
        for s in students:
            if str(s.student_id) == str(student.student_id):
                raise StudentValidatorException(f'Two students cannot have the same id! ({s.name} has this id.)')

    def validate_update(self, new_id, new_group, students):
        for student in students:
            if str(student.student_id) == str(new_id):
                raise StudentValidatorException(f'This id is already used by another student: {student.name}')

        if not str(new_id).isdigit() or not str(new_group).isdigit():
            raise StudentValidatorException('The new student id and the new group must be integers!')

    def remove_validate(self, students, student_id):
        ok = 0
        for student in students:
            if str(student.student_id) == str(student_id):
                ok = 1
        if ok == 0:
            raise StudentValidatorException('There is no student with such id. Nothing changes.')

class AssignmentValidatorException(Error):
    pass

class AssignmentValidator:
    def validate(self, assignment, assignments):
        if not str(assignment.assignment_id).isdigit():
            raise AssignmentValidatorException('The assignment id must be an integer!')
        for a in assignments:
            if str(a.assignment_id) == str(assignment.assignment_id):
                raise AssignmentValidatorException('Two assignments cannot have the same id!')

    def validate_update(self, new_id, assignments):
        for assignment in assignments:
            if str(assignment.assignment_id) == str(new_id):
                raise AssignmentValidatorException(f'This id is already used by another assignment, having the description: {assignment.description}')

        if not str(new_id).isdigit():
            raise AssignmentValidatorException('The new assignment id must be an integer!')

    def remove_validate(self, assignments, assignment_id):
        ok = 0
        for assignment in assignments:
            if str(assignment.assignment_id) == str(assignment_id):
                ok = 1
        if ok == 0:
            raise AssignmentValidatorException('There is no assignment with such id.')

    def validate_assignment_id(self, assignment_id):
        if str(assignment_id).isdigit() == False:
            raise AssignmentValidatorException('The id must be an integer!')

class GradeValidatorException(Error):
    pass

class GradeValidator:
    def validate(self, grade):
        if grade.grade_value == -1:
            if not str(grade.assignment_id).isdigit() or not str(grade.student_id).isdigit():
                raise GradeValidatorException('Ids and grade value must be integers!')
        elif not str(grade.assignment_id).isdigit() or not str(grade.student_id).isdigit() or not str(grade.grade_value).isdigit():
            raise GradeValidatorException('Ids and grade value must be integers!')

    def grade_assignment_validate(self, student_id, assignment_id, grades, new_value):
        if str(new_value).isdigit() == 0:
            raise GradeValidatorException("The new assignment's grade has to be an integer!")
        for grade in grades:
            if str(grade.assignment_id) == str(assignment_id) and str(grade.student_id) == str(student_id):
                if grade.grade_value != -1:
                    raise GradeValidatorException('Once graded, the grade value of an assignment cannot be modified!')
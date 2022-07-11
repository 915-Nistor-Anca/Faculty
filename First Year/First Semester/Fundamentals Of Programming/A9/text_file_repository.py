from src.repository.repository import StudentRepository, AssignmentRepository, GradeRepository
from src.domain.domain import Grade
class StudentFileRepository(StudentRepository):
    def __init__(self, validator_class, file_name, entity_class):
        super().__init__(validator_class)
        self.__file_name = file_name
        self.__entity_class = entity_class
        self.__load_data()

    def __load_data(self):
        with open(self.__file_name) as file_pointer:
            for line in file_pointer:
                student = self.__entity_class.read_from(self.__entity_class, line)
                if student != -1:
                    super().add(student)

    def add(self, student):
        super().add(student)
        self.__save_to_file(student)

    def remove(self, student_id):
        super().remove(student_id)
        lines = open(self.__file_name).readlines()
        k = 0
        with open(self.__file_name) as file_pointer:
            for line in file_pointer:
                student = self.__entity_class.read_from(self.__entity_class, line)
                if student != -1:
                    if int(student.student_id) == int(student_id):
                        del lines[k]
                k += 1
        new_file = open(self.__file_name, "w+")
        for line in lines:
            new_file.write(line)

    def update(self, student_id, student):
        self.add(student)
        self.remove(student_id)

    def __save_to_file(self, student):
        with open(self.__file_name, "a") as file_pointer:
            self.__entity_class().write_to(file_pointer, student)


class AssignmentFileRepository(AssignmentRepository):
    def __init__(self, validator_class, file_name, entity_class):
        super().__init__(validator_class)
        self.__file_name = file_name
        self.__entity_class = entity_class
        self.__load_data()

    def __load_data(self):
        with open(self.__file_name) as file_pointer:
            for line in file_pointer:
                assignment = self.__entity_class.read_from(self.__entity_class, line)
                if assignment != -1:
                    super().add(assignment)

    def add(self, assignment):
        super().add(assignment)
        self.__save_to_file(assignment)

    def remove(self, assignment_id):
        super().remove(assignment_id)
        lines = open(self.__file_name).readlines()
        k = 0
        with open(self.__file_name) as file_pointer:
            for line in file_pointer:
                assignment = self.__entity_class.read_from(self.__entity_class, line)
                if assignment != -1:
                    if int(assignment.assignment_id) == int(assignment_id):
                        del lines[k]
                k += 1
        new_file = open(self.__file_name, "w+")
        for line in lines:
            new_file.write(line)

    def update(self, assignment_id, assignment):
        self.add(assignment)
        self.remove(assignment_id)

    def __save_to_file(self, assignment):
        with open(self.__file_name, "a") as file_pointer:
            self.__entity_class().write_to(file_pointer, assignment)

class GradeFileRepository(GradeRepository):
    def __init__(self, validator_class, file_name, entity_class):
        super().__init__(validator_class)
        self.__file_name = file_name
        self.__entity_class = entity_class
        self.__load_data()

    def __load_data(self):
        with open(self.__file_name) as file_pointer:
            for line in file_pointer:
                grade = self.__entity_class.read_from(self.__entity_class, line)
                if grade != -1:
                    super().add(grade)

    def add(self, grade):
        super().add(grade)
        self.__save_to_file(grade)

    def remove(self, assignment_id, student_id):
        super().remove(assignment_id, student_id)
        lines = open(self.__file_name).readlines()
        k = 0
        with open(self.__file_name) as file_pointer:
            for line in file_pointer:
                grade = self.__entity_class.read_from(self.__entity_class, line)
                if grade != -1:
                    if int(grade.assignment_id) == int(assignment_id) and \
                        int(grade.student_id) == int(student_id):
                        del lines[k]
                k += 1
        new_file = open(self.__file_name, "w+")
        for line in lines:
            new_file.write(line)

    def grade(self, grade, grade_value):
        self.remove(grade.assignment_id, grade.student_id)
        g = Grade(grade.assignment_id, grade.student_id, grade_value)
        self.add(g)

    def __save_to_file(self, grade):
        with open(self.__file_name, "a") as file_pointer:
            self.__entity_class().write_to(file_pointer, grade)
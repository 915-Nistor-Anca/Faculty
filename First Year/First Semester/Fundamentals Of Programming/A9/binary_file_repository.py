from src.repository.repository import StudentRepository, AssignmentRepository, GradeRepository
from src.repository.entitites_data_acces import StudentDataAccess, AssignmentDataAccess, GradeDataAccess

class BinaryFileStudentRepository(StudentRepository):
    def __init__(self, validator_class, file_path):
        super().__init__(validator_class)
        self.__file_path = file_path
        self.__load_data()


    def __load_data(self):
        data = StudentDataAccess.read_from_binary_file(self.__file_path)
        for student in data:
            super().add(student)

    def add(self, student):
        super().add(student)
        StudentDataAccess.write_in_binary_file(self.__file_path, super().get_all())

    def remove(self, student_id):
        super().remove(student_id)
        StudentDataAccess.write_in_binary_file(self.__file_path, super().get_all())

    def update(self, student_id, student):
        super().update(student_id, student)
        StudentDataAccess.write_in_binary_file(self.__file_path, super().get_all())


class BinaryFileAssignmentRepository(AssignmentRepository):
    def __init__(self, validator_class, file_path):
        super().__init__(validator_class)
        self.__file_path = file_path
        self.__load_data()

    def __load_data(self):
        data = AssignmentDataAccess.read_from_binary_file(self.__file_path)
        for assignment in data:
            super().add(assignment)

    def add(self, assignment):
        super().add(assignment)
        AssignmentDataAccess.write_in_binary_file(self.__file_path, super().get_all())

    def remove(self, assignment_id):
        super().remove(assignment_id)
        StudentDataAccess.write_in_binary_file(self.__file_path, super().get_all())

    def update(self, assignment_id, assignment):
        super().update(assignment_id, assignment)
        StudentDataAccess.write_in_binary_file(self.__file_path, super().get_all())


class BinaryFileGradeRepository(GradeRepository):
    def __init__(self, validator_class, file_path):
        super().__init__(validator_class)
        self.__file_path = file_path
        self.__load_data()

    def __load_data(self):
        data = GradeDataAccess.read_from_binary_file(self.__file_path)
        for grade in data:
            super().add(grade)

    def add(self, grade):
        super().add(grade)
        GradeDataAccess.write_in_binary_file(self.__file_path, super().get_all())

    def remove(self, assignment_id, student_id):
        super().remove(assignment_id, student_id)
        GradeDataAccess.write_in_binary_file(self.__file_path, super().get_all())

    def grade(self, grade, new_value):
        super().grade(grade, new_value)
        GradeDataAccess.write_in_binary_file(self.__file_path, super().get_all())

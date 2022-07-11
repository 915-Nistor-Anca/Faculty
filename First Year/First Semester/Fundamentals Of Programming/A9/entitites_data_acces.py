import os.path
from abc import ABC, abstractmethod
import pickle

from src.domain.domain import Student, Assignment, Grade


class DataAccessEntity(ABC):
    @abstractmethod
    def write_to(self, file_pointer, entity):
        pass

    @abstractmethod
    def read_from(self, line):
        pass


class StudentDataAccess(DataAccessEntity):

    def  write_to(self, file_pointer, student):
        file_pointer.write(f"\n{student.student_id},{student.name},{student.group}")

    def read_from(self, line):
        if line != '\n':
            student_data = line.split(",")
            student = Student(int(student_data[0]), student_data[1], int(student_data[2]))
            return student
        return -1

    @staticmethod
    def read_from_binary_file(file_path):
        if os.path.getsize(file_path) == 0:
            return []
        with open(file_path, "rb") as file_pointer:
            data = pickle.load(file_pointer)
            return data

    @staticmethod
    def write_in_binary_file(file_path, data):
        with open(file_path, "wb") as file_pointer:
            pickle.dump(data, file_pointer)


class AssignmentDataAccess(DataAccessEntity):

    def write_to(self, file_pointer, assignment):
        file_pointer.write(f"\n{assignment.assignment_id};{assignment.description};{assignment.deadline}")

    def read_from(self, line):
        if line != '\n':
            assignment_data = line.split(";")
            assignment = Assignment(int(assignment_data[0]), assignment_data[1], assignment_data[2])
            return assignment
        return -1

    @staticmethod
    def read_from_binary_file(file_path):
        if os.path.getsize(file_path) == 0:
            return []
        with open(file_path, "rb") as file_pointer:
            data = pickle.load(file_pointer)
            return data

    @staticmethod
    def write_in_binary_file(file_path, data):
        with open(file_path, "wb") as file_pointer:
            pickle.dump(data, file_pointer)

class GradeDataAccess(DataAccessEntity):

    def write_to(self, file_pointer, grade):
        file_pointer.write(f"\n{grade.assignment_id},{grade.student_id},{grade.grade_value}")

    def read_from(self, line):
        if line != '\n':
            grade_data = line.split(",")
            grade = Grade(int(grade_data[0]), int(grade_data[1]), int(grade_data[2]))
            return grade
        return -1

    @staticmethod
    def read_from_binary_file(file_path):
        if os.path.getsize(file_path) == 0:
            return []
        with open(file_path, "rb") as file_pointer:
            data = pickle.load(file_pointer)
            return data

    @staticmethod
    def write_in_binary_file(file_path, data):
        with open(file_path, "wb") as file_pointer:
            pickle.dump(data, file_pointer)

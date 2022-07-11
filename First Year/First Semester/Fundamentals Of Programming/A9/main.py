import configparser

from src.ui.ui import Console
from src.repository.repository import StudentRepository, AssignmentRepository, GradeRepository
from src.services.services import StudentService, GeneralServices, AssignmentService, GradeService
from src.validators.validators import StudentValidator, AssignmentValidator, GradeValidator
from src.tests.tests import RunAllTests

from src.repository.text_file_repository import AssignmentFileRepository, StudentFileRepository, GradeFileRepository
from src.repository.entitites_data_acces import StudentDataAccess, AssignmentDataAccess, GradeDataAccess
from src.repository.binary_file_repository import BinaryFileStudentRepository, BinaryFileAssignmentRepository, BinaryFileGradeRepository


if __name__ == '__main__':

 tests = RunAllTests()
 tests.run_all()

 student_validator = StudentValidator()
 assignment_validator = AssignmentValidator()
 grade_validator = GradeValidator()

 config = configparser.ConfigParser()
 config.read("D:\\Fisiere facultate\\Programe FP\\GitHub\\a9-915-Nistor-Anca\\src\\repository\\settings.properties")
 choice = config.get("Choice", "repository")

 if choice == "textfiles":
  st_file = config.get("Text files", "students")
  as_file = config.get("Text files", "assignments")
  gr_file = config.get("Text files", "grades")
  students_repository = StudentFileRepository(student_validator, st_file, StudentDataAccess)
  assignments_repository = AssignmentFileRepository(assignment_validator, as_file, AssignmentDataAccess)
  grades_repository = GradeFileRepository(grade_validator, gr_file, GradeDataAccess)

 elif choice == "binaryfiles":
  st_file = config.get("Binary files", "st")
  as_file = config.get("Binary files", "as")
  gr_file = config.get("Binary files", "gr")
  students_repository = BinaryFileStudentRepository(student_validator, st_file)
  assignments_repository = BinaryFileAssignmentRepository(assignment_validator, as_file)
  grades_repository = BinaryFileGradeRepository(grade_validator, gr_file)

 else:
  students_repository = StudentRepository(student_validator)
  assignments_repository = AssignmentRepository(assignment_validator)
  grades_repository = GradeRepository(grade_validator)

 general_services = GeneralServices()
 student_service = StudentService(students_repository, grades_repository)
 assignment_service = AssignmentService(assignments_repository, students_repository, grades_repository)
 grade_service = GradeService(students_repository, assignments_repository, grades_repository)


 console = Console(general_services, student_service, assignment_service, grade_service)
 console.run()



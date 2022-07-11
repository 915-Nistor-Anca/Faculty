from src.ui.ui import Console
from src.repository.repository import StudentRepository, AssignmentRepository, GradeRepository
from src.services.services import StudentService, GeneralServices, AssignmentService, GradeService
from src.validators.validators import StudentValidator, AssignmentValidator, GradeValidator
from src.tests.tests import RunAllTests
if __name__ == '__main__':

 tests = RunAllTests()
 tests.run_all()

 student_validator = StudentValidator()
 assignment_validator = AssignmentValidator()
 grade_validator = GradeValidator()

 students_repository = StudentRepository(student_validator)
 assignments_repository = AssignmentRepository(assignment_validator)
 grades_repository = GradeRepository(grade_validator)

 general_services = GeneralServices()
 student_service = StudentService(students_repository, grades_repository)
 assignment_service = AssignmentService(assignments_repository, students_repository, grades_repository)
 grade_service = GradeService(students_repository, assignments_repository, grades_repository)


 console = Console(general_services, student_service, assignment_service, grade_service)
 console.run()


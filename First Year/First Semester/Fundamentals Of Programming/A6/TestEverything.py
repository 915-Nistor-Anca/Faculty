import unittest
from src.repository.repository import StudentRepository, GradeRepository, AssignmentRepository
from src.validators.validators import StudentValidator, GradeValidator, AssignmentValidator, DeadlineValidator
from src.validators.validators import StudentValidatorException, AssignmentValidatorException, GradeValidatorException, TimeDataNotMatchFormat
from src.domain.domain import Student, Grade, Assignment
from src.services.services import StudentService, GradeService, AssignmentService, GeneralServices
from src.undo_redo.undo import UndoManager
from src.undo_redo.redo import RedoManager
from src.undo_redo.handlers import *


class StudentRepositoryTest(unittest.TestCase):
    def setUp(self) -> None:
        self.__validator = StudentValidator()
        self.__student_repository = StudentRepository(self.__validator)

    def tearDown(self) -> None:
        pass

    def test_repository_empty(self):
        self.assertEqual(len(self.__student_repository), 0)

    def test_repository(self):
        a = Student(18968, 'Maria', 915)
        self.assertEqual(Student.__repr__(a), "Id: 18968, Name: Maria, Group: 915")
        a.student_id = 3
        self.assertEqual(a.student_id, 3)

        student = Student('3801', 'John', '915')
        self.__student_repository.add(student)
        self.__student_repository.add(Student('2572', 'Tina', '912'))

        with self.assertRaises(StudentValidatorException):
            self.__student_repository.add(Student('2792', 'Mary', '91a1'))
        self.assertEqual(len(self.__student_repository), 2)

        with self.assertRaises(StudentValidatorException):
            self.__student_repository.remove(1000)
        self.assertEqual(len(self.__student_repository), 2)

        self.__student_repository.remove(3801)
        self.assertEqual(len(self.__student_repository), 1)

        self.__student_repository.update(2572, Student('2579', 'Tara', '913'))
        list = self.__student_repository.get_all()
        self.assertEqual(list[-1].name, 'Tara')

        with self.assertRaises(StudentValidatorException):
            student = Student('6363', 'Lary', '913')
            self.__student_repository.add(student)
            student = Student('6363', 'Rita', '914')
            self.__student_repository.add(student)

        with self.assertRaises(StudentValidatorException):
            self.__student_repository.update(6363, Student('Ana', 'Tara', '913'))
            student = Student('123456', 'Lary', '913')
            self.__student_repository.add(student)
            self.__student_repository.update(6363, Student(123456, 'Tara', '913'))



class AssignmentRepositoryTest(unittest.TestCase):
    def setUp(self) -> None:
        self.__validator = AssignmentValidator()
        self.__assignment_repository = AssignmentRepository(self.__validator)

    def tearDown(self) -> None:
        pass

    def test_repository_empty(self):
        self.assertEqual(len(self.__assignment_repository), 0)

    def test_repository(self):
        a = Assignment(141, 'ABC', '21 June, 2021')
        self.assertEqual(Assignment.__repr__(a), "Id: 141, Description: ABC, Deadline: 21 June, 2021")

        assignment = Assignment(235, 'Draw an exemple of an Eulerian graph.', '11 December, 2021')
        self.__assignment_repository.add(assignment)
        self.assertEqual(len(self.__assignment_repository), 1)

        self.__assignment_repository.add(Assignment(245, 'Paint fruits.', '25 July, 2022'))
        self.assertEqual(len(self.__assignment_repository), 2)

        self.__assignment_repository.remove(245)
        self.assertEqual(len(self.__assignment_repository), 1)

        self.__assignment_repository.update(235, Assignment(532, 'Sing.', '19 December, 2021'))
        list = self.__assignment_repository.get_all()
        self.assertEqual(list[-1].description, 'Sing.')

        with self.assertRaises(AssignmentValidatorException):
            self.__assignment_repository.update(100, Assignment('abc', 'Do a math problem.', '21 July, 2020'))

        deadline = self.__assignment_repository.get_deadline_of_an_assignment(532)
        self.assertEqual(deadline, '19 December, 2021')

        with self.assertRaises(TimeDataNotMatchFormat):
            v = DeadlineValidator()
            v.validate_deadline('200 June, 2021')

        with self.assertRaises(TimeDataNotMatchFormat):
             v = DeadlineValidator()
             v.validate_deadline('Two June, 2021')

        with self.assertRaises(TimeDataNotMatchFormat):
             v = DeadlineValidator()
             v.validate_deadline('2 Juneee, 2021')

        with self.assertRaises(AssignmentValidatorException):
            self.__assignment_repository.add(Assignment('aapdkpff', 'abc', '21 June, 2021'))

        self.__assignment_repository.add(Assignment(1, 'abc', '21 June, 2021'))
        with self.assertRaises(AssignmentValidatorException):
            self.__assignment_repository.add(Assignment(1, 'abc', '21 June, 2021'))

        with self.assertRaises(AssignmentValidatorException):
            v = AssignmentValidator()
            v.validate_assignment_id('aafb')

        self.__assignment_repository.add(Assignment(10, 'abc', '21 June, 2021'))
        list = self.__assignment_repository.get_all()
        self.assertEqual(list[-1].assignment_id, 10)


class GradeRepositoryTest(unittest.TestCase):
    def setUp(self) -> None:
        self.__validator = GradeValidator()
        self.__grade_repository = GradeRepository(self.__validator)

    def tearDown(self) -> None:
        pass

    def test_repository_empty(self):
        self.assertEqual(len(self.__grade_repository), 0)

    def test_repository(self):
        self.__grade_repository.add(Grade(131, 31, 9))
        self.__grade_repository.remove_last_given_assignment_ungraded()
        a = Grade(123, 31, 10)
        self.assertEqual(Grade.__repr__(a), "Assignment id: 123, Student id: 31, Grade: 10")
        a.student_id = 100
        self.assertEqual(a.student_id, 100)
        a.assignment_id = 13
        self.assertEqual(a.assignment_id, 13)
        grade = Grade(242, 2213, 10)
        self.__grade_repository.add(grade)
        self.assertEqual(len(self.__grade_repository), 1)

        grade = Grade(282, 2924, 9)
        self.__grade_repository.add(grade)
        g = self.__grade_repository.find_grade_value(2924, 282)
        self.assertEqual(g, 9)
        self.__grade_repository.change_a_grade(2924, 282, 8)
        g = self.__grade_repository.find_grade_value(2924, 282)
        self.assertEqual(g, 8)
        self.assertEqual(len(self.__grade_repository), 2)
        self.__grade_repository.remove(282, 2924)
        self.assertEqual(len(self.__grade_repository), 1)

        grade = Grade(242, 2213, 10)
        with self.assertRaises(GradeValidatorException):
            self.__grade_repository.grade(grade, 8)

        list = self.__grade_repository.get_all()
        self.assertEqual(list[-1].grade_value, 10)

        grade = Grade(213, 1234, -1)
        self.__grade_repository.add(grade)
        self.__grade_repository.grade(grade, 10)
        self.assertEqual(list[-1].grade_value, 10)

        grade = Grade(214298423, 1234, -1)
        self.__grade_repository.add(grade)
        with self.assertRaises(GradeValidatorException):
            self.__grade_repository.grade(Grade(214298423, 1234, -1), 'ten')

        with self.assertRaises(GradeValidatorException):
            grade = Grade('adad', 'daa', -1)
            self.__grade_repository.add(grade)

class StudentServiceTest(unittest.TestCase):
    def setUp(self) -> None:
        self.__s_validator = StudentValidator()
        self.__g_validator = GradeValidator()
        self.__student_repository = StudentRepository(self.__s_validator)
        self.__grade_repository = GradeRepository(self.__g_validator)
        self.__assignment_validator = AssignmentValidator()
        self.__assignment_repository = AssignmentRepository(self.__assignment_validator)
        self.__student_service = StudentService(self.__student_repository, self.__grade_repository)

    def tearDown(self) -> None:
        pass

    def test_service(self):
        self.__student_service.first_20_students()
        list = self.__student_service.get_list_of_students()
        self.assertEqual(len(list), 20)

        self.__student_service.add_student('3141', 'Mary', '915')
        list = self.__student_service.get_list_of_students()
        self.assertEqual(list[-1].name, 'Mary')
        name = self.__student_service.get_name_from_id(3141)
        self.assertEqual(name, 'Mary')

        self.__student_service.update_student('3141', '7564', 'Jane', '914')
        list = self.__student_service.get_list_of_students()

        list = self.__student_service.get_list_of_students()
        self.assertEqual(list[-1].name, 'Jane')

        self.__student_service.add_student('3141', 'Mary', '915')
        self.__student_service.remove_student('7564')
        list = self.__student_service.get_list_of_students()
        self.assertEqual(list[-1].name, 'Mary')

    def test_delete_assignments(self):
        self.__student_service.add_student(4252, 'George', 915)
        self.__grade_repository.add(Grade(421, 4252, 8))
        self.__student_service.remove_student_and_delete_assignments(4252)
        list = self.__grade_repository.get_all()
        self.assertEqual(len(list), 0)

    def test_undo_functions(self):
        self.__student_service.add_student_undo(4252, 'George', 915)
        list = self.__student_repository.get_all()
        self.assertEqual(len(list), 1)
        self.__student_service.update_student_undo(4252, 1, 'Gigi', 911)
        self.__student_service.remove_student_undo(1)
        self.__student_service.delete_assignments_of_a_deleted_student_undo(131)
        self.__student_service.remove_student_and_delete_assignments_redo(9)

    def test_undo_functions_2(self):
        self.__assignment_repository.add(Assignment(134, 'abc', '21 June, 2021'))
        self.__student_repository.add(Student(5678, 'Ama', 915))
        self.__grade_repository.add(Grade(134, 5678, -1))
        self.__student_service.delete_assignments_of_a_deleted_student_undo(5678)

class AssignmentServiceTest(unittest.TestCase):
    def setUp(self) -> None:
        self.__a_validator = AssignmentValidator()
        self.__g_validator = GradeValidator()
        self.__s_validator = StudentValidator()
        self.__assignment_repository = AssignmentRepository(self.__a_validator)
        self.__student_repository = StudentRepository(self.__s_validator)
        self.__grade_repository = GradeRepository(self.__g_validator)
        self.__assignment_service = AssignmentService(self.__assignment_repository, self.__student_repository, self.__grade_repository)

    def tearDown(self) -> None:
        pass

    def test_service(self):
        self.__assignment_service.first_20_assignments()
        list = self.__assignment_service.get_list_of_assignments()
        self.assertEqual(len(list), 20)

        self.__assignment_service.add_assignment(144, 'Draw a cat.', '21 September, 2021')
        list = self.__assignment_service.get_list_of_assignments()
        self.assertEqual(len(list), 21)

        self.__assignment_service.add_assignment(15353515, 'Sing.', '15 August, 2020')
        self.__assignment_service.add_assignment(113325, 'Sing.', '15 August, 2020')
        self.__assignment_service.update_assignment(113325, 112846, 'Learn a language.', '16 January, 2022')
        list = self.__assignment_service.get_list_of_assignments()
        self.assertEqual(list[-1].deadline, '16 January, 2022')

        self.__assignment_service.remove_assignment(112846)
        list = self.__assignment_service.get_list_of_assignments()
        self.assertEqual(len(list), 22)

        self.__assignment_service.add_assignment(244, 'Description.', '21 July, 2021')
        deadline = self.__assignment_service.get_deadline(244)
        self.assertEqual(deadline, '21 July, 2021')

    def test_delete_assignment_grade(self):
        self.__assignment_service.add_assignment(628, 'Sing.', '21 July, 2021')
        self.__assignment_service.add_assignment(592, 'Draw.', '14 May, 2022')
        self.__student_repository.add(Student(2452, 'Mary', 914))
        self.__student_repository.add(Student(2314, 'Lexy', 913))
        self.__grade_repository.add(Grade(628, 2314, 8))
        self.__grade_repository.add(Grade(628, 2452, 7))
        self.__grade_repository.add(Grade(592, 2452, 7))
        self.__assignment_service.remove_assignment_delete_grades(628)
        list = self.__grade_repository.get_all()
        self.assertEqual(len(list), 1)

    def test_undo_functions(self):
        self.__assignment_service.add_assignment_undo(183, 'abc', '21 June, 2021')
        self.__assignment_service.update_assignment_undo(183, 1, 'x', '16 May, 2021')
        self.__assignment_service.remove_assignment_undo(1)
        self.__assignment_service.add_assignment_undo(183, 'abc', '21 June, 2021')
        self.__assignment_service.remove_assignment_delete_grades_undo(183)

    def test_validators(self):
        pass

class GradeServiceTest(unittest.TestCase):
    def setUp(self) -> None:
        self.__a_validator = AssignmentValidator()
        self.__g_validator = GradeValidator()
        self.__s_validator = StudentValidator()
        self.__assignment_repository = AssignmentRepository(self.__a_validator)
        self.__student_repository = StudentRepository(self.__s_validator)
        self.__grade_repository = GradeRepository(self.__g_validator)
        self.__grade_service = GradeService(self.__student_repository, self.__assignment_repository, self.__grade_repository)

    def tearDown(self) -> None:
        pass

    def test_service(self):

        self.__grade_service.add_grade(2424, 2093, 10)
        list = self.__grade_service.get_list_of_grades()
        self.assertEqual(len(list), 1)

        self.__grade_service.remove_grade(2424, 2093)
        list = self.__grade_service.get_list_of_grades()
        self.assertEqual(len(list), 0)

        self.__grade_service.add_grade(2424, 2093, 10)
        self.assertEqual(self.__grade_service.check_if_assignment_not_given_to_student(2424,2093), False)
        self.assertEqual(self.__grade_service.check_if_assignment_not_given_to_student(2424, 2083), True)

        assignment = Assignment(235, 'Draw an exemple of an Eulerian graph.', '11 December, 2021')
        self.__assignment_repository.add(assignment)
        self.assertEqual(self.__grade_service.check_if_assignment_exists(235), True)
        self.assertEqual(self.__grade_service.check_if_assignment_exists(285), False)

        student = Student('3801', 'John', '915')
        self.__student_repository.add(student)
        self.assertEqual(self.__grade_service.check_if_student_exists(3801), True)
        self.assertEqual(self.__grade_service.check_if_student_exists(3881), False)

        self.__assignment_repository.add(Assignment(852, 'Paint', '21 August, 2021'))
        self.__grade_service.give_assignment_student(852, 3801)
        list = self.__grade_service.get_list_of_grades()
        self.assertEqual(list[-1].assignment_id, 852)

        self.__student_repository.add(Student(3134, 'John', 914))
        self.__grade_service.give_assignment_group(852, 914)
        list = self.__grade_service.get_list_of_grades()
        self.assertEqual(list[-1].student_id, 3134)

        self.__assignment_repository.add(Assignment(525, 'Paint.', '12 May, 2021'))
        self.__assignment_repository.add(Assignment(134, 'Sing.', '15 April, 2021'))
        self.__grade_service.give_assignment_student(525, 3801)
        self.__grade_service.give_assignment_student(134, 3801)
        list = self.__grade_service.create_list_assignments_for_student(3801)
        a1 = Grade(852, 3801, -1)
        a2 = Grade(525, 3801, -1)
        a3 = Grade(134, 3801, -1)
        self.assertEqual(list[-1].assignment_id, 134)

        self.__grade_service.grade_student(3801, 134, 8)
        list = self.__grade_service.create_list_assignments_for_student(3801)
        self.assertEqual(list[-1].grade_value, -1)

        self.assertEqual(self.__grade_service.get_grade_value(134, 3801), -1)

        self.__assignment_repository.add(Assignment(421, 'Description.', '13 June, 2022'))
        list = self.__assignment_repository.get_all()
        self.assertEqual(list[-1].assignment_id, 421)
        self.__student_repository.add(Student(4842, 'Lia', 915))
        self.__student_repository.add(Student(6325, 'John', 914))
        self.__student_repository.add(Student(5336, 'John', 914))
        self.__grade_service.give_assignment_student(421, 4842)
        self.__grade_service.give_assignment_student(421, 3134)
        self.__grade_service.give_assignment_student(421, 6325)
        self.__grade_service.give_assignment_student(421, 5336)
        self.__grade_service.grade_student(4842, 421, 7)
        self.__grade_service.grade_student(5336, 421, 8)
        list = self.__grade_service.students_with_given_assignment(421)
        self.assertEqual(list, [4842, 3134, 6325, 5336])

        self.__grade_service.first_10_assignments()
        list = self.__grade_service.get_list_of_grades()
        self.assertEqual(len(list), 10)

        self.__grade_service.first_5_grades()
        self.assertEqual(len(list), 10)

        deadline = '21 July, 2024'
        self.assertEqual(self.__grade_service.deadline_has_passed(deadline), False)

    def test_sort_students_by_grades(self):
        self.__student_repository.add(Student(1111, 'A', 911))
        self.__student_repository.add(Student(2222, 'B', 912))
        self.__student_repository.add(Student(3333, 'C', 913))
        self.__student_repository.add(Student(4444, 'D', 914))
        self.__student_repository.add(Student(5555, 'E', 915))
        self.__assignment_repository.add(Assignment(111, 'D1', '1 January, 2022'))
        self.__assignment_repository.add(Assignment(222,'D2', '2 January, 2022'))
        self.__grade_service.give_assignment_student(111, 1111)
        self.__grade_service.give_assignment_student(111, 2222)
        self.__grade_service.give_assignment_student(111, 3333)
        self.__grade_service.give_assignment_student(111, 4444)
        self.__grade_service.give_assignment_student(111, 5555)
        self.__grade_service.grade_student(1111, 111, 10)

    def test_functions_undo(self):
        self.__assignment_repository.add(Assignment(134, 'abc', '21 June, 2021'))
        self.__student_repository.add(Student(5678, 'Ama', 915))
        self.__grade_repository.add(Grade(134, 5678, 10))
        self.__grade_service.make_minus_one(5678, 134)
        self.__grade_service.give_assignment_student_redo(134, 5678)
        self.__grade_service.delete_given_assignment(None, None)
        self.__grade_service.give_assignment_group_undo(134, 915)
        self.__grade_repository.add(Grade(134, 5678, 10))
        self.__grade_service.remove_assignment_group(134, 915, [5678])
        self.__grade_repository.add(Grade(134, 5678, -1))
        self.__grade_service.grade_student(5678, 134, 4)
        self.__grade_service.make_minus_one(5678, 134)
        self.__grade_repository.add(Grade(134, 5678, -1))
        self.__grade_service.grade_student_redo(5678, 134, 7)

    def test_functions_2(self):
        self.__assignment_repository.add(Assignment(134, 'abc', '21 June, 2022'))
        self.__student_repository.add(Student(5678, 'Ama', 915))
        self.__student_repository.add(Student(5552, 'Ama', 915))
        self.__student_repository.add(Student(2521, 'Ama', 915))
        self.__student_repository.add(Student(6463, 'Ama', 915))
        self.__student_repository.add(Student(4213, 'Ama', 915))
        self.__grade_repository.add(Grade(134, 5678, 1))
        self.__grade_repository.add(Grade(134, 5552, 4))
        self.__grade_repository.add(Grade(134, 2521, 8))
        self.__grade_repository.add(Grade(134, 6463, 3))
        self.__grade_repository.add(Grade(134, 4213, 6))
        list = self.__grade_service.students_with_given_assignment(134)
        self.assertEqual(list, [2521, 4213, 5552, 6463, 5678])
        self.__assignment_repository.add(Assignment(999, 'blabla', '21 June, 2020'))

        self.__grade_service.give_assignment_student(999, 5678)
        list = self.__grade_service.late_students()
        self.assertEqual(list, [])
        g = self.__grade_service.average_grade_for_student(5678)
        self.assertEqual(g, 1)

        list = self.__grade_service.sort_students_by_their_grades()
        self.assertEqual(list[0].name, 'Ama')

class GeneralServiceTest(unittest.TestCase):
    def setUp(self) -> None:
        self.__general_service = GeneralServices()

    def tearDown(self) -> None:
        pass

    def test_functions(self):
        self.assertEqual(self.__general_service.get_command_and_args('remove 1'), ('remove', ['1']))

class UndoRedoTest(unittest.TestCase):
    def setUp(self) -> None:
        self.__undo_manager = UndoManager()
        self.__redo_manager = RedoManager()
        self.__a_validator = AssignmentValidator()
        self.__g_validator = GradeValidator()
        self.__s_validator = StudentValidator()
        self.__assignment_repository = AssignmentRepository(self.__a_validator)
        self.__student_repository = StudentRepository(self.__s_validator)
        self.__grade_repository = GradeRepository(self.__g_validator)
        self.__grade_service = GradeService(self.__student_repository, self.__assignment_repository,
                                            self.__grade_repository)
        self.__student_service = StudentService(self.__student_repository, self.__grade_repository)
        self.__assignment_service = AssignmentService(self.__assignment_repository, self.__student_repository,
                                                      self.__grade_repository)

    def tearDown(self) -> None:
        pass

    def test_undo_redo(self):
        self.__undo_manager.undo()
        self.__redo_manager.redo()

    def test_h(self):
        remove_assignment_handler(self.__assignment_service, 3378342, 'abc', '21 June, 2021')
        delete_assignment_delete_grades_handler(self.__assignment_service, 4242, 'abc', '21 June, 2021',
                                                self.__grade_repository, [])
        give_assignment_group_handler(self.__grade_service, 42425, 915, [])
        self.__assignment_service.add_assignment(42974, 'abc', '21 June, 2021')
        update_assignment_handler(self.__assignment_service, 42974, 29429, 'abc', '21 June, 2021')
        self.__assignment_service.add_assignment(4297400, 'abc', '21 June, 2021')
        update_a_handler(self.__assignment_service, 4297400, 423, 'vsin', '21 June, 2021')

        update_s_handler(self.__student_service, 4225242, 42522, 'ale', 915)
        remove_s_handler(self.__student_service, 42974740, 'ale', 915)
    def test_handlers(self):
        self.__student_service.add_student(314, 'Alexia', 915)
        self.__assignment_service.add_assignment(3, 'abc', '21 June, 2021')
        remove_student_and_delete_his_assignments(self.__student_service, 314)
        remove_assignment_delete_grades(self.__assignment_service, 3)
        give_assignment_to_a_student(self.__grade_service, 314, 3)
        give_assignment_to_a_group(self.__grade_service, 3, 915)
        self.__grade_service.add_grade(3, 314, -1)
        remove_student_handler(self.__student_service, 314, 'Alexia', 915)
        add_student_handler(self.__student_service, 314)
        update_student_handler(self.__student_service, 314, 315, 'Ale', 915)
        g = Grade(3, 314, 10)
        delete_student_delete_assignments_handler(self.__student_service, 314, 'ale', 915,
                                                  self.__grade_repository, [g])
        add_grade_handler(self.__grade_service, 314, 3, 9)
        give_assignment_student_handler(self.__grade_service, 314, 3)
        grade_change_handler(self.__grade_service, 314, 3, 10)

    def test_handlers_2(self):
        self.__assignment_service.add_assignment(3, 'abc', '21 June, 2021')
        self.__assignment_service.add_assignment(5342423, 'abc', '21 June, 2021')
        remove_assignment_handler(self.__assignment_service, 30, 'abc', '21 July, 2021')


if __name__ == '__main__':
    unittest.main()
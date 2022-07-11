from src.validators.validators import *
from src.repository.repository import *
from src.services.services import *

class TestsRepository:
    def test_students_add(self):
        st = StudentValidator()
        c = StudentRepository(st)
        student = Student(1, 'Alexia', 915)
        c.add(student)
        students = c.get_all()
        assert students[-1].group == 915

    def test_students_remove(self):
        st = StudentValidator()
        c = StudentRepository(st)
        student = Student(1,'Ana', 912)
        c.add(student)
        student = Student(2,'Maria', 913)
        c.add(student)
        c.remove(2)
        students = c.get_all()
        assert students[-1].name == 'Ana'

    def test_students_update(self):
        st = StudentValidator()
        c = StudentRepository(st)
        student = Student(1, 'Ana', 912)
        c.add(student)
        new = Student(2, 'Diana', 913)
        c.update(1, new)
        students = c.get_all()
        assert students[-1].name == 'Diana' and students[-1].student_id == 2

    def test_get_all_s(self):
        st = StudentValidator()
        c = StudentRepository(st)
        student = Student(1, 'Ana', 912)
        c.add(student)
        student = Student(2, 'Maria', 913)
        c.add(student)
        students = c.get_all()
        assert students[0].student_id == 1 and students[1].group == 913


    def test_assignments_add(self):
        av = AssignmentValidator()
        c = AssignmentRepository(av)
        a = Assignment(1, 'Write an essay.', '21_dec_2021')
        c.add(a)
        assignments = c.get_all()
        assert assignments[-1].description == 'Write an essay.'

    def test_assignments_remove(self):
        av = AssignmentValidator()
        c = AssignmentRepository(av)
        a = Assignment(1, 'Write an essay.', '21_dec_2021')
        c.add(a)
        a = Assignment(2, 'Draw the solar sistem.', '15_dec_2021')
        c.add(a)
        c.remove(2)
        assignments = c.get_all()
        assert assignments[-1].assignment_id == 1

    def test_assignments_update(self):
        av = AssignmentValidator()
        c = AssignmentRepository(av)
        a = Assignment(1, 'Write an essay.', '21_dec_2021')
        c.add(a)
        new = Assignment(10, 'Compose a song.', '14_dec_2021')
        c.update(1, new)
        assignments = c.get_all()
        assert assignments[-1].description == 'Compose a song.'

    def test_get_all_a(self):
        av = AssignmentValidator()
        c = AssignmentRepository(av)
        a = Assignment(412, 'Write an essay.', '21_dec_2021')
        c.add(a)
        b = Assignment(10, 'Compose a song.', '14_dec_2021')
        c.add(b)
        assignments = c.get_all()
        assert assignments[0].assignment_id == 412

    def test_grade_add(self):
        gv = GradeValidator()
        c = GradeRepository(gv)
        g = Grade(1,2,10)
        c.add(g)
        grades = c.get_all()
        assert grades[0].grade_value == 10


    def test_grade_remove(self):
        gv = GradeValidator()
        c = GradeRepository(gv)
        g = Grade(1, 2, 10)
        c.add(g)
        g = Grade(1, 8, 7)
        c.add(g)
        c.remove(1, 2)
        grades = c.get_all()
        assert grades[0].grade_value == 7

    def test_get_all_g(self):
        gv = GradeValidator()
        c = GradeRepository(gv)
        g = Grade(1, 2, 10)
        c.add(g)
        g = Grade(1, 8, 7)
        c.add(g)
        grades = c.get_all()
        assert grades[0].grade_value == 10 and grades[1].assignment_id == 1

class TestServices:
    def test_student_add_student(self):
        sv = StudentValidator()
        sr = StudentRepository(sv)
        gv = GradeValidator()
        gr = GradeRepository(gv)
        ss = StudentService(sr, gv)
        ss.add_student(1,'Gina', 915)
        ss.add_student(2,'Miruna', 913)
        students = ss.get_list_of_students()
        assert students[-1].name == 'Miruna'

    def test_student_update_student(self):
        sv = StudentValidator()
        sr = StudentRepository(sv)
        gv = GradeValidator()
        gr = GradeRepository(gv)
        ss = StudentService(sr, gv)
        ss.add_student(1, 'Irina', 917)
        ss.add_student(2, 'Tina', 914)
        ss.update_student(1,10,'Luana',912)
        students = ss.get_list_of_students()
        assert students[0].name == 'Luana'

    def test_student_remove_student(self):
        sv = StudentValidator()
        sr = StudentRepository(sv)
        gv = GradeValidator()
        gr = GradeRepository(gv)
        ss = StudentService(sr, gv)
        ss.add_student(1, 'Elena', 914)
        ss.add_student(2, 'Sofia', 911)
        ss.remove_student(2)
        students = ss.get_list_of_students()
        assert students[-1].name == 'Elena'

    def test_student_get_lists_of_students(self):
        sv = StudentValidator()
        sr = StudentRepository(sv)
        gv = GradeValidator()
        gr = GradeRepository(gv)
        ss = StudentService(sr, gv)
        ss.add_student(1, 'Claudia', 912)
        ss.add_student(2, 'Denisa', 916)
        students = ss.get_list_of_students()
        assert students[0].name == 'Claudia'

    def test_student_first_20_students(self):
        sv = StudentValidator()
        sr = StudentRepository(sv)
        gv = GradeValidator()
        gr = GradeRepository(gv)
        ss = StudentService(sr, gv)
        ss.first_20_students()
        students = ss.get_list_of_students()
        assert len(students) == 20

    def test_assignment_add_assignment(self):
        av = AssignmentValidator()
        gv = GradeValidator()
        ar = AssignmentRepository(av)
        gr = GradeRepository(gv)
        sv = StudentValidator()
        sr = StudentRepository(sv)
        asr = AssignmentService(ar, sr, gr)
        asr.add_assignment(1, 'Draw.', '12_nov_2021')
        assignments = asr.get_list_of_assignments()
        assert assignments[0].assignment_id == 1

    def test_assignment_update_assignment(self):
        av = AssignmentValidator()
        gv = GradeValidator()
        ar = AssignmentRepository(av)
        gr = GradeRepository(gv)
        sv = StudentValidator()
        sr = StudentRepository(sv)
        asr = AssignmentService(ar, sr, gr)
        asr.add_assignment(1, 'Draw.', '12_nov_2021')
        asr.update_assignment(1,10,'Sing.', '20_dec_2021')
        assignments = asr.get_list_of_assignments()
        assert assignments[0].deadline == '20_dec_2021'

    def test_assignment_remove_assignment(self):
        av = AssignmentValidator()
        gv = GradeValidator()
        ar = AssignmentRepository(av)
        gr = GradeRepository(gv)
        sv = StudentValidator()
        sr = StudentRepository(sv)
        asr = AssignmentService(ar, sr, gr)
        asr.add_assignment(1, 'Draw.', '12_nov_2021')
        asr.add_assignment(2, 'Paint.', '21_jan_2022')
        asr.remove_assignment(1)
        assignments = asr.get_list_of_assignments()
        assert assignments[0].description == 'Paint.'

    def test_assignment_first_20_assignments(self):
        av = AssignmentValidator()
        gv = GradeValidator()
        ar = AssignmentRepository(av)
        gr = GradeRepository(gv)
        sv = StudentValidator()
        sr = StudentRepository(sv)
        asr = AssignmentService(ar, sr, gr)
        asr.first_20_assignments()
        assignments = asr.get_list_of_assignments()
        assert len(assignments) == 20

    def test_assignments_get_list_of_assignments(self):
        av = AssignmentValidator()
        gv = GradeValidator()
        ar = AssignmentRepository(av)
        gr = GradeRepository(gv)
        sv = StudentValidator()
        sr = StudentRepository(sv)
        asr = AssignmentService(ar, sr, gr)
        asr.add_assignment(1, 'Draw.', '12_dec_2021')
        assignments = asr.get_list_of_assignments()
        assert assignments[0].description == 'Draw.'

    def test_grades_add_grade(self):
        gv = GradeValidator()
        av = AssignmentValidator()
        sv = StudentValidator()
        sr = StudentRepository(sv)
        ar = AssignmentRepository(av)
        gr = GradeRepository(gv)
        gs = GradeService(sr, ar, gr)
        gs.add_grade(1,1234,9)
        grades = gs.get_list_of_grades()
        assert grades[0].assignment_id == 1

    def test_grades_remove_grade(self):
        gv = GradeValidator()
        av = AssignmentValidator()
        sv = StudentValidator()
        sr = StudentRepository(sv)
        ar = AssignmentRepository(av)
        gr = GradeRepository(gv)
        gs = GradeService(sr, ar, gr)
        gs.add_grade(2, 1234, 9)
        gs.add_grade(1, 3292, 7)
        gs.remove_grade(2,1234)
        grades = gs.get_list_of_grades()
        assert grades[0].assignment_id == 1

    def test_grades_get_list_of_grades(self):
        gv = GradeValidator()
        av = AssignmentValidator()
        sv = StudentValidator()
        sr = StudentRepository(sv)
        ar = AssignmentRepository(av)
        gr = GradeRepository(gv)
        gs = GradeService(sr, ar, gr)
        gs.add_grade(2, 1234, 9)
        gs.add_grade(1, 3292, 7)
        grades = gs.get_list_of_grades()
        assert grades[1].student_id == 3292

    def test_grades_check_if_assignment_not_given_to_student(self):
        gv = GradeValidator()
        av = AssignmentValidator()
        sv = StudentValidator()
        sr = StudentRepository(sv)
        ar = AssignmentRepository(av)
        gr = GradeRepository(gv)
        gs = GradeService(sr, ar, gr)
        gs.add_grade(123, 4213, -1)
        assert gs.check_if_assignment_not_given_to_student(123, 4213) == False

    def test_grades_check_if_assignment_exists(self):
        gv = GradeValidator()
        av = AssignmentValidator()
        sv = StudentValidator()
        sr = StudentRepository(sv)
        ar = AssignmentRepository(av)
        gr = GradeRepository(gv)
        gs = GradeService(sr, ar, gr)
        assignment = Assignment(2325, 'Sleep!', '12_dec_2021')
        ar.add(assignment)
        assert gs.check_if_assignment_exists(2325) == True

    def test_grades_check_if_student_exists(self):
        gv = GradeValidator()
        av = AssignmentValidator()
        sv = StudentValidator()
        sr = StudentRepository(sv)
        ar = AssignmentRepository(av)
        gr = GradeRepository(gv)
        gs = GradeService(sr, ar, gr)
        student = Student(1357, 'Elisabeta', 915)
        sr.add(student)
        assert gs.check_if_student_exists(1357) == True

    def test_grades_give_assignment_student(self):
        gv = GradeValidator()
        av = AssignmentValidator()
        sv = StudentValidator()
        sr = StudentRepository(sv)
        ar = AssignmentRepository(av)
        gr = GradeRepository(gv)
        gs = GradeService(sr, ar, gr)
        a = Assignment(1432, 'Draw.', '17_dec_2021')
        s = Student(5321, 'Lorena', 913)
        ar.add(a)
        sr.add(s)
        gs.give_assignment_student(1432, 5321)
        grades = gs.get_list_of_grades()
        assert grades[0].grade_value == -1

    def test_grades_give_assignment_group(self):
        gv = GradeValidator()
        av = AssignmentValidator()
        sv = StudentValidator()
        sr = StudentRepository(sv)
        ar = AssignmentRepository(av)
        gr = GradeRepository(gv)
        gs = GradeService(sr, ar, gr)
        a = Assignment(1432, 'Draw.', '17_dec_2021')
        s = Student(5321, 'Lorena', 913)
        ar.add(a)
        sr.add(s)
        gs.give_assignment_group(1432, 913)
        grades = gs.get_list_of_grades()
        assert grades[0].grade_value == -1

    def test_general_remove_useless_spaces(self):
        gs = GeneralServices()
        assert gs.remove_useless_spaces('  ana    are  mere ') == 'ana are mere'

    def test_general_get_command_and_args(self):
        gs = GeneralServices()
        assert gs.get_command_and_args('add 1 maria 915') == ('add', ['1', 'maria', '915'])



class RunAllTests:
    def __init__(self):
        self.__tests_for_repository = TestsRepository()
        self.__test_for_services = TestServices()

    def run_all(self):
        self.__tests_for_repository.test_students_add()
        self.__tests_for_repository.test_students_remove()
        self.__tests_for_repository.test_students_update()
        self.__tests_for_repository.test_get_all_s()

        self.__tests_for_repository.test_assignments_add()
        self.__tests_for_repository.test_assignments_remove()
        self.__tests_for_repository.test_assignments_update()
        self.__tests_for_repository.test_get_all_a()

        self.__tests_for_repository.test_grade_add()
        self.__tests_for_repository.test_grade_remove()
        self.__tests_for_repository.test_get_all_g()


        self.__test_for_services.test_student_add_student()
        self.__test_for_services.test_student_update_student()
        self.__test_for_services.test_student_remove_student()
        self.__test_for_services.test_student_get_lists_of_students()
        self.__test_for_services.test_student_first_20_students()

        self.__test_for_services.test_assignment_add_assignment()
        self.__test_for_services.test_assignment_remove_assignment()
        self.__test_for_services.test_assignment_update_assignment()
        self.__test_for_services.test_assignments_get_list_of_assignments()
        self.__test_for_services.test_assignment_first_20_assignments()

        self.__test_for_services.test_grades_add_grade()
        self.__test_for_services.test_grades_remove_grade()
        self.__test_for_services.test_grades_get_list_of_grades()
        self.__test_for_services.test_grades_give_assignment_student()
        self.__test_for_services.test_grades_give_assignment_group()
        self.__test_for_services.test_grades_check_if_assignment_not_given_to_student()
        self.__test_for_services.test_grades_check_if_assignment_exists()

        self.__test_for_services.test_general_remove_useless_spaces()
        self.__test_for_services.test_general_get_command_and_args()


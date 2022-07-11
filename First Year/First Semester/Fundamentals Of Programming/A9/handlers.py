from enum import Enum

def add_student_handler(student_service, student_id):
    student_service.remove_student_undo(student_id)

def remove_student_handler(student_service, student_id, name, group):
    student_service.add_student_undo(student_id, name, group)

def update_student_handler(student_service, old_student_id, student_id, name, group):
    student_service.update_student_undo(old_student_id, student_id, name, group)


def add_assignment_handler(assignment_service, assignment_id):
    assignment_service.remove_assignment_undo(assignment_id)

def remove_assignment_handler(assignment_service, assignment_id, description, deadline):
    assignment_service.add_assignment_undo(assignment_id, description, deadline)

def update_assignment_handler(assignment_service, old_assignment_id, assignment_id, description, deadline):
    assignment_service.update_assignment_undo(old_assignment_id, assignment_id, description, deadline)

def remove_s_handler(student_service, student_id, name, group):
    student_service.add_student(student_id, name, group)

def update_s_handler(student_service, old_student_id, student_id, name, group):
    student_service.update_student(old_student_id, student_id, name, group)

def update_a_handler(assignment_service, old_assignment_id, assignment_id, description, deadline):
    assignment_service.update_assignment(old_assignment_id, assignment_id, description, deadline)

def delete_assignments_student_handler(grade_repository, list_of_assignments):
    for assignment in list_of_assignments:
        grade_repository.add(assignment)

def delete_student_delete_assignments_handler(student_service, student_id, name, group, grade_repository, list_of_assignments):
    remove_student_handler(student_service, student_id, name, group)
    delete_assignments_student_handler(grade_repository, list_of_assignments)
    student_service.remove_student_and_delete_assignments_redo(student_id)

def add_grade_handler(grade_service, student_id, assignment_id, grade_value):
    grade_service.make_minus_one(student_id, assignment_id)
    grade_service.grade_student_redo(student_id, assignment_id, grade_value)

def give_assignment_student_handler(grade_service, student_id, assignment_id):
    grade_service.delete_given_assignment(student_id, assignment_id)
    grade_service.give_assignment_student_redo(assignment_id, student_id)

def delete_assignment_delete_grades_handler(assignment_service, assignment_id, description, deadline, grade_repository, list_of_grades):
    remove_assignment_handler(assignment_service, assignment_id, description, deadline)
    delete_assignments_student_handler(grade_repository, list_of_grades)
    assignment_service.remove_assignment_delete_grades_undo(assignment_id)

def give_assignment_group_handler(grade_service, assignment_id, group, l):
    grade_service.remove_assignment_group(assignment_id, group, l)
    grade_service.give_assignment_group_undo(assignment_id, group)

def grade_change_handler(grade_service, student_id, assignment_id, grade_value):
    grade_service.grade_student_undo(student_id, assignment_id, grade_value)

def give_assignment_to_a_group(grade_service, assignment_id, group):
    grade_service.give_assignment_group(assignment_id, group)

def give_assignment_to_a_student(grade_service, assignment_id, student_id):
    grade_service.give_assignment_student(assignment_id, student_id)

def remove_student_and_delete_his_assignments(student_service, student_id):
    student_service.remove_student_and_delete_assignments(student_id)

def remove_assignment_delete_grades(assignment_service, assignment_id):
    assignment_service.remove_assignment_delete_grades(assignment_id)


class UndoHandlers(Enum):
    ADD_STUDENT = add_student_handler
    UPDATE_STUDENT = update_student_handler
    DELETE_ASSIGNMENTS = delete_student_delete_assignments_handler

    ADD_ASSIGNMENT = add_assignment_handler
    UPDATE_ASSIGNMENT = update_assignment_handler
    GIVE_ASSIGNMENT_GROUP = give_assignment_group_handler

    ADD_GRADE = add_grade_handler
    DELETE_GIVEN_ASSIGNMENT = give_assignment_student_handler
    DELETE_ASSIGNMENT_GRADES = delete_assignment_delete_grades_handler

class RedoHandlers(Enum):
    REMOVE_S = remove_s_handler
    UPDATE_S = update_s_handler

    UPDATE_A = update_a_handler

    CHANGE_GRADE_HANDLER = grade_change_handler
    GIVE_ASSIGNMENT_GROUP = give_assignment_to_a_group
    GIVE_ASSIGNMENT_STUDENT = give_assignment_to_a_student
    REMOVE_STUDENT_DELETE_ASSIGNMENTS = remove_student_and_delete_his_assignments
    REMOVE_ASSIGNMENTS_DELETE_GRADES = remove_assignment_delete_grades
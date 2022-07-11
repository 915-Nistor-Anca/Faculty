from dataclasses import dataclass

@dataclass
class RedoOperation:
    target_object: object
    handler: object
    args: tuple

class RedoManager:
    __redo_operations = []
    __last_operation = ""

    @staticmethod
    def register_operation(target_object, handler, *args):
        RedoManager.__redo_operations.append(RedoOperation(target_object, handler, args))
        print('REDO: ', len(RedoManager.__redo_operations), str(handler))

    @staticmethod
    def redo():
        redo_operation = RedoManager.__redo_operations.pop()
        redo_operation.handler(redo_operation.target_object, *redo_operation.args)

    @staticmethod
    def save_last_operation(command_line):
        if command_line in ["add", "remove", "update", "undo", "give", "grade"]:
            RedoManager.__last_operation = command_line
            print('Iupi', RedoManager.__last_operation)

    @staticmethod
    def return_last_operation():
        return RedoManager.__last_operation

    @staticmethod
    def empty_list():
        RedoManager.__redo_operations = []
        RedoManager.__last_operation = ""
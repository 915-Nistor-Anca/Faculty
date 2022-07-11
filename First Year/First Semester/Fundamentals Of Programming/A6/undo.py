from dataclasses import dataclass

@dataclass
class UndoOperation:
    target_object: object
    handler: object
    args: tuple

class UndoManager:
    __undo_operations = []

    @staticmethod
    def register_operation(target_object, handler, *args):
        UndoManager.__undo_operations.append(UndoOperation(target_object, handler, args))
        print('UNDO: ', len(UndoManager.__undo_operations), str(handler))
    @staticmethod
    def undo():
        undo_operation = UndoManager.__undo_operations.pop()
        undo_operation.handler(undo_operation.target_object, *undo_operation.args)



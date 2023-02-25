#include "ui.h"
#include "repository.h"
#include "service.h"
#include <crtdbg.h>
#include "tests.h"
int main() {
    Repository* repository = create_repository();
    Operation_Stack* op = create_operation_stack();
    Operation_Stack* op2 = create_operation_stack();
    Service* service = create_service(repository, op, op2);
    UI* ui = create_ui(service);
    test_all();
    start_ui(ui);
    destroy_ui(ui);
    _CrtDumpMemoryLeaks();
    return 0;
}
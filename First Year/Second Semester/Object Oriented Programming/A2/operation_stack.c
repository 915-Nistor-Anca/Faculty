#include "operation_stack.h"
#include <stdlib.h>
#include <stdio.h>

Operation_Stack* create_operation_stack()
{
    Operation_Stack* op_stack = malloc(sizeof(Operation_Stack));
    if (op_stack == NULL) return NULL;
    op_stack->ops = create_dynamic_array(10, &destroy_operation);
    if (op_stack->ops == NULL) return NULL;
    return op_stack;
}

void destroy_operation_stack(Operation_Stack* op_stack)
{
    destroy_dynamic_array(op_stack->ops);
    free(op_stack);
}

void push(Operation_Stack* op_stack, Operation* operation)
{
    add(op_stack->ops, operation);
}

Operation* pop(Operation_Stack* op_stack)
{
    int pos = get_length(op_stack->ops) - 1;
    Operation* op = copy_operation(get(op_stack->ops, pos));
    delete(op_stack->ops, pos);
    return op;
}

int is_empty(Operation_Stack* op_stack)
{
    return get_length(op_stack->ops) == 0;
}

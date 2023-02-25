#pragma once
#include "dynamic_array.h"
#include "operation.h"

typedef struct{
    Dynamic_Array* ops;
}Operation_Stack;

Operation_Stack* create_operation_stack();
void destroy_operation_stack(Operation_Stack*);
void push(Operation_Stack*, Operation*);
Operation* pop(Operation_Stack*);
int is_empty(Operation_Stack*);
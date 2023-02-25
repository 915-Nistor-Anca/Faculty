#pragma once
#include "material.h"

typedef struct{
    Material* material;
    char* operation_name;
}Operation;

Operation* create_operation(Material*, char*);
Operation* copy_operation(Operation*);
void destroy_operation(Operation*);
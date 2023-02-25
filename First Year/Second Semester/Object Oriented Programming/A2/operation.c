#include "operation.h"
#include <string.h>
#include <stdlib.h>
#include <stdio.h>

Operation* create_operation(Material* m, char* operation_name)
{
    /*This function creates an operation with a material and a name.
     * Return: null, if the material or the operation name are null or the created operation.*/
    Operation* operation = malloc(sizeof(Operation));
    if (operation == NULL) return NULL;
    operation->material = copy_material(m);
    operation->operation_name = malloc(sizeof(char)* strlen(operation_name)+1);
    if (operation->operation_name == NULL) return NULL;
    strcpy(operation->operation_name, operation_name);
    return operation;
}

Operation* copy_operation(Operation* operation)
{
    /*Return: a copy of the given operation.*/
    return create_operation(operation->material, operation->operation_name);
}

void destroy_operation(Operation* operation)
{
    /*This function destroys the operation.*/
    destroy_material(operation->material);
    free(operation->operation_name);
    free(operation);
}
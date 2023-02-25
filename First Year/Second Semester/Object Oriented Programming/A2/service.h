#pragma once
#include "repository.h"
#include "operation_stack.h"
#include <stdlib.h>
typedef struct
{
    Repository * repo;
    Operation_Stack* undo_stack;
    Operation_Stack* redo_stack;
}Service;

Service* create_service(Repository* repo, Operation_Stack* undo_stack, Operation_Stack* redo_stack);
void destroy_service(Service* s);
Repository* get_repository(Service* s);
int add_material_service(Service* s, char* name, char* supplier, int quantity, char* expiration_date);
int delete_material_service(Service* s, char* name, char *supplier, char* expiration_date);
int find_by_name_supplier_exp_date_service(Service* s, char* name, char* supplier, char* expiration_date);
int is_the_material_expired(char* expiration_date, int c_day, int c_month, int c_year);
void sort_positions(Service* s, int positions[100], int k);

void undo(Service* s);
void update(Service* s);
void redo(Service* s);

int add_material_service_2(Service* s, char* name, char* supplier, int quantity, char* expiration_date);
int delete_material_service_2(Service* s, char* name, char* supplier, char* expiration_date);
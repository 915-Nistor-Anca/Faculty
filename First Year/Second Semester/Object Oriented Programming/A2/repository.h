#pragma once
#include "dynamic_array.h"
#include "material.h"

typedef struct
{
    Dynamic_Array* elements;
}Repository;

Repository * create_repository();
void destroy_repository(Repository* repo);
int add_material_repository(Repository* repo, Material * m);
int delete_material_repository(Repository* repo, char* name, char* supplier, char* expiration_date);
int find_by_name_supplier_expdate(Repository* repo, char* name, char* supplier, char* expiration_date);
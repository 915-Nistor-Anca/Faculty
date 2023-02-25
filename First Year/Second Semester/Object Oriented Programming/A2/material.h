#pragma once

typedef struct
{
    char* name;
    char* supplier;
    char* expiration_date;
    int quantity;
}Material;

Material* create_material(char* name, char* supplier, int quantity, char* expiration_date);
void destroy_material(Material* m);
char* get_name(Material* m);
char* get_supplier(Material* m);
char* get_expiration_date(Material* m);
int get_quantity(Material* m);
Material* copy_material(Material* m);
#include "material.h"
#include <string.h>
#include <stdlib.h>

Material* create_material(char * name, char * supplier,  int quantity, char * expiration_date)
{
    /*
     * The function allocates space for a new material which receives the given name, supplier, quantity and expiration date.
     * Parameters name, supplier, expiration date: char, the data of the material which has to be created.
     * Parameter quantity: of type int, representing the quantity of the material.
     * Return: the created material.
     */
    Material* m = malloc(sizeof(Material));
    m->name = malloc(sizeof(char)* (strlen(name)+1));
    strcpy(m->name, name);

    m->supplier = malloc(sizeof(char)* (strlen(supplier)+1));
    strcpy(m->supplier, supplier);

    m->quantity = quantity;
    m->expiration_date = malloc(sizeof(char)* (strlen(expiration_date)+1));
    strcpy(m->expiration_date, expiration_date);

    return m;
}

char* get_name(Material* m)
{
    /*
     *Return: the material's name.
     */
    return m->name;
}

char* get_supplier(Material* m)
{
    /*
     *Return: the material's  supplier.
     */
    return m->supplier;
}

char* get_expiration_date(Material* m)
{
    /*
    *Return: the material's expiration date.
    */
    return m->expiration_date;
}

int get_quantity(Material* m)
{
    /*
    *Return: the material's quantity.
    */
    return m->quantity;
}


void destroy_material(Material* m)
{
    /*This function destroys the given material.*/
    free(m->name);
    free(m->supplier);
    free(m->expiration_date);
    free(m);
}

Material* copy_material(Material* m)
{
    /*This function creates a copy of the given material.
     *Return: the material which was copied.*/
    if (m == NULL) return NULL;
    Material* new_material = create_material(get_name(m), get_supplier(m), get_quantity(m), get_expiration_date(m));
    return new_material;
}
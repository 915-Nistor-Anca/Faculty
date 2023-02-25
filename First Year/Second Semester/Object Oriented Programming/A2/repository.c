#include "repository.h"
#include "material.h"
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

Repository * create_repository()
{
    /* This function creates a repository. It allocates space for the repository and it creates its dynamic array.
     * Return: the created repository.*/
    Repository * repo = malloc(sizeof(Repository));
    if (repo == NULL) return NULL;
    repo->elements = create_dynamic_array(10, &destroy_material);
    if (repo->elements == NULL) return NULL;
    return repo;
}

void destroy_repository(Repository* repo)
{
    /* This function destroys the repository.
     * Parameter repo: the repository*/
    destroy_dynamic_array(repo->elements);
    free(repo);
}

int find_by_name_supplier_expdate(Repository* repo, char* name, char* supplier, char* expiration_date)
{
    /*This function receives a name, a supplier and an expiration date and searches, in the list of elements, for the
     * material which has the same given data.
     * Parameter repo: the repository.
     * Parameter name, supplier, expiration date: the data.
     * Return: the position of the element or -1 if it wasn't found.*/
    Material* m;
    for (int i = 0; i< get_length(repo->elements); i++)
    {
        m = get(repo->elements, i);
        if (strcmp(m->name, name) == 0 && strcmp(m->supplier, supplier) == 0 && strcmp(m->expiration_date, expiration_date) == 0)
            return i;
    }
    return -1;
}

int add_material_repository(Repository* repo, Material* m)
{
    /*This function adds the given material to the list of materials.
     * If the material already exists, the new quantity id added to the old one.
     * Paramaters: repo - the repository, m - the material which is to be added.
     * Return: 0, if the repository does not exist.
     * 1, if the material is new and it was added.
     * 2, if the material has already existed, but the new quantity has been added to its old one.*/
    if (repo == NULL || m == NULL) return 0;
    int pos = find_by_name_supplier_expdate(repo, m->name, m->supplier, m->expiration_date);
    if (pos != -1)
    {
        Material* m2 = get(repo->elements, pos);
        delete_material_repository(repo, get_name(m), get_supplier(m), get_expiration_date(m));
        Material* m3 = create_material(get_name(m), get_supplier(m), get_quantity(m) + get_quantity(m2),
                                       get_expiration_date(m));
        add(repo->elements, m3);
        return 2;
    }
    add(repo->elements, copy_material(m));
    return 1;


}

int delete_material_repository(Repository* repo, char* name, char* supplier, char* expiration_date)
{
    /*
     * This function deletes the material with the given name, supplier and expiration date from the list of materials.
     * Return: 0, if the material wasn't found/deleted; 1, if it was deleted.
     * */
    int pos = find_by_name_supplier_expdate(repo, name, supplier, expiration_date);
    if (pos == -1) return 0;
    delete(repo->elements, pos);
    return 1;
}

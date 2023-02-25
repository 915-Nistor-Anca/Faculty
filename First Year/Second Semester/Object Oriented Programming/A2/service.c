#include "service.h"
#include <stdlib.h>
#include <string.h>

Service* create_service(Repository* repo, Operation_Stack* undo_stack, Operation_Stack* redo_stack)
{
    /*This function creates a new service.
     * Return: null or the created service.*/
    Service* s = (Service*)malloc(sizeof(Service));
    if (s == NULL) return NULL;
    s->repo = repo;
    s->undo_stack = undo_stack;
    s->redo_stack = redo_stack;
    return s;
}

void destroy_service(Service *s)
{
    /*This function destroys the given service.*/
    destroy_repository(s->repo);
    destroy_operation_stack(s->undo_stack);
    destroy_operation_stack(s->redo_stack);
    free(s);
}

int add_material_service(Service* s, char* name, char* supplier, int quantity, char* expiration_date)
{
    /*This function creates a material with the given data and adds it in the list of materials.
     * Return: 1, if the material is new, 2 if it isn't and 0 if it wasn't added.*/
    Material* m = create_material(name,supplier,quantity,expiration_date);
    int result = add_material_repository(s->repo, m);
    if (result == 1 || result == 2)
    {
        Operation* operation = create_operation(m, "add");
        push(s->undo_stack, operation);
    }
    destroy_material(m);
    return result;
}

int add_material_service_2(Service* s, char* name, char* supplier, int quantity, char* expiration_date)
{
    /*
     * This function adds a material without adding anything in the undo stack.
     * Return: 1, if the material is new, 2 if it isn't and 0 if it wasn't added.*/
    Material* m = create_material(name,supplier,quantity,expiration_date);
    int result = add_material_repository(s->repo, m);
    destroy_material(m);

    return result;
}

int delete_material_service_2(Service* s, char* name, char* supplier, char* expiration_date)
{
    /*This function deletes a material, without adding anything in the undo stack.*/
    int result =  delete_material_repository(s->repo, name, supplier, expiration_date);
    return result;
}

void undo(Service* s) {
    /*
     * This function undoes the last operation. If the last operation was named "add", the program will delete
     * the material from the list which matches the material of the operation. If the operation name is "delete",
     * it will add the material. If it is "update", it will delete the new material and add the old one.*/
    if (is_empty(s->undo_stack)) return;

    Operation *operation = pop(s->undo_stack);

    if (strcmp(operation->operation_name, "add") == 0) {
        delete_material_service_2(s, get_name(operation->material), get_supplier(operation->material),
                                  get_expiration_date(operation->material));
        Material* m = create_material(get_name(operation->material), get_supplier(operation->material), get_quantity(operation->material),
                                      get_expiration_date(operation->material));
        Operation* o = create_operation(m, "add");
        push(s->redo_stack, copy_operation(o));
        destroy_material(m);
        destroy_operation(o);

    } else if (strcmp(operation->operation_name, "delete") == 0) {
        add_material_service_2(s, get_name(operation->material), get_supplier(operation->material),
                               get_quantity(operation->material),
                               get_expiration_date(operation->material));
       Material* m = create_material(get_name(operation->material), get_supplier(operation->material), get_quantity(operation->material),
                                      get_expiration_date(operation->material));
        Operation* o = create_operation(m, "delete");
        push(s->redo_stack, copy_operation(o));
        destroy_material(m);
        destroy_operation(o);

    } else if (strcmp(operation->operation_name, "update") == 0) {
        // it firstly deletes the updated operation
        Operation *op = pop(s->undo_stack);
        delete_material_service_2(s, get_name(op->material), get_supplier(op->material),
                                  get_expiration_date(op->material));

        Material *m1 = create_material(get_name(op->material), get_supplier(op->material), get_quantity(op->material),
                                       get_expiration_date(op->material));
        Operation *opp = create_operation(m1, "add");
        push(s->redo_stack, copy_operation(opp));
        destroy_operation(opp);
        destroy_material(m1);
        destroy_operation(op);

        // then it adds the initial one (before the update was done)
        Operation *op2 = pop(s->undo_stack);
        add_material_service_2(s, get_name(op2->material), get_supplier(op2->material),
                               get_quantity(op2->material),
                               get_expiration_date(op2->material));

        Material *m2 = create_material(get_name(op2->material), get_supplier(op2->material),
                                       get_quantity(op2->material),
                                       get_expiration_date(op2->material));
        Operation* opp2 = create_operation(m2, "delete");
        push(s->redo_stack, copy_operation(opp2));
        destroy_operation(opp2);
        destroy_material(m2);
        destroy_operation(op2);

        Material* m = create_material(get_name(operation->material), get_supplier(operation->material), get_quantity(operation->material),
                                      get_expiration_date(operation->material));
        Operation* o = create_operation(m, "update");
        push(s->redo_stack,copy_operation(o));
        destroy_operation(o);
        destroy_material(m);

    }
    destroy_operation(operation);
}

void redo(Service* s)
{
    /*This function redoes the operation which was done before the undo.*/
    if (is_empty(s->redo_stack)) return;

    Operation* operation = pop(s->redo_stack);
    if (strcmp(operation->operation_name, "add") == 0)
        add_material_service_2(s, get_name(operation->material), get_supplier(operation->material), get_quantity(operation->material),
                             get_expiration_date(operation->material));
    else if (strcmp(operation->operation_name, "delete") == 0)
        delete_material_service_2(s, get_name(operation->material), get_supplier(operation->material), get_expiration_date(operation->material));
    else if (strcmp(operation->operation_name, "update") == 0)
    {

        Operation *op2 = pop(s->redo_stack);
        delete_material_service_2(s, get_name(op2->material), get_supplier(op2->material),
                                  get_expiration_date(op2->material));
        destroy_operation(op2);
        Operation *op = pop(s->redo_stack);
        add_material_service_2(s, get_name(op->material), get_supplier(op->material), get_quantity(op->material),
                               get_expiration_date(op->material));
        destroy_operation(op);





    }
}

void update(Service* s)
{
    Material* m = create_material("name", "supplier", 100, "expiration_date"); ///the material which was deleted and needs to be added
    Operation* operation = create_operation(m, "update");
    push(s->undo_stack, operation);
}

Repository* get_repository(Service* s)
{
    return s->repo;
}

int delete_material_service(Service* s, char* name, char* supplier, char* expiration_date)
{
    /*This function deletes the material which matches the given data and saves the material in the undo stack.
     * Return: 0, if the material was not deleted, and */
    int pos = find_by_name_supplier_exp_date_service(s,name,supplier,expiration_date);
    if (pos == -1) return 0;
    Material* m = get(s->repo->elements, pos);
    m = copy_material(m);
    int result =  delete_material_repository(s->repo, name, supplier, expiration_date);
    if (result == 1)
    {

        Operation* operation = create_operation(m, "delete");
        push(s->undo_stack, operation);
    }
    destroy_material(m);
    return result;
}


int find_by_name_supplier_exp_date_service(Service* s, char* name, char* supplier, char* expiration_date)
{
    /*This function receives a name, a supplier and an expiration date and searches, in the list of elements, for the
     * material which has the same given data.
     * Parameter repo: the repository.
     * Parameter name, supplier, expiration date: the data.
     * Return: the position of the element or -1 if it wasn't found.*/
    return find_by_name_supplier_expdate(s->repo, name, supplier, expiration_date);
}

int is_the_material_expired(char* expiration_date, int c_day, int c_month, int c_year)
{
    /*This function checkes if a material is expired, comparing the current date to the expiration date.
     * Return: 1, if it is expired and 0 if not.*/
    char copy[50];
    strcpy(copy, expiration_date);
    int day, month, year;
    day = atoi(copy);
    month = atoi(copy+3);
    year = atoi(copy+6);
    //printf("YEAR %d, MONTH %d, DAY %d ", year, month, day);
    if (year < c_year) return 1;
    else {
        if (month < c_month) return 1;
        else if (day < c_day) return 1;
    }
    return 0;
}

void sort_positions(Service* s, int positions[100], int k)
{
    /*This function uses bubble sort to sort a vector of positions with respect to the elements' quantity from the
     * list of materials.*/
    int ok;
    do {
        ok = 1;
        for (int i = 0; i<k; i++) {
            if (get_quantity(get(s->repo->elements, positions[i])) >
                get_quantity(get(s->repo->elements, positions[i + 1]))) {
                ok = 0;
                int aux = positions[i];
                positions[i] = positions[i + 1];
                positions[i + 1] = aux;
            }
        }
    } while (ok == 0);
}
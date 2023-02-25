#include <assert.h>
#include "tests.h"
#include "material.h"
#include "dynamic_array.h"
#include <string.h>
#include "operation.h"
#include <stdio.h>
#include "operation_stack.h"
#include "repository.h"
#include "service.h"

void test_dynamic_array()
{
    /*Material* m = create_material("abc", "def", 100, "13.10.2021");
    Dynamic_Array* d = create_dynamic_array(5, &destroy_material);
    add(d, m);
    assert(d->elements != NULL);
    delete(d, 0);
    assert(d->length == 0);
    resize(d);
    add(d,m);
    Material *m2 = create_material("abcd", "defg", 110, "15.10.2021");
    add(d, m2);
    Material *m3 = create_material("abcde", "defgh", 1100, "15.02.2021");
    add(d, m3);
    delete(d,1);
    resize(d);*/
    Material* m = create_material("abc", "def", 100, "13.10.2021");
    Dynamic_Array* d = create_dynamic_array(5, &destroy_material);
    //resize(d);
    destroy_material(m);
    destroy_dynamic_array(d);
    /*destroy_material(m2);
    destroy_material(m3);
    */

}


void test_operation()
{
    Material* m = create_material("abc", "def", 100, "13.10.2021");
    Operation * operation = create_operation(m, "add");
    Operation* operation2 = copy_operation(operation);
    assert(strcmp(operation2->operation_name, "add") == 0);
    //Dynamic_Array* d = create_dynamic_array(10, &destroy_material);
    
    //add(d,operation2);
    destroy_material(m);
    destroy_operation(operation);
    destroy_operation(operation2);
    
}

void test_operation_stack()
{
    Operation_Stack* os = create_operation_stack();
    assert(is_empty(os) == 1);
    Material* m = create_material("abc", "def", 100, "13.10.2021");
    push(os, create_operation(m, "add"));
    pop(os);
    destroy_material(m);
    destroy_operation_stack(os);
   
    
}

void test_repo()
{
    Repository *repo = create_repository();
    add_material_repository(repo, create_material("abc","def", 100, "21.10.2021"));
    add_material_repository(repo, create_material("abc","def", 100, "21.10.2021"));
    destroy_repository(repo);

}

void test_service()
{
    Repository* repo = create_repository();
    Operation_Stack* op = create_operation_stack();
    Operation_Stack* op2 = create_operation_stack();
    Service* s = create_service(repo, op, op2);
    add_material_service_2(s, "abc", "def", 100, "21.10.2021");
    delete_material_service_2(s, "abc", "def", "21.10.2021");
    undo(s);
    redo(s);
    update(s);
    delete_material_service(s, "abc", "def", "21.10.2021");
    add_material_service(s, "abc", "def", 100, "21.10.2021");
    delete_material_service(s, "abc", "def", "21.10.2021");
    undo(s);
    redo(s);
    add_material_service(s, "abcd", "defg", 150, "21.10.2021");
    delete_material_service(s, "abcd", "defg", "21.10.2021");
    add_material_service(s, "milk", "def", 100, "21.10.2023");
    Material * m = create_material("flour", "adjoa", 300, "13.07.2022");
    Operation * operation = create_operation(m, "update");
    push(s->undo_stack, operation);
    destroy_material(m);
    Material * m1 = create_material("milk", "jda", 300, "13.10.2022");
    Operation * operation2 = create_operation(m1, "update");
    push(s->redo_stack, operation2);
    undo(s);
    undo(s);
    undo(s);
    redo(s);
    redo(s);
    redo(s);
    Repository * r = get_repository(s);
    destroy_service(s);
    int x = is_the_material_expired("21.10.2021", 5, 10, 2021);
    assert(x==0);

}

void test_service_2()
{
    Repository * r = create_repository();
    Operation_Stack* op = create_operation_stack();
    Operation_Stack* op2 = create_operation_stack();
    Service* s = create_service(r, op, op2);
    add_material_service(s, "abc", "def", 80, "21.10.2021");
    add_material_service(s, "oafj", "aok", 50, "21.10.2021");
    add_material_service(s, "afjia", "jsoj", 100, "15.01.2020");
    int pos[100];
    sort_positions(s,pos,3);
    assert(pos[0] == 2);
    //destroy_repository(r);
    //destroy_operation_stack(op);
    //destroy_operation_stack(op2);
    destroy_service(s);
}

void test_all()
{
    test_dynamic_array();
    test_operation();
    //test_operation_stack();
    //test_repo();
    //test_service();
    //test_service_2();

}
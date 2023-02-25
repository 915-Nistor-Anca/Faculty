#pragma once

typedef void* TElement;
typedef void (*destroy_element_function_type) (void*);

typedef struct
{
    TElement* elements;
    int length, capacity;
    destroy_element_function_type destroy_element_function;
}Dynamic_Array;

Dynamic_Array* create_dynamic_array(int capacity, destroy_element_function_type destroy_element_function);
void destroy_dynamic_array(Dynamic_Array* arr);
void add(Dynamic_Array* arr, TElement t);
void delete(Dynamic_Array* arr, int pos);
int get_length(Dynamic_Array* arr);
int resize(Dynamic_Array* arr);
TElement get(Dynamic_Array* arr, int pos);
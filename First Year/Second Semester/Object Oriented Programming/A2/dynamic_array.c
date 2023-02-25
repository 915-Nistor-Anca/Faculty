#include "dynamic_array.h"
#include <stdlib.h>

Dynamic_Array* create_dynamic_array(int capacity, destroy_element_function_type destroy_element_function)
{
    /*
     * This function creates allocates space for a dynamic array.
     * Return: the created dynamic array.*/
    Dynamic_Array* dynamic_array  = (Dynamic_Array*)malloc(sizeof(Dynamic_Array));
    if (dynamic_array == NULL) return NULL;
    dynamic_array->capacity = capacity;
    dynamic_array->length = 0;
    dynamic_array->elements = (TElement*)malloc(capacity*sizeof(TElement));
    if (dynamic_array->elements == NULL) return NULL;
    dynamic_array->destroy_element_function = destroy_element_function;
    return dynamic_array;
}

void destroy_dynamic_array(Dynamic_Array* arr)
{
    /*
     * This function destroys the given dynamic array. It deallocates space for each element of the array and then it frees it.*/
    if (arr == NULL) return;
    for (int i = 0; i< arr->length; i++)
        arr->destroy_element_function(arr->elements[i]);
    free(arr->elements);
    arr->elements = NULL;
    free(arr);
    arr = NULL;
}

int resize(Dynamic_Array* arr)
{
    /*
     * This function resizes the given dynamic array.
     * Return: 0, if it could successfully resize it, or -1 if the array is null.*/
    if (arr == NULL) return -1;
    arr->capacity*=2;
    TElement* aux = (TElement*)malloc(arr->capacity * sizeof(TElement));
    if (aux == NULL) return -1;
    for (int i = 0; i < arr->length; i++)
        aux[i] = arr->elements[i];
    free(arr->elements);
    arr->elements = aux;
    return  0;
}

void add(Dynamic_Array* arr, TElement t)
{
    /*
     * This function adds an element to the dynamic array.
     */
    if (arr == NULL) return;
    if (arr->elements == NULL) return;
    if (arr->length == arr->capacity)
        resize(arr);
    arr->elements[arr->length++] = t;
}

void delete(Dynamic_Array* arr, int position)
{
    /*This function deletes the element from the given position in the array.*/
    if (arr == NULL) return;
    if (arr->elements == NULL) return;
    if (position < 0 || position >= arr->length) return;
    arr->destroy_element_function(arr->elements[position]);
    for (int i = position; i < arr->length - 1; i++)
        arr->elements[i] = arr->elements[i+1];
    arr->length--;
}

int get_length(Dynamic_Array* arr)
{
    /*Return: -1, if the array is null or the length of the array.*/
    if (arr == NULL) return -1;
    return arr->length;
}

TElement get(Dynamic_Array* arr, int position)
{
    /*Return: the element from the given position in the dynamic array.*/
    return arr->elements[position];
}
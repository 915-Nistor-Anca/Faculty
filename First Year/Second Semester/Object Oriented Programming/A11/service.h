
#pragma once

#include "repository.h"

class Service
{
    Repository& repo;
public:
    Service(Repository& repo);
    ~Service();
    /* Adds a new dog to the list of dogs, with the given data. The dog is added if there is no other dog with the same name.
     * Return: 1, if the dog was added and 0, if it was not.
    */
    int add_dog_service(const std::string& breed, const std::string& name, const int& age, const std::string& photograph);


    /* Searches for the dog with the given name in the list of dogs.
     * Return: the position on which the dog is, if it can be found or -1, if there is no dog with that name.
     * */
    int search_dog_by_name(const std::string& name);


    /*Returns how many dogs are in the list.*/
    int get_number_of_dogs();


    /*Returns the dog which can be found on the given position.*/
    Dog get_dog_on_given_position(int pos);

    /*Returns the list of dogs.*/
    std::vector<Dog> get_dogs();

    /*Deletes the dog from the given position.*/
    void delete_dog_service(int pos);

    void read_file();
    void write_to_file();

    Service& operator = (const Service& serv);
    void getFiltered(std::vector<Dog>& valid_dogs, const std::string& filter_string, int age_filter);
};
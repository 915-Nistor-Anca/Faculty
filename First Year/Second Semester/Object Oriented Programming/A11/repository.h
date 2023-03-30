#pragma once
#include "domain.h"
#include <vector>
class Repository
{
private:
    std::vector<Dog> dogs;
    std::string file_name;
public:
    Repository(const std::string& file_name);
    Repository();
    ~Repository();
    //Returns the list of dogs.
    std::vector<Dog> get_dogs();

    //Adds the dog to the list of dogs.
    void add_dog(const Dog&);

    //Returns how many dogs are in the list.
    int get_number_of_dogs();

    //Returns the dog on the given position.
    Dog get_dog_on_given_position(int pos);

    //Deletes the dog on the given position.
    void delete_dog(int position);

    int find_dog_with_given_name(const std::string& name);

    void load_data();
    void write_data();
};
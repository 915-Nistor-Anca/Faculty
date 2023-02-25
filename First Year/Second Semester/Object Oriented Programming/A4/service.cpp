#include "service.h"
#include <string.h>
#include <iostream>
Service::Service(Repository &repo): repo{repo} {
    this->repo = repo;
}

int Service::search_dog_by_name(const string &name) {
    Dog* list_of_dogs = this->repo.get_dogs();
    int length = this->repo.get_number_of_dogs();
    if (length < 1) return -1;
    for (int i = 0; i < length; i++)
    {
        Dog dog = list_of_dogs[i];
        string dog_name = dog.get_name();
        if (name == dog_name) return i;
    }
    return -1;
}

int Service::add_dog_service(const string &breed, const string &name, const int &age, const string &photograph) {

    int search = search_dog_by_name(name);
    if (search == -1) {
        Dog new_dog(breed, name, age, photograph);
        repo.add_dog(new_dog);
        return 1;
    }
    else return 0;
}

int Service::get_number_of_dogs(){
    return this->repo.get_number_of_dogs();
}

Dog* Service::get_dogs() {
    return this->repo.get_dogs();
}

Dog Service::get_dog_on_given_position(int pos){
    return this->repo.get_dog_on_given_position(pos);
}

void Service::delete_dog_service(int pos){
    this->repo.delete_dog(pos);
}
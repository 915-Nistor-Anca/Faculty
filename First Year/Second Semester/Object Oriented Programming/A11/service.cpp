#include "service.h"
#include <string.h>
#include <iostream>
#include <algorithm>

Service::Service(Repository& repo) : repo{ repo } {
    this->repo = repo;
}


Service::~Service()
{
}

int Service::search_dog_by_name(const std::string& name) {
    std::vector<Dog> list_of_dogs = this->repo.get_dogs();
    int length = this->repo.get_number_of_dogs();
    if (length < 1) return -1;
    for (int i = 0; i < length; i++)
    {
        Dog dog = list_of_dogs[i];
        std::string dog_name = dog.get_name();
        if (name == dog_name) return i;
    }
    return -1;
}

int Service::add_dog_service(const std::string& breed, const std::string& name, const int& age, const std::string& photograph) {

    /*int search = search_dog_by_name(name);
    if (search == -1) {
        Dog new_dog(breed, name, age, photograph);
        repo.add_dog(new_dog);
        return 1;
    }
    else return 0;*/

    int k = this->get_number_of_dogs();
    Dog new_dog(breed, name, age, photograph);
    repo.add_dog(new_dog);
    if (k < this->get_number_of_dogs()) return 1;
    return 0;

}

int Service::get_number_of_dogs() {
    return this->repo.get_number_of_dogs();
}

std::vector<Dog> Service::get_dogs() {
    return this->repo.get_dogs();
}

Dog Service::get_dog_on_given_position(int pos) {
    return this->repo.get_dog_on_given_position(pos);
}

void Service::delete_dog_service(int pos) {
    this->repo.delete_dog(pos);
}

void Service::read_file()
{
    this->repo.load_data();
}

void Service::write_to_file() {
    this->repo.write_data();
}

Service& Service::operator=(const Service& serv)
{
    this->repo = serv.repo;
    return *this;
}


void Service::getFiltered(std::vector<Dog>& valid_dogs, const std::string& filter_string, int age_filter) {
    std::vector<Dog> data;
    data = this->repo.get_dogs();
    if (filter_string[0] == '\0') {
        std::copy_if(data.begin(), data.end(), std::back_inserter(valid_dogs), [&age_filter](Dog& dog) { return dog.get_age() < age_filter; });
    }
    else {
        std::copy_if(data.begin(), data.end(), std::back_inserter(valid_dogs), [&age_filter, &filter_string](Dog& dog) { return dog.get_age() < age_filter && dog.get_breed() == filter_string; });
    }
}
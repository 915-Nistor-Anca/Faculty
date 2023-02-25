
#include "domain.h"

Dog::Dog()
    :breed(""), name(""), age(), photograph("")
{
}

Dog::Dog(const string &breed, const string &name, const int &age, const string &photograph)
    : breed(breed), name(name), age(age), photograph(photograph)
{
}

Dog::Dog(const Dog &dog)
    :breed(dog.breed), name(dog.name), age(dog.age), photograph(dog.photograph)
{
}

string Dog::get_breed() {
    return this->breed;
}

string Dog::get_name() {
    return this->name;
}

int Dog::get_age() {
    return this->age;
}

string Dog::get_photograph() {
    return this->photograph;
}
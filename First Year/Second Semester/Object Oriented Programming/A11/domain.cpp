
#include "domain.h"
#include <sstream>
#include <vector>

using namespace std;


Dog::Dog()
    :breed(""), name(""), age(), photograph("")
{
}

Dog::Dog(const string& breed, const string& name, const int& age, const string& photograph)
    : breed(breed), name(name), age(age), photograph(photograph)
{
}

Dog::Dog(const Dog& dog)
    : breed(dog.breed), name(dog.name), age(dog.age), photograph(dog.photograph)
{
}

Dog::~Dog()
{
}

string Dog::get_breed() {
    return this->breed;
}

string Dog::get_name() const {
    return this->name;
}

int Dog::get_age() {
    return this->age;
}

string Dog::get_photograph() {
    return this->photograph;
}

std::string Dog::to_string()
{
    return this->get_breed() + "-" + this->get_name() + "-" + std::to_string(this->get_age())
        + "-" + this->get_photograph() + "\n";
}

std::ostream& operator<<(std::ostream& output, const Dog& dog)
{
    output << dog.breed << ',' << dog.name << ',' << std::to_string(dog.age) << ',' << dog.photograph << endl;
    return output;
}

istream& operator>>(istream& input, const Dog& dog)
{
    string line;
    getline(input, line);
    string breed, name, age, photograph;
    breed = "";
    name = "";
    age = "";
    photograph = "";
    int pos = 0, k = 0;
    for (int i = 0; i < line.length(); i++) {
        if (line[i] == ',') {
            for (int j = pos; j < i; j++) {
                if (k == 0) breed += line[j];
                else if (k == 1) name += line[j];
                else if (k == 2) age += line[j];
            }
            k++;
            pos = i + 1;
        }
    }
    for (int j = pos; j < line.length(); j++) photograph += line[j];
    if (age != "")
    {
        int age2 = stoi(age);
        Dog dog2(breed, name, age2, photograph);
    }
    return input;
}

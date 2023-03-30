
#include "repository.h"
#include "exceptions.h"
#include <iostream>
#include <fstream>

std::ifstream fin("data.txt");

Repository::Repository(const std::string& file_name) {
    this->file_name = file_name;
}

Repository::Repository()
{
}

Repository::~Repository()
{
}

std::vector<Dog> Repository::get_dogs() {
    return this->dogs;
}

int Repository::get_number_of_dogs() {
    return int(dogs.size());
};

void Repository::add_dog(const Dog& dog) {

    for (auto& d : dogs)
        if (dog.get_name() == d.get_name())
            throw DogAlreadyExists();

    dogs.push_back(dog);
}

Dog Repository::get_dog_on_given_position(int pos) {
    std::vector<Dog> dogs = get_dogs();
    return dogs[pos];
}

void Repository::delete_dog(int position) {
    dogs.erase(dogs.begin() + position);
}

int Repository::find_dog_with_given_name(const std::string& name)
{
    int i = 0;
    for (auto& dog : dogs) {
        if (dog.get_name() == name) return i;
        i++;
    }
    return -1;
}

void Repository::load_data() {
    std::string line;
    std::string breed, name, age, photograph;
    breed = "";
    name = "";
    age = "";
    photograph = "";
    int pos = 0, k = 0;
    std::ifstream file(this->file_name);
    if (file.is_open())
    {
        while (getline(file, line)) {
            pos = 0, k = 0;
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
                Dog dog(breed, name, age2, photograph);
                dogs.push_back(dog);
                std::cout << "Dog added " << breed << std::endl;
                breed = "";
                name = "";
                age = "";
                photograph = "";
            }
        }
        file.close();
    }
}

void Repository::write_data() {
    std::ofstream file;
    file.open(this->file_name);
    for (auto& dog : dogs)
        file << dog;
    file.close();
}

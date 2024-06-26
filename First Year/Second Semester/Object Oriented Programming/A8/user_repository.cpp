#include "user_repository.h"

User_Repository::User_Repository() = default;

User_Repository:: ~User_Repository() = default;

vector<Dog> User_Repository::get_all_dogs() {
    return this->adoption_list;
}

void User_Repository::add_dog(Dog &dog) {
    adoption_list.push_back(dog);
}

int User_Repository::get_number_of_dogs(){
    return this->adoption_list.size();
}
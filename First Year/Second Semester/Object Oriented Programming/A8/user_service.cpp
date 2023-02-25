#include "user_service.h"

User_Service::User_Service(Repository &repo, User_Repository &user_repo): repository{repo}, user_repository{user_repo} {
    this->repository = repo;
    this->user_repository = user_repo;
}

vector<Dog> User_Service::get_all_dogs() {
    return this->user_repository.get_all_dogs();
}

void User_Service::add_dog(Dog dog) {
    this->user_repository.add_dog(dog);
    int pos = this->repository.find_dog_with_given_name(dog.get_name());
    this->repository.delete_dog(pos);
}

int User_Service::get_number_of_dogs(){
    return this->user_repository.get_number_of_dogs();
}

User_Service::~User_Service() = default;

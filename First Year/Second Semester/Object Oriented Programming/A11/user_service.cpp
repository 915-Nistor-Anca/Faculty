#include "user_service.h"

User_Service::User_Service(Repository& repo, User_Repository& user_repo, AdoptionList* list) : repository{ repo }, user_repository{ user_repo }, list{ list } {
    this->repository = repo;
    this->user_repository = user_repo;
    this->list = list;

}

std::vector<Dog> User_Service::get_all_dogs() {
    return this->user_repository.get_all_dogs();
}

void User_Service::add_dog(Dog dog) {
    this->user_repository.add_dog(dog);
    int pos = this->repository.find_dog_with_given_name(dog.get_name());
    this->repository.delete_dog(pos);

    list->add_dog(dog);
}

int User_Service::get_number_of_dogs() {
    return this->user_repository.get_number_of_dogs();
}

std::string User_Service::get_file_name()
{
    return list->get_file_name();
}

User_Service::~User_Service() = default;

User_Service& User_Service::operator=(const User_Service& serv)
{
    this->user_repository = serv.user_repository;
    this->repository = serv.repository;
    this->list = serv.list;
    return *this;
}

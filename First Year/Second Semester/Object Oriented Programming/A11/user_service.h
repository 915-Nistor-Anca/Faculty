#pragma once
#include "user_repository.h"
#include "repository.h"
#include "adoption_list.h"

class User_Service {
private:
    Repository& repository;
    User_Repository& user_repository;
    AdoptionList* list;
public:
    User_Service(Repository& repo, User_Repository& user_repo, AdoptionList* list);
    ~User_Service();

    User_Service& operator=(const User_Service& serv);

    std::vector<Dog> get_all_dogs();
    void add_dog(Dog);


    int get_number_of_dogs();
    std::string get_file_name();
};

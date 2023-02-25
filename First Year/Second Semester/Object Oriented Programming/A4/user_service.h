#include "user_repository.h"
#include "repository.h"

class User_Service{
private:
    Repository& repository;
    User_Repository& user_repository;
public:
    User_Service(Repository& repo, User_Repository& user_repo);
    ~User_Service();

    Dog* get_all_dogs();
    void add_dog(Dog);


    int get_number_of_dogs();
};

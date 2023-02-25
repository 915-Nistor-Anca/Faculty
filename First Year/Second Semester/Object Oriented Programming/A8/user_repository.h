
#include "domain.h"
#include <vector>

class User_Repository{
private:
    vector<Dog> adoption_list;
public:
    User_Repository();
    vector<Dog> get_all_dogs();
    void add_dog(Dog &dog);
    ~User_Repository();

    int get_number_of_dogs();
};

#include "domain.h"
#include <vector>

class User_Repository {
private:
    std::vector<Dog> adoption_list;
public:
    User_Repository();
    std::vector<Dog> get_all_dogs();
    void add_dog(Dog& dog);
    ~User_Repository();

    int get_number_of_dogs();
};
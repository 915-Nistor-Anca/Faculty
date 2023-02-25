#include "dynamic_vector.h"
#include "domain.h"

class User_Repository{
private:
    DynamicVector<Dog> adoption_list;
public:
    User_Repository();
    Dog* get_all_dogs();
    void add_dog(Dog &dog);
    ~User_Repository();

    int get_number_of_dogs();
};
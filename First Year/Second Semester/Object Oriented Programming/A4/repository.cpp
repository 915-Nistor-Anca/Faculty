
#include "repository.h"


Repository::Repository(){

}

Dog* Repository::get_dogs() {
    return dogs.getAllElems();
}

int Repository::get_number_of_dogs(){
    return dogs.getSize();
};

void Repository::add_dog(const Dog & dog) {
    dogs.add(dog);
}

Dog Repository::get_dog_on_given_position(int pos){
    Dog* dogs = get_dogs();
    return dogs[pos];
}

void Repository:: delete_dog(int position){
    dogs.remove(position);
}

int Repository::find_dog_with_given_name(const string &name)
{
    Dog* list = dogs.getAllElems();
    for (int i = 0; i < dogs.getSize(); i++)
        if (dogs[i].get_name() == name) return i;
    return -1;
}
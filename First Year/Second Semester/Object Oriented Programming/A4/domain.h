#pragma once
#include <string>
using namespace std;

class Dog{
private:
    string breed;
    string name;
    int age;
    string photograph;
public:
    Dog();
    Dog(const string& breed, const string& name, const int& age, const string& photograph);
    Dog(const Dog& dog);

    //Returns the breed of the dog.
    string get_breed();

    //Returns the name of the dog.
    string get_name();

    //Returns the age of the dog.
    int get_age();

    //Returns the link to the photograph to the dog.
    string get_photograph();
};

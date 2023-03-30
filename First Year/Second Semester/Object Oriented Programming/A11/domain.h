#pragma once
#include <string>
//using namespace std;

class Dog {
private:
    std::string breed;
    std::string name;
    int age;
    std::string photograph;
public:
    Dog();
    Dog(const std::string& breed, const std::string& name, const int& age, const std::string& photograph);
    Dog(const Dog& dog);
    ~Dog();
    //Returns the breed of the dog.
    std::string get_breed();

    //Returns the name of the dog.
    std::string get_name() const;

    //Returns the age of the dog.
    int get_age();

    //Returns the link to the photograph to the dog.
    std::string get_photograph();

    friend std::ostream& operator << (std::ostream& output, const Dog& dog);
    friend std::istream& operator >> (std::istream& input, const Dog& dog);

    std::string to_string();
};

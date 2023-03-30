#include "ui.h"
#include "exceptions.h"
#include "html_file.h"
#include "adoption_list.h"
#include "comparator.h"

#include <iostream>
#include <vector>
#include <algorithm>
#include <stdlib.h>
#include <stdio.h>

using namespace std;

void UI::print_first_menu() {
    cout << "0. Exit application." << endl;
    cout << "1. ADMINISTRATOR" << endl;
    cout << "2. USER" << endl;
    cout << "Choose an option:" << endl;
}

void UI::print_menu_administrator() {
    cout << endl;
    cout << "0. Exit." << endl;
    cout << "1. Add a dog." << endl;
    cout << "2. Delete a dog." << endl;
    cout << "3. Update the information for a dog." << endl;
    cout << "4. See all the dogs." << endl;
}

void UI::print_menu_user() {
    cout << "0. Exit." << endl;
    cout << "1. Adopt dogs!" << endl;
    cout << "2. See specific dogs, depending on breed/age." << endl;
    cout << "3. See the adoption list." << endl;
};

void UI::print_information_for_each_dog() {
    vector<Dog> list = this->service.get_dogs();
    if (list.size() > 0) {
        cout << "The list of dogs is:" << endl;
        int i = 0;
        for (auto& d : list) {
            cout << i + 1 << ". " << "Name: " << d.get_name() << ". Age: " << d.get_age() << ". Breed: "
                << d.get_breed() << "." << endl;
            i++;
        }
    }
}



void UI::user_list_all_dogs()
{
    int ok = 1;
    while (ok) {
        vector<Dog> list = this->service.get_dogs();
        if (list.size() == 0) {
            cout << "There are no dogs!";
            break;
        }
        else
        {
            for (auto& dog : list)
            {
                cout << "Name: " << dog.get_name() << endl;
                cout << "Breed:" << dog.get_breed() << endl;
                cout << "Age:" << dog.get_age() << endl;
                //string link = string("start ").append(dog.get_photograph());
                //system(link.c_str());
                int option;
                cout << "Do you want to adopt this dog? 1-yes / 2-no / 0-exit" << endl;
                cin >> option;
                if (option == 0) { ok = 0; break; }
                else if (option == 2) cout << "The dog is not adopted." << endl << endl;
                else if (option == 1)
                {
                    this->user_service.add_dog(dog);
                }

            }
        }
    }

}

void UI::user_list_all_dogs_filtered() {

    int i = 0;
    string breed;
    int age;
    cout << "Breed: " << endl;
    cin.get();
    getline(cin, breed);
    cout << "Age: " << endl;
    cin >> age;
    int ok = 1;
    while (ok) {
        vector<Dog> list = this->service.get_dogs();
        vector<Dog> filtered_list;
        copy_if(list.begin(), list.end(), back_inserter(filtered_list), [age, breed](Dog& dog) {return dog.get_age() < age && dog.get_breed() == breed; });

        if (filtered_list.size() == 0) {
            cout << "There are no dogs!\n";
            break;
        }
        else
        {
            for (auto& dog : filtered_list)
            {
                cout << "Name: " << dog.get_name() << endl;
                cout << "Breed:" << dog.get_breed() << endl;
                cout << "Age:" << dog.get_age() << endl;
                //string link = string("start ").append(dog.get_photograph());
                //system(link.c_str());
                int option;
                cout << "Do you want to adopt this dog? 1-yes / 2-no / 0-exit" << endl;
                cin >> option;
                if (option == 0) { ok = 0; break; }
                else if (option == 2) cout << "The dog is not adopted." << endl << endl;
                else if (option == 1)
                {
                    this->user_service.add_dog(dog);
                }

            }
        }
    }

}

void UI::see_adoption_list() {

    vector<Dog> list_of_adopted_dogs = this->user_service.get_all_dogs();
    if (list_of_adopted_dogs.empty()) cout << "There are no dogs in the adoption list." << endl << endl;
    else
    {
        for (auto& dog : list_of_adopted_dogs)
        {
            cout << "Name: " << dog.get_name() << endl;
            cout << "Breed: " << dog.get_breed() << endl;
            cout << "Age: " << dog.get_age() << endl;
            cout << endl;
        }
    }
    string command = "start ";
    string file_name = this->user_service.get_file_name();
    command += file_name;
    system(command.c_str());
}

void UI::run() {
    this->service.read_file();
    while (true) {
        print_first_menu();
        int first_option;
        cin >> first_option;
        if (first_option == 0) break;
        else if (first_option == 1) {

            while (true) {
                this->service.write_to_file();
                print_menu_administrator();
                int second_option;
                cout << "Option:" << endl;
                cin >> second_option;
                if (second_option == 0) break;
                else if (second_option == 1) { //add
                    string breed, name, photograph;
                    int age;
                    cout << "Dog's breed:" << endl;
                    cin.get();
                    getline(cin, breed);
                    cout << "Dog's name:" << endl;
                    //cin.get();
                    getline(cin, name);
                    cout << "Dog's age:" << endl;
                    cin >> age;
                    cout << "Link to the dog's photograph:" << endl;
                    cin.get();
                    getline(cin, photograph);

                    try {
                        DogValidator d;
                        if (d.validate_age(age) == false)
                            throw InvalidAge();
                        if (d.validate_name(name) == false)
                            throw InvalidName();
                        int result = this->service.add_dog_service(breed, name, age, photograph);
                        if (result == 1) cout << "Dog added!" << endl;
                        else cout << "This name is already taken by another dog! ";
                        print_information_for_each_dog();
                    }
                    catch (DogAlreadyExists const& i) {
                        cout << i.what() << endl;
                    }
                    catch (InvalidAge const& i) {
                        cout << i.what() << endl;
                    }
                    catch (InvalidName const& i) {
                        cout << i.what() << endl;
                    }
                }
                else if (second_option == 2) //delete
                {
                    string name;
                    cout << "The name of the dog which has to be deleted: " << endl;
                    cin.get();
                    getline(cin, name);
                    int pos = this->service.search_dog_by_name(name);
                    if (pos == -1) cout << "There is no dog with such name." << endl;
                    else
                    {
                        this->service.delete_dog_service(pos);
                        cout << "Dog deleted." << endl;
                        print_information_for_each_dog();
                    }
                }
                else if (second_option == 3) //update
                {
                    string name;
                    cout << "The name of the dog which has to be updated: " << endl;
                    cin.get();
                    getline(cin, name);
                    int pos = this->service.search_dog_by_name(name);
                    if (pos == -1) cout << "There is no dog with such name." << endl;
                    else
                    {
                        this->service.delete_dog_service(pos);
                        string new_name, new_breed, new_photograph;
                        int new_age;
                        cout << "The new name:" << endl;
                        //cin.get();
                        getline(cin, new_name);
                        cout << "The new breed:" << endl;
                        cin.get();
                        getline(cin, new_breed);
                        cout << "The new age:" << endl;
                        cin >> new_age;
                        cout << "The new link to the photograph:" << endl;
                        //cin.get();
                        getline(cin, new_photograph);
                        int result = this->service.add_dog_service(new_breed, new_name, new_age, new_photograph);
                        if (result == 1) cout << "Dog added!" << endl;
                        else cout << "This name is already taken by another dog! ";
                        print_information_for_each_dog();

                    }
                }
                else if (second_option == 4) print_information_for_each_dog();
            }
        }
        else
        {
            while (true) {
                print_menu_user();
                int option = -1;
                cin >> option;
                if (option == 0) break;
                if (option == 1) user_list_all_dogs();
                if (option == 2) user_list_all_dogs_filtered();
                if (option == 3) see_adoption_list();
            }
        }
    }
    this->service.write_to_file();
}
UI::UI(Service& service, User_Service& user_service) : service(service), user_service(user_service) {

}


UI::~UI()
{
}

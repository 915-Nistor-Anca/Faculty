#pragma once
#include "service.h"
#include "user_service.h"
class UI
{
private:
    Service& service;
    User_Service& user_service;
public:
    UI(Service& service, User_Service& user_service);
    ~UI();

    //Prints the first menu.
    void print_first_menu();

    //Prints the menu with the options which are used by the administrator.
    void print_menu_administrator();

    //Runs the main function.
    void run();

    //Prints each dog from the list of dogs, along with its data.
    void print_information_for_each_dog();

    //Adds some dogs at the start of the program.
    void add_new_dogs();

    void user_list_all_dogs();

    void print_menu_user();

    void user_list_all_dogs_filtered();

    void see_adoption_list();
};
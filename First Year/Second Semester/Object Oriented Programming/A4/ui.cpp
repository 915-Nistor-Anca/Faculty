#include "ui.h"
#include <iostream>
using namespace std;

void UI::print_first_menu() {
    cout << "0. Exit application." << endl;
    cout << "1. ADMINISTRATOR"<< endl;
    cout << "2. USER" << endl;
    cout << "Choose an option:" << endl;
}

void UI::print_menu_administrator() {
    cout << endl;
    cout << "0. Exit." << endl;
    cout<< "1. Add a dog." << endl;
    cout << "2. Delete a dog." << endl;
    cout << "3. Update the information for a dog." << endl;
    cout << "4. See all the dogs." << endl;
}

void UI::print_menu_user(){
    cout << "0. Exit." << endl;
    cout << "1. Adopt dogs!" << endl;
    cout << "2. See specific dogs, depending on breed/age."<<endl;
    cout << "3. See the adoption list."<<endl;
};

void UI::print_information_for_each_dog(){
    int length = this->service.get_number_of_dogs();
    if (length > 0) {
        cout << "The list of dogs is:" << endl;
        for (int i = 0; i < length; i++) {
            Dog d = this->service.get_dog_on_given_position(i);
            cout << i + 1 << ". " << "Name: " << d.get_name() << ". Age: " << d.get_age() << ". Breed: "
                 << d.get_breed() << "." << endl;
        }
    }
    else cout << "There are no dogs." << endl;
}

void UI::add_new_dogs(){
    this->service.add_dog_service("Golden Retriever", "Bruno", 3, "https://www.megapet.ro/continut/upload//Golden-Retriever.jpg");
    this->service.add_dog_service("Bulldog", "Terry", 9, "https://rasedecaini.ro/wp-content/uploads/2019/05/Bulldog-Englez.jpg");
    this->service.add_dog_service("Labrador", "Lucky", 5, "https://www.taramulanimalelor.com/wp-content/uploads/2020/10/Labrador-caracteristici-rasa-caine.jpg");
    this->service.add_dog_service("Golden Retriever", "Max", 10, "https://www.animalepierdute.ro/wp-content/uploads/2019/08/golden-retriver-caine-de-rasa.jpg");
    this->service.add_dog_service("Bulldog", "Rex", 2, "https://cdn.pixabay.com/photo/2020/07/20/06/42/english-bulldog-5422018__340.jpg");
    this->service.add_dog_service("Bichon", "Suzy", 3, "https://animax.ro/wp/wp-content/uploads/2015/03/painting-1893461_640.jpg");
    this->service.add_dog_service("Pomeranian", "Ginger", 5, "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Pomeranian_orange-sable_Coco.jpg/1200px-Pomeranian_orange-sable_Coco.jpg");
    this->service.add_dog_service("Labrador", "Sparky", 7, "https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F34%2F2022%2F03%2F22%2Fhappy-labrador-retriever-getty-0322-2000.jpg");
    this->service.add_dog_service("Husky", "Caesar", 2, "https://www.radiooltenia.ro/wp-content/uploads/2021/08/photo-1617895153857-82fe79adfcd4.jpg");
    this->service.add_dog_service("Bichon", "Lucy", 5, "https://rasedecaini.ro/wp-content/uploads/2019/05/rasa-bichon-maltez-730x438.jpg");
}


void UI::user_list_all_dogs()
{

    int i = 0;
    while(true)
    {
        if (this->service.get_number_of_dogs() != 0)
        {
            string option;
            cout << this->service.get_dog_on_given_position(i).get_name() << ' ';
            cout << this->service.get_dog_on_given_position(i).get_breed() << ' ';
            cout << this->service.get_dog_on_given_position(i).get_age() << ' ';
            cout << "Do you want to adopt this dog? (yes / no / exit)" << endl;
            string link = string("start ").append(this->service.get_dog_on_given_position(i).get_photograph());
            system(link.c_str());
            cin >> option;
            if (option == "exit")break;
            if (option == "no") {
                i++;
                if (i == this->service.get_number_of_dogs()) i = 0;
            }
            if (option == "yes"){
                Dog dog = this->service.get_dog_on_given_position(i);
                this->user_service.add_dog(dog);
            }
        }
        else
        {
            cout << "There are no more dogs which can be adopted!" << endl;
            break;
        }
        }
    }

void UI::user_list_all_dogs_filtered(){

    int i = 0;
    string breed;
    int age;
    cout<<"Breed: "<< endl;
    cin.get();
    getline(cin, breed);
    cout <<"Age: "<< endl;
    cin>>age;
    int k = 0;
    Dog* list = this->service.get_dogs();
    int n = this->service.get_number_of_dogs();
    DynamicVector<Dog> list2;
    for (int i = 0; i < n; i++)
        if ((list[i].get_breed() == breed or breed == "") && list[i].get_age() < age) {
            k++;
            list2.add(list[i]);
        }

    i = 0;
    while(k != 0)
    {
        cout << "Name: "<<list2[i].get_name()<<endl;
        cout <<"Breed: "<<list2[i].get_breed()<<endl;
        cout<<"Age: "<<list2[i].get_age()<<endl;
        string link = string("start ").append(list2.operator[](i).get_photograph());
        system(link.c_str());
        int option;
        cout << "Do you want to adopt this dog? 1-Yes, 2-No, 0-Exit." << endl;
        cin >> option;
        if (option == 0) break;
        else if (option == 2) {
            if (i == k - 1) i = 0;
            else i++;
        }
        else if (option == 1)
        {
            k--;
            int pos = this->service.search_dog_by_name(list2[i].get_name());
            this->user_service.add_dog(list2[i]);
            this->service.delete_dog_service(pos);
            list2.remove(i);
        }
    }
    if (k == 0) cout << "All the dogs of this breed which are younger than the given age have been adopted!"<<endl;
}

void UI::see_adoption_list(){
    Dog* list_of_adopted_dogs = this->user_service.get_all_dogs();
    int number_of_dogs = this->user_service.get_number_of_dogs();
    if (number_of_dogs == 0) cout << "There are no dogs in the adoption list." << endl<<endl;
    for (int i = 0; i < number_of_dogs; i++)
    {
        cout << "Name: "<<list_of_adopted_dogs[i].get_name()<<endl;
        cout <<"Breed: "<<list_of_adopted_dogs[i].get_breed()<<endl;
        cout<<"Age: "<<list_of_adopted_dogs[i].get_age()<<endl;
        cout << endl;
    }

}

void UI::run() {
    add_new_dogs();
    while (true) {
        print_first_menu();
        int first_option;
        cin >> first_option;
        if (first_option == 0) break;
        else if (first_option == 1) {
            while (true) {
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

                    int result = this->service.add_dog_service(breed, name, age, photograph);
                    if (result == 1) cout << "Dog added!" << endl;
                    else cout << "This name is already taken by another dog! ";
                    print_information_for_each_dog();
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
                        cout << "The new name:"<<endl;
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
}
UI::UI(Service &service, User_Service &user_service) : service(service), user_service(user_service){

}

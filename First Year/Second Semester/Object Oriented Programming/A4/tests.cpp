#include "tests.h"
#include <assert.h>

void test_domain(){
    Dog d("abc", "def", 4, "x");
    assert(d.get_age() == 4);
    assert(d.get_name() == "def");
    assert(d.get_breed() == "abc");
    assert(d.get_photograph() == "x");
}

void test_dynamic_vector(){
    DynamicVector<Dog> list;
    Dog d("abc", "def", 4, "x");
    list.add(d);
    assert(list.getSize() == 1);
    list.add(d); list.add(d);list.add(d); list.add(d); list.add(d);
    list.add(d); list.add(d); list.add(d); list.add(d); list.add(d);
    list.add(d);
    list.add(d);
    Dog d2("jk", "def", 4, "x");
    list.add(d2);
    assert(list[0].get_breed() == "abc");
    list.remove(4);
    assert(list.getSize() == 13);
    DynamicVector<Dog> list2;
    list2= list;
    assert(list2.operator[](0).get_breed() == "abc");
}

void test_repositories(){
    Dog d("a","b", 4, "c");
    DynamicVector<Dog> list;
    Repository repo;
    repo.add_dog(d);
    assert(repo.get_dog_on_given_position(0).get_breed() =="a");
    repo.delete_dog(0);
    assert(repo.get_number_of_dogs() == 0);
    repo.add_dog(d);
    int x = repo.find_dog_with_given_name("b");
    assert(x == 0);
    x = repo.find_dog_with_given_name("abc");
    assert(x == -1);
}

void test_service(){
    DynamicVector<Dog> list;
    Repository repo;
    Service serv(repo);
    serv.add_dog_service("a", "b", 4, "c");
    int x = serv.search_dog_by_name("z");
    assert(x == -1);
    serv.add_dog_service("abc", "abb", 4, "c");
    x = serv.search_dog_by_name("abb");
    assert(x == 1);
    x = serv.add_dog_service("a", "b", 4, "c");
    assert(x == 0);
    x = serv.get_number_of_dogs();
    assert(x == 2);
    Dog* l = serv.get_dogs();
    assert(l[0].get_breed() == "a");
    Dog d = serv.get_dog_on_given_position(1);
    assert(d.get_age() == 4);
    serv.delete_dog_service(0);
    assert(serv.get_number_of_dogs() == 1);
}

void test_user_repo_service(){
    User_Repository user_repo;
    Repository repo;
    User_Service user_service(repo, user_repo);
    Dog d("a","b", 4, "c");
    user_repo.add_dog(d);
    Dog* list = user_repo.get_all_dogs();
    assert(list[0].get_breed() == "a");
    int x = user_repo.get_number_of_dogs();
    assert(x == 1);
    user_service.add_dog(d);
    int n = user_service.get_number_of_dogs();
    assert(n == 2);
    user_service.add_dog(d);
    Dog* l = user_service.get_all_dogs();
    assert(l[0].get_name() == "b");

}

void test_all(){
 test_domain();
 test_dynamic_vector();
 test_repositories();
 test_service();
 test_user_repo_service();
}
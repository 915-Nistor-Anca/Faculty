#include <iostream>
#include <cstring>
using namespace std;
#include "ui.h"
#include "tests.h"
#include "crtdbg.h"

int main()
{
    test_all();
    Repository repo;
    Service serv(repo);

    User_Repository user_repo;
    User_Service user_service(repo, user_repo);
    UI ui(serv, user_service);
    ui.run();
    _CrtDumpMemoryLeaks();


}
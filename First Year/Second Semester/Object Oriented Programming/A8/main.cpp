#include <iostream>
#include <cstring>
using namespace std;
#include "ui.h"
#include "crtdbg.h"
int main()
{
    string file_name = "data.in";
    Repository repo(file_name);
    Service serv(repo);

    User_Repository user_repo;
    User_Service user_service(repo, user_repo);
    UI ui(serv, user_service);
    ui.run();
    _CrtDumpMemoryLeaks();


}
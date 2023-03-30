
#include <QtWidgets/QApplication>

#include "adoption_list.h"
#include "service.h"
#include "html_file.h"
#include "csv_file.h"
#include "repository.h"
#include "ui.h"
#include "gui.h"

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);

    std::string file_name = "data.in";
    std::string html_file_name = "html_file_data.html";

    HtmlFile html(html_file_name);
    Repository repo(file_name);
    Service serv(repo);

    AdoptionList* list;
    list = &html;

    User_Repository user_repo;
    User_Service user_service(repo, user_repo, list);
    //UI ui(serv, user_service);
    //ui.run();
     
    serv.read_file();
    GUI gui{ serv, user_service, repo };
    gui.show();

    return a.exec();
}

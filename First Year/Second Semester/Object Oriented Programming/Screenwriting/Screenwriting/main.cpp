#include "Screenwriting.h"
#include <QtWidgets/QApplication>
#include "service.h"

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    
    repository repo;
    service serv(repo);

    for (writer w : serv.getWriters()) {
        auto* window = new Screenwriting{ serv, w.getName() };
        window->show();
    }

    return a.exec();
}

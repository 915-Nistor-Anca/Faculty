#include "QuestionsAnswersSite.h"
#include "UserWindow.h"
#include <QtWidgets/QApplication>
#include "service.h"

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    
    repository repo;
    service serv(repo);
    for (user u : serv.getUsers()) {
        auto* w = new UserWindow{u.getName(), serv};
        w->show();
    }
    auto* w = new QuestionsAnswersSite{ serv };
    w->show();
    return a.exec();
}

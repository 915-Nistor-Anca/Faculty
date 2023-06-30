#include "PracticalExam.h"
#include <QtWidgets/QApplication>
#include "couriercompany.h"

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    
    repository repo;
    service serv(repo);

    for (courier c: serv.getCouriers()) {
        auto* window = new PracticalExam{ serv,  c.getName()};
        window->show();
    }
    auto* w = new couriercompany{ serv };
    w->show();
    return a.exec();
}

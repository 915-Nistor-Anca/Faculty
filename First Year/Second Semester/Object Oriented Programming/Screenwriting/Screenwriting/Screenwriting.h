#pragma once
#include "service.h"

#include <QtWidgets/QMainWindow>
#include "ui_Screenwriting.h"

class Screenwriting : public QMainWindow
{
    Q_OBJECT

public:
    Screenwriting(service& s, string username, QWidget *parent = nullptr);
    ~Screenwriting();
    void showIdeas();
    void addIdea();
    void connectSignalsAndSlots();
    void acceptIdea();
    void checkIfSenior();
    void checkIfCanDevelop();
    void developIdea();
    

private:
    Ui::ScreenwritingClass ui;
    service& s;
    string username;
};

#pragma once

#include <QtWidgets/QMainWindow>
#include "ui_PracticalExam.h"
#include "service.h"
#include "observer.h"

class PracticalExam : public QMainWindow, public observer
{
    Q_OBJECT

public:
    PracticalExam(service& s, string username, QWidget *parent = nullptr);
    ~PracticalExam();
    void connectSignalsAndSlots();
    void populatePackages();
    void deliverPackage();
    void populateStreets();
    void update() override;

private:
    Ui::PracticalExamClass ui;
    service& s;
    string username;
};

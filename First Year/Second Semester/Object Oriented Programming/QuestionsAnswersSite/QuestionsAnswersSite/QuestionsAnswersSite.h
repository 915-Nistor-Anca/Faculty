#pragma once

#include <QtWidgets/QMainWindow>
#include "ui_QuestionsAnswersSite.h"
#include "service.h"

class QuestionsAnswersSite : public QMainWindow
{
    Q_OBJECT

public:
    QuestionsAnswersSite(service& s, QWidget *parent = nullptr);
    ~QuestionsAnswersSite();
    void findBestMatch();
    void connectSignalsAndSlots();
private:
    service& s;
    Ui::QuestionsAnswersSiteClass ui;
};

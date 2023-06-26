#include "Screenwriting.h"
#include <QMessageBox>
#include <QTextEdit>

Screenwriting::Screenwriting(service& s, string username, QWidget* parent)
    : QMainWindow(parent), s(s), username(username)
{
    ui.setupUi(this);
    this->setWindowTitle(QString::fromStdString(username));
    showIdeas();
    connectSignalsAndSlots();
    checkIfSenior();
    checkIfCanDevelop();
}

Screenwriting::~Screenwriting()
{}

void Screenwriting::showIdeas()
{
    this->ui.listWidget->clear();
    vector<idea> ideas = s.getIdeas();
    sort(ideas.begin(), ideas.end(), [](idea i1, idea i2) {return i1.getAct() < i2.getAct(); });
    for (idea i : ideas) {
        this->ui.listWidget->addItem(QString::fromStdString(i.getDescription() + '|' + i.getStatus() + '|' + i.getCreator() + '|' + to_string(i.getAct())));
    }
}

void Screenwriting::addIdea()
{
    string description = this->ui.lineEdit->text().toStdString();
    int act = stoi(this->ui.lineEdit_2->text().toStdString());
    for (idea i : s.getIdeas()) if (i.getDescription() == description) {
        QMessageBox::critical(this, "Error", "Description already exists!");
        break;
    }
    else if (description == "") QMessageBox::critical(this, "Error", "Text cannot be empty!");
    else {
        if (act != 1 && act != 2 && act != 3) {
            QMessageBox::critical(this, "Error", "Act must be 1, 2 or 3!");
            break;
        }
        else {
            idea i(description, "proposed", username, act);
            s.addIdea(i);
        }
    }
    showIdeas();
}

void Screenwriting::connectSignalsAndSlots()
{
    QObject::connect(this->ui.pushButton, &QPushButton::clicked, this, &Screenwriting::addIdea);
    QObject::connect(this->ui.pushButton_2, &QPushButton::clicked, this, &Screenwriting::acceptIdea);
    QObject::connect(this->ui.pushButton_3, &QPushButton::clicked, this, &Screenwriting::developIdea);
}

void Screenwriting::acceptIdea()
{
    this->ui.pushButton_2->setEnabled(true);
    int ok = 1;
    for (writer w : s.getWriters()) {
        if (w.getName() == username && w.getExpertise() != "senior")
        {
            this->ui.pushButton_2->setEnabled(false);
            ok = 0;
            break;
        }
    }
    if (ok == 1) {
        string text = this->ui.listWidget->selectedItems().at(0)->text().toStdString();
        string description = text.substr(0, text.find("|"));
        s.changeIdeaStatus(description, "accepted");
    }
    showIdeas();
}

void Screenwriting::checkIfSenior()
{
    for (writer w : s.getWriters()) {
        if (w.getName() == username && w.getExpertise() != "senior")
        {
            this->ui.pushButton_2->setEnabled(false);
        }
    }
}

void Screenwriting::checkIfCanDevelop()
{
    int k = 0;
    for (idea i : s.getIdeas()) {
        if (i.getCreator() == username && i.getStatus() == "accepted") k++;
    }
    if (k == 0) this->ui.pushButton_3->setEnabled(false);
}

void Screenwriting::developIdea()
{
    
    
    auto* window = new Screenwriting{ s, username };
    QWidget* centralWidget = new QWidget(window);
    window->setCentralWidget(centralWidget);
    QVBoxLayout* layout = new QVBoxLayout(centralWidget);

    for (idea i: s.getIdeas())
        if (i.getCreator() == username && i.getStatus() == "accepted") {

            QTextEdit* textEdit = new QTextEdit;
            textEdit->setPlainText(QString::fromStdString(i.getDescription()));
            layout->addWidget(textEdit);

            QPushButton* button = new QPushButton("Save");

            layout->addWidget(button);


        }
    QPushButton* button2 = new QPushButton("Back");
    layout->addWidget(button2);
    QObject::connect(button2, &QPushButton::clicked, window, &QMainWindow::close);
    window->show();
}


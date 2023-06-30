#include "PracticalExam.h"
#include <QMessageBox>
#include <QTextEdit>

PracticalExam::PracticalExam(service& s, string username, QWidget *parent)
    : QMainWindow(parent), s(s), username(username)
{
    ui.setupUi(this);
    this->setWindowTitle(QString::fromStdString(username));
    s.addObserver(this);
    string zone;
    for (courier c : s.getCouriers())
    {
        if (c.getName() == username) zone = c.getZone();
    }
    this->ui.zonewidget->addItem(QString::fromStdString(zone));
    connectSignalsAndSlots();
    populatePackages();
    populateStreets();
}

PracticalExam::~PracticalExam()
{}

void PracticalExam::connectSignalsAndSlots()
{
    QObject::connect(this->ui.pushButton, &QPushButton::clicked, this, &PracticalExam::deliverPackage);
}

void PracticalExam::populatePackages()
{
    this->ui.listWidget->clear();
    string streets, zone;
    for (courier c : s.getCouriers())
    {
        if (c.getName() == username) {
            streets = c.getStreets();
            zone = c.getZone();
        }
    }
    vector<int> street_nb;
    stringstream ss(streets);
    string number;
    while (getline(ss, number, ',')) {
        street_nb.push_back(std::stoi(number));
    }
    for (package p : s.getPackages()) {
        if (p.getDeliveryStatus() == 0) {
            string address = p.getAddress();
            stringstream ss2(address);
            string x;
            std::getline(ss2, x, ',');
            int street = stoi(x);
            auto it = std::find(street_nb.begin(), street_nb.end(), street);
            if (it != street_nb.end())
                this->ui.listWidget->addItem(QString::fromStdString(p.getRecipient() + '|' + p.getAddress() + '|' + p.getLocation() + '|' + to_string(p.getDeliveryStatus())));

            else {
                string location = p.getLocation();
                string field;
                int c1, c2;
                vector<string> fields;
                stringstream ss3(location);
                while (getline(ss3, field, ',')) {
                    fields.push_back(field);
                }
                c1 = stoi(fields[0]);
                c2 = stoi(fields[1]);

                int x1, x2, x3;
                string field2;
                vector<string> fields2;
                stringstream ss4(zone);
                while (getline(ss4, field2, ',')) {
                    fields2.push_back(field2);
                }
                x1 = stoi(fields2[0]);
                x2 = stoi(fields2[1]);
                x3 = stoi(fields2[2]);

                double distance = std::sqrt(std::pow(c1 - x1, 2) + std::pow(c2 - x2, 2));
                if (distance <= x3)this->ui.listWidget->addItem(QString::fromStdString(p.getRecipient() + '|' + p.getAddress() + '|' + p.getLocation() + '|' + to_string(p.getDeliveryStatus())));
            }
        }
    }
}

void PracticalExam::deliverPackage()
{
    string text = this->ui.listWidget->selectedItems().at(0)->text().toStdString();
    std::string recipient;

    std::stringstream ss(text);
    std::getline(ss, recipient, '|');
    s.deliverPackage(recipient);
    populatePackages();
    
}

void PracticalExam::populateStreets()
{
    std::vector<int> streets;
    for (package p : s.getPackages()) {
        std::string address = p.getAddress();
        std::stringstream ss(address);
        std::string number;
        while (std::getline(ss, number, ',')) {
            int street = std::stoi(number);
            if (std::find(streets.begin(), streets.end(), street) == streets.end()) {
                streets.push_back(street);
            }
        }
    }
    for (int street : streets)
        this->ui.comboBox->addItem(QString::fromStdString(to_string(street)));
}

void PracticalExam::update()
{
    populatePackages();
}


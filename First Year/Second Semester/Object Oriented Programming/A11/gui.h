#pragma once

#include <QWidget>
#include "service.h"
#include <QLabel>
#include <QPushButton>
#include "user_service.h"
#include <QListWidget>
#include <QLineEdit>
#include <QRadioButton>
class DogListModel : public QAbstractListModel {
private:
    Repository& repository;
public:
    explicit DogListModel(Repository& repo) : repository{ repo } {};

    int rowCount(const QModelIndex& parent = QModelIndex()) const override;
    QVariant data(const QModelIndex& index, int role = Qt::DisplayRole) const override;
};

class GUI : public QWidget {
private:
    Service& service;
    User_Service& userService;
    Repository& repository;
    void initGUI();
    QLabel* titleWidget;
    QPushButton* adminButton;
    QPushButton* userButton;
    void showAdmin();
    void showUser();
    void connectSignalsAndSlots();
public:
    explicit GUI(Service& serv, User_Service& userserv, Repository& repository);
    ~GUI() override;
};

class AdminGUI : public QWidget {
private:
    Service& service;
    Repository& repository;
    void initAdminGUI();
    QLabel* titleWidget;
    QListWidget* dogsListWidget;
    QLineEdit* nameLineEdit, * breedLineEdit, * ageLineEdit, * linkLineEdit;
    QPushButton* addButton, * deleteButton, * updateButton, * chartButton;
    DogListModel* listModel;

    void populateList();
    void connectSignalsAndSlots();
    int getSelectedIndex() const;
    void addDog();
    void deleteDog();
    void updateDog();

    QWidget* chartWindow;
public:
    explicit AdminGUI(QWidget* parent, Service& serv, Repository& repo);
    ~AdminGUI() override;
};

class UserGUI : public QWidget {
private:
    Service& service;
    User_Service& userService;
    void initUserGUI();
    QLabel* titleWidget;
    QListWidget* dogsListWidget, * adoptionListWidget;
    QLineEdit* nameLineEdit, * breedLineEdit, * ageLineEdit, * linkLineEdit, * breedFilterLineEdit, * ageFilterLineEdit;
    QPushButton* addButton, * filterButton, * openListButton;
    QRadioButton* csvButton, * htmlButton;
    bool repoTypeSelected;
    bool filtered;
    void populateDogList();
    void populateAdoptionList();
    void connectSignalsAndSlots();
    int getSelectedIndex() const;
    void addDog();
    void filterDogs();
    void save_html();
public:
    explicit UserGUI(QWidget* parent, Service& serv, User_Service& userserv);
    ~UserGUI() override;
};

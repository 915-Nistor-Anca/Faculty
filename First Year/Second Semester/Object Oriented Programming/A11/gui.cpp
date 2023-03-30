#include <QVBoxLayout>
#include <QFormLayout>
#include <QErrorMessage>
#include <QMessageBox>
#include <QtCharts/QChartView>
#include <QtCharts/QBarSeries>
#include <QtCharts/QBarSet>
#include <QtCharts/QBarCategoryAxis>
#include <QtCharts/QValueAxis>
#include "GUI.h"
#include "html_file.h"
#include "csv_file.h"

GUI::GUI(Service& serv, User_Service& userserv, Repository& repository) : service{ serv }, userService{ userserv }, repository{ repository }{
    this->titleWidget = new QLabel(this);
    this->adminButton = new QPushButton(this);
    this->userButton = new QPushButton(this);
    this->initGUI();
    this->connectSignalsAndSlots();
}

void GUI::initGUI() {
    auto* layout = new QVBoxLayout(this);
    QFont titleFont = this->titleWidget->font();
    this->titleWidget->setText("<p style='text-align:center'><font color=#4D2D52>Welcome to the Dog Shelter App! <br> Select your mode!</font></p>");
    titleFont.setItalic(true);
    titleFont.setPointSize(10);
    titleFont.setStyleHint(QFont::System);
    //titleFont.setWeight(63);
    this->titleWidget->setFont(titleFont);
    layout->addWidget(this->titleWidget);
    this->adminButton->setText("Admin mode");
    layout->addWidget(this->adminButton);
    this->userButton->setText("User mode");
    layout->addWidget(this->userButton);
    this->setLayout(layout);
    this->setStyleSheet("background-color:#D9EBF1");
}

GUI::~GUI() = default;

void GUI::connectSignalsAndSlots() {
    QObject::connect(this->adminButton, &QPushButton::clicked, this, &GUI::showAdmin);
    QObject::connect(this->userButton, &QPushButton::clicked, this, &GUI::showUser);
}

void GUI::showAdmin() {
    auto* admin = new AdminGUI(this, this->service, this->repository);
    admin->show();
}

AdminGUI::AdminGUI(QWidget * parent, Service & serv, Repository & repo) : service{ serv },repository{ repo }{
    this->titleWidget = new QLabel(this);
    this->dogsListWidget = new QListWidget{};
    this->nameLineEdit = new QLineEdit{};
    this->breedLineEdit = new QLineEdit{};
    this->ageLineEdit = new QLineEdit{};
    this->linkLineEdit = new QLineEdit{};
    this->addButton = new QPushButton("Add");
    this->deleteButton = new QPushButton("Delete");
    this->updateButton = new QPushButton("Update");
    //setParent(parent);
    setWindowFlag(Qt::Window);
    this->initAdminGUI();
    this->populateList();
    this->connectSignalsAndSlots();

    this->listModel = new DogListModel{ this->repository };

}

void AdminGUI::initAdminGUI() {
    auto* layout = new QVBoxLayout(this);
    QFont titleFont = this->titleWidget->font();
    this->titleWidget->setText("<p style='text-align:center'><font color=#4D2D52>ADMIN MODE</font></p>");
    titleFont.setItalic(true);
    titleFont.setPointSize(10);
    titleFont.setStyleHint(QFont::System);
    //titleFont.setWeight(63);
    this->titleWidget->setFont(titleFont);
    layout->addWidget(this->titleWidget);

    layout->addWidget(this->dogsListWidget);

    auto* dogDetailsLayout = new QFormLayout{};
    dogDetailsLayout->addRow("Name", this->nameLineEdit);
    dogDetailsLayout->addRow("Breed", this->breedLineEdit);
    dogDetailsLayout->addRow("Age", this->ageLineEdit);
    dogDetailsLayout->addRow("Link", this->linkLineEdit);
    layout->addLayout(dogDetailsLayout);

    auto* buttonsLayout = new QGridLayout{};
    buttonsLayout->addWidget(this->addButton, 0, 0);
    buttonsLayout->addWidget(this->deleteButton, 0, 1);
    buttonsLayout->addWidget(this->updateButton, 1, 0);
    layout->addLayout(buttonsLayout);
}

void AdminGUI::populateList() {
    this->dogsListWidget->clear();
    std::vector<Dog> allDogs = this->service.get_dogs();
    for (Dog& dog : allDogs)
        this->dogsListWidget->addItem(QString::fromStdString(dog.get_name()));
}

void AdminGUI::connectSignalsAndSlots() {
    QObject::connect(this->dogsListWidget, &QListWidget::itemSelectionChanged, [this]() {
        int selectedIndex = this->getSelectedIndex();
        if (selectedIndex < 0)
            return;
        Dog dog = this->service.get_dogs()[selectedIndex];
        this->nameLineEdit->setText(QString::fromStdString(dog.get_name()));
        this->breedLineEdit->setText(QString::fromStdString(dog.get_breed()));
        this->ageLineEdit->setText(QString::fromStdString(std::to_string(dog.get_age())));
        this->linkLineEdit->setText(QString::fromStdString(dog.get_photograph()));
        });

    QObject::connect(this->addButton, &QPushButton::clicked, this, &AdminGUI::addDog);
    QObject::connect(this->deleteButton, &QPushButton::clicked, this, &AdminGUI::deleteDog);
    QObject::connect(this->updateButton, &QPushButton::clicked, this, &AdminGUI::updateDog);
    //QObject::connect(this->chartButton, &QPushButton::clicked, this, &AdminGUI::displayChart);
}

void AdminGUI::addDog() {
    std::string breed = this->breedLineEdit->text().toStdString();
    std::string name = this->nameLineEdit->text().toStdString();
    std::string age_s = this->ageLineEdit->text().toStdString();
    std::string link = this->linkLineEdit->text().toStdString();
    int age;
    age = stoi(age_s);
    this->service.add_dog_service(breed, name, age, link);
    this->populateList();
    
}

void AdminGUI::deleteDog() {
    
    std::string name = this->nameLineEdit->text().toStdString();
    int pos = 0, k = 0;
    for (auto& dog : this->service.get_dogs()) {
        if (dog.get_name() == name) pos = k;
        k++;
    }
    this->service.delete_dog_service(pos);
    this->populateList();
}

void AdminGUI::updateDog() {
    int index = this->getSelectedIndex();
        if (index < 0) {
            auto* error = new QMessageBox();
            error->setIcon(QMessageBox::Critical);
            error->setText("No dog selected!");
            error->setWindowTitle("Selection error!");
            error->exec();
        }
        else { //TODO
            this->service.delete_dog_service(index);
            std::string old_name = this->service.get_dogs()[index].get_name();
            std::string new_name = this->nameLineEdit->text().toStdString();
            std::string new_breed = this->breedLineEdit->text().toStdString();
            std::string age_s = this->ageLineEdit->text().toStdString();
            int age;
            std::string new_link = this->linkLineEdit->text().toStdString();
            age = stoi(age_s);
            this->service.add_dog_service(new_breed, new_name, age, new_link);
            this->populateList();
        }
    
}


int AdminGUI::getSelectedIndex() const {
    QModelIndexList selectedIndexes = this->dogsListWidget->selectionModel()->selectedIndexes();
    if (selectedIndexes.empty()) {
        this->nameLineEdit->clear();
        this->breedLineEdit->clear();
        this->ageLineEdit->clear();
        this->linkLineEdit->clear();
        return -1;
    }
    int selectedIndex = selectedIndexes.at(0).row();
    return selectedIndex;
}

AdminGUI::~AdminGUI() = default;

void GUI::showUser() {
    auto* user = new UserGUI(this, this->service, this->userService);
    user->show();
}


UserGUI::UserGUI(QWidget * parent, Service & serv, User_Service & userserv) : service{ serv }, userService{ userserv }{
    this->titleWidget = new QLabel(this);
    this->dogsListWidget = new QListWidget{};
    this->adoptionListWidget = new QListWidget{};
    this->nameLineEdit = new QLineEdit{};
    this->breedLineEdit = new QLineEdit{};
    this->ageLineEdit = new QLineEdit{};
    this->linkLineEdit = new QLineEdit{};
    this->breedFilterLineEdit = new QLineEdit{};
    this->ageFilterLineEdit = new QLineEdit{};
    this->addButton = new QPushButton("Add to the adoption list");
    this->filterButton = new QPushButton("Filter");
    this->openListButton = new QPushButton("Open file");
    this->csvButton = new QRadioButton("CSV");
    this->htmlButton = new QRadioButton("HTML");
    this->repoTypeSelected = false;
    this->filtered = false;
    setParent(parent);
    setWindowFlag(Qt::Window);
    this->initUserGUI();
    this->populateDogList();
    this->connectSignalsAndSlots();
}

void UserGUI::initUserGUI() {
    auto* layout = new QVBoxLayout(this);
    QFont titleFont = this->titleWidget->font();
    this->titleWidget->setText("<p style='text-align:center'><font color=#4D2D52>USER MODE <br> Select the type of file you want for saving your adopted dogs!</font></p>");
    titleFont.setItalic(true);
    titleFont.setPointSize(10);
    titleFont.setStyleHint(QFont::System);
    //titleFont.setWeight(63);
    this->titleWidget->setFont(titleFont);
    layout->addWidget(this->titleWidget);

    auto* radioButtonsLayout = new QGridLayout(this);
    radioButtonsLayout->addWidget(this->csvButton, 0, 0);
    radioButtonsLayout->addWidget(this->htmlButton, 1, 0);
    radioButtonsLayout->addWidget(this->openListButton, 0, 1);
    layout->addLayout(radioButtonsLayout);

    auto* listLayout = new QGridLayout(this);
    listLayout->addWidget(this->dogsListWidget, 0, 0);
    listLayout->addWidget(this->adoptionListWidget, 0, 1);
    layout->addLayout(listLayout);

    auto* dogDetailsLayout = new QFormLayout{};
    dogDetailsLayout->addRow("Name", this->nameLineEdit);
    dogDetailsLayout->addRow("Breed", this->breedLineEdit);
    dogDetailsLayout->addRow("Age", this->ageLineEdit);
    dogDetailsLayout->addRow("Link", this->linkLineEdit);
    dogDetailsLayout->addRow(this->addButton);
    layout->addLayout(dogDetailsLayout);


    auto* filterTitle = new QLabel("<p style='text-align:center'><font color=#4D2D52><br>Filter the available dogs by breed and age</font></p>");
    QFont filterFont = filterTitle->font();
    filterFont.setPointSize(10);
    filterFont.setStyleHint(QFont::System);
    //filterFont.setWeight(63);
    filterTitle->setFont(filterFont);
    layout->addWidget(filterTitle);

    auto* filterDetailsLayout = new QFormLayout{};
    filterDetailsLayout->addRow("Breed", this->breedFilterLineEdit);
    filterDetailsLayout->addRow("Age", this->ageFilterLineEdit);
    filterDetailsLayout->addRow(this->filterButton);
    layout->addLayout(filterDetailsLayout);
}

void UserGUI::populateDogList() {
    this->dogsListWidget->clear();
    std::vector<Dog> allDogs = this->service.get_dogs();
    for (Dog& dog : allDogs)
        this->dogsListWidget->addItem(QString::fromStdString(dog.get_name()));
}

void UserGUI::connectSignalsAndSlots() {
    QObject::connect(this->dogsListWidget, &QListWidget::itemClicked, [this]() {
        std::string dog_name = this->dogsListWidget->selectedItems().at(0)->text().toStdString();
        int index = this->service.search_dog_by_name(dog_name);
        Dog dog = this->service.get_dogs()[index];
        this->nameLineEdit->setText(QString::fromStdString(dog.get_name()));
        this->breedLineEdit->setText(QString::fromStdString(dog.get_breed()));
        this->ageLineEdit->setText(QString::fromStdString(std::to_string(dog.get_age())));
        this->linkLineEdit->setText(QString::fromStdString(dog.get_photograph()));
        std::string link = std::string("start ").append(dog.get_photograph());
        system(link.c_str());
        });

    QObject::connect(this->addButton, &QPushButton::clicked, this, &UserGUI::addDog);
    QObject::connect(this->filterButton, &QPushButton::clicked, this, &UserGUI::filterDogs);
    QObject::connect(this->htmlButton, &QPushButton::clicked, this, &UserGUI::save_html);

    QObject::connect(this->csvButton, &QRadioButton::clicked, [this]() {
        this->service.write_to_file();
        this->repoTypeSelected = true;
        });


    QObject::connect(this->htmlButton, &QRadioButton::clicked, [this]() {
        this->service.write_to_file();
        this->repoTypeSelected = true;
        });
}


void UserGUI::save_html()
{
    std::string s = this->userService.get_file_name();

    
}

int UserGUI::getSelectedIndex() const {
    QModelIndexList selectedIndexes = this->dogsListWidget->selectionModel()->selectedIndexes();
    if (selectedIndexes.empty()) {
        this->nameLineEdit->clear();
        this->breedLineEdit->clear();
        this->ageLineEdit->clear();
        this->linkLineEdit->clear();
        return -1;
    }
    int selectedIndex = selectedIndexes.at(0).row();
    return selectedIndex;
}

void UserGUI::populateAdoptionList() {
    this->adoptionListWidget->clear();
    std::vector<Dog> allDogs = this->userService.get_all_dogs();
    for (Dog& dog : allDogs)
        this->adoptionListWidget->addItem(QString::fromStdString(dog.get_name()));
}

void UserGUI::addDog() {
    //if (!this->repoTypeSelected) {
        //auto* error = new QMessageBox();
        //error->setIcon(QMessageBox::Warning);
        //error->setText("Please select the type of file you want!");
        //error->setWindowTitle("File type warning!");
        //error->exec();
    //}
    if (!this->repoTypeSelected){}
    else {
        std::string breed = this->breedLineEdit->text().toStdString();
        std::string name = this->nameLineEdit->text().toStdString();
        std::string age_s = this->ageLineEdit->text().toStdString();
        std::string link = this->linkLineEdit->text().toStdString();
        int age;
            age = stoi(age_s);
            Dog dog = Dog(breed, name, age, link);
            this->userService.add_dog(dog);
            if (!this->filtered)
                this->populateDogList();
            else
                this->adoptionListWidget->addItem(this->dogsListWidget->takeItem(this->getSelectedIndex()));
            this->populateAdoptionList();
       
    }
}

void UserGUI::filterDogs() {
    
        std::string breed_filter = this->breedFilterLineEdit->text().toStdString();
        std::string age_filter_s = this->ageFilterLineEdit->text().toStdString();
        int age;
        if (breed_filter.empty() && age_filter_s.empty()) {
            this->filtered = false;
            this->populateDogList();
        }
        else {
            age = stoi(age_filter_s);
            std::vector<Dog> validDogs;
            this->service.getFiltered(validDogs, breed_filter, age);
            
                this->filtered = true;
                this->dogsListWidget->clear();
                for (Dog& dog : validDogs)
                    this->dogsListWidget->addItem(QString::fromStdString(dog.get_name()));
            
        }
   
}



UserGUI::~UserGUI() = default;

int DogListModel::rowCount(const QModelIndex & parent) const {
    return this->repository.get_dogs().size();
}

QVariant DogListModel::data(const QModelIndex & index, int role) const {
    int row = index.row();
    Dog currentDog = this->repository.get_dogs()[row];
    if (role == Qt::DisplayRole)
    {
        return QString::fromStdString(currentDog.get_name());
    }
    return QVariant();
}

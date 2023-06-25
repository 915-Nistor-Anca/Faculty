#include "UserWindow.h"
#include <QMessageBox>
#include <fstream>
using namespace std;

UserWindow::UserWindow(std::string username, service& serv, QWidget *parent)
	: QMainWindow(parent), username(username), serv(serv)
{
	ui.setupUi(this);
	this->setWindowTitle(QString::fromStdString(username));
	populateUserQuestions();
	connectSignalsAndSlots();
	populateAllQuestions();
}

UserWindow::~UserWindow()
{
}

void UserWindow::populateUserQuestions()
{
	this->ui.listWidget->clear();
	vector<question> user_questions;
	for (question q : serv.getQuestions()) {
		if (q.getUsername() == username) {
			user_questions.push_back(q);
		}
	}
	vector<pair<int, int>> nb;
	for (question q : user_questions) {
		int k = 0;
		for (answer a : serv.getAnswers()) {
			if (a.getIdQuestion() == q.getId()) k++;
		}
		nb.push_back(make_pair(k, q.getId()));
	}
	std::sort(nb.begin(), nb.end(), [](const pair<int, int>& p1, const pair<int, int>& p2) {
		return p1.first > p2.first; });

	for (pair<int, int>&p: nb){
		for (question q : user_questions) {
			if (q.getId()==p.second)
				this->ui.listWidget->addItem(QString::fromStdString(q.getText() + '|' +  std::to_string(p.first)));
		}
	}
}

void UserWindow::addQuestion()
{
	string text = this->ui.lineEdit->text().toStdString();
	if (text == "") QMessageBox::critical(this, "Error", "Text cannot be empty!");
	else {
		int l = serv.getQuestions().size();
		question q(l + 1, text, username);
		serv.addQuestion(q);
		populateUserQuestions();
		populateAllQuestions();
		this->ui.listWidget_3->clear();
	}
}

void UserWindow::connectSignalsAndSlots()
{
	QObject::connect(this->ui.pushButton, &QPushButton::clicked, this, &UserWindow::addQuestion);
	QObject::connect(this->ui.listWidget_2, &QListWidget::itemClicked, this, &UserWindow::seeAnswers);
	QObject::connect(this->ui.pushButton_2, &QPushButton::clicked, this, &UserWindow::addAnswer);
	QObject::connect(this->ui.listWidget_3, &QListWidget::itemDoubleClicked, this, &UserWindow::setSpinValue);
	QObject::connect(this->ui.pushButton_3, &QPushButton::clicked, this, &UserWindow::setNewVotes);

}

void UserWindow::populateAllQuestions()
{
	for (question q : serv.getQuestions()) {
		this->ui.listWidget_2->addItem(QString::fromStdString(q.getText()));
	}
}

void UserWindow::seeAnswers()
{
	this->ui.listWidget_3->clear();
	string text = this->ui.listWidget_2->selectedItems().at(0)->text().toStdString();
	int id;
	for (question q : serv.getQuestions()) if (q.getText() == text) id = q.getId();
	for (answer a : serv.getAnswers()) {
		if (a.getIdQuestion() == id)
			//this->ui.listWidget_3->addItem(QString::fromStdString(a.getText() + '|' + a.getUsername()));
			if (a.getUsername() == username) {
				QListWidgetItem* item = new QListWidgetItem(QString::fromStdString(a.getText() + '|' + username + '|' + std::to_string(a.getVotes())));
				item->setBackground(QBrush(Qt::yellow));
				this->ui.listWidget_3->addItem(item);
			}
			else {
				this->ui.listWidget_3->addItem(QString::fromStdString(a.getText() + '|' + a.getUsername() + '|' + std::to_string(a.getVotes())));
			}
	}
}

void UserWindow::addAnswer()
{
	string text = this->ui.listWidget_2->selectedItems().at(0)->text().toStdString();
	int id;
	for (question q : serv.getQuestions()) if (q.getText() == text) id = q.getId();
	string text_answer = this->ui.lineEdit_2->text().toStdString();
	if (text_answer == "") QMessageBox::critical(this, "Error", "Text cannot be empty!");
	else {
		int l = serv.getAnswers().size();
		answer a(l + 1, id, username, text_answer, 0);
		serv.addAnswer(a);
		seeAnswers();
	}
}

void UserWindow::setSpinValue()
{
	this->ui.spinBox->setEnabled(true);
	string text2 = this->ui.listWidget_3->selectedItems().at(0)->text().toStdString();
	string text = text2.substr(0, text2.find("|"));
	int votes = 0;
	string usern;
	for (answer a : serv.getAnswers()) if (a.getText() == text) {
		votes = a.getVotes();
		usern = a.getUsername();
	}
	this->ui.spinBox->setValue(votes);
	if (usern == username) this->ui.spinBox->setEnabled(false);
}

void UserWindow::setNewVotes()
{
	string text2 = this->ui.listWidget_3->selectedItems().at(0)->text().toStdString();
	string text = text2.substr(0, text2.find("|"));
	int value = this->ui.spinBox->value();
	vector<int> v1, v2;
	for (answer a : serv.getAnswers()) {
		if (a.getText() == text)
		{
			serv.updateVotes(text, value);
			
		}
		v1.push_back(a.getVotes());
	}
	for (answer a : serv.getAnswers()) v2.push_back(a.getVotes());
	seeAnswers();
	
}


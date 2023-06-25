#pragma once

#include <QMainWindow>
#include "ui_UserWindow.h"
#include "service.h"

class UserWindow : public QMainWindow
{
	Q_OBJECT

public:
	UserWindow(std::string username, service& serv, QWidget *parent = nullptr);
	~UserWindow();

private:
	Ui::UserWindowClass ui;
	std::string username;
	service& serv;
	void populateUserQuestions();
	void addQuestion();
	void connectSignalsAndSlots();
	void populateAllQuestions();
	void seeAnswers();
	void addAnswer();
	void setSpinValue();
	void setNewVotes();
	
};

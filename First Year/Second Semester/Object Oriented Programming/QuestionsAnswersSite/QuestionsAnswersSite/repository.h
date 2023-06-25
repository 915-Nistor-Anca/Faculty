#pragma once
#include "question.h"
#include "answer.h"
#include "user.h"
#include <vector>

class repository
{
private:
	vector<question> questions;
	vector<answer> answers;
	vector<user> users;

public:
	repository();
	void loadUsers();
	void loadQuestions();
	void loadAnswers();
	vector<user> getUsers();
	vector<question> getQuestions();
	vector<answer> getAnswers();
	void addQuestion(question q);
	void addAnswer(answer a);
	void updateVotes(string text, int new_value);
};


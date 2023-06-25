#pragma once
#include "repository.h"

class service
{
private:
	repository repo;
public:
	service(repository repo);
	vector<user> getUsers();
	vector<question> getQuestions();
	vector<answer> getAnswers();
	void addQuestion(question q);
	void addAnswer(answer a);
	void writeToFile();
	~service();
	void updateVotes(string text, int new_value);
};


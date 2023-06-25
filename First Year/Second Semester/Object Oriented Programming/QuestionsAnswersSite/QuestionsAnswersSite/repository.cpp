#include "repository.h"
#include <fstream>
#include <sstream>

repository::repository()
{
	loadUsers();
	loadQuestions();
	loadAnswers();
}

void repository::loadUsers()
{
	ifstream file("D:\\Fisiere facultate\\OOP\\Modele\\QuestionsAnswersSite\\QuestionsAnswersSite\\users.txt");
	string line;
	while (getline(file, line)) {
		vector<string> fields;
		istringstream iss(line);
		string field;
		while (getline(iss, field, '|')) {
			fields.push_back(field);
		}

		string name = fields[0];

		user u(name);
		users.push_back(u);

		field.clear();
	}

}

void repository::loadQuestions()
{
	ifstream file("D:\\Fisiere facultate\\OOP\\Modele\\QuestionsAnswersSite\\QuestionsAnswersSite\\questions.txt");
	string line;
	while (getline(file, line)) {
		vector<string> fields;
		istringstream iss(line);
		string field;
		while (getline(iss, field, '|')) {
			fields.push_back(field);
		}

		int id = stoi(fields[0]);
		string text = fields[1];
		string user = fields[2];

		question q(id, text, user);
		questions.push_back(q);

		field.clear();
	}
}

void repository::loadAnswers()
{
	ifstream file("D:\\Fisiere facultate\\OOP\\Modele\\QuestionsAnswersSite\\QuestionsAnswersSite\\answers.txt");
	string line;
	while (getline(file, line)) {
		vector<string> fields;
		istringstream iss(line);
		string field;
		while (getline(iss, field, '|')) {
			fields.push_back(field);
		}

		int id = stoi(fields[0]);
		int id_question = stoi(fields[1]);
		string user = fields[2];
		string text = fields[3];
		int votes = stoi(fields[4]);

		answer a(id, id_question, user, text, votes);
		answers.push_back(a);

		field.clear();
	}
}

vector<user> repository::getUsers()
{
	return users;
}

vector<question> repository::getQuestions()
{
	return questions;
}

vector<answer> repository::getAnswers()
{
	return answers;
}

void repository::addQuestion(question q)
{
	questions.push_back(q);
}

void repository::addAnswer(answer a)
{
	answers.push_back(a);
}

void repository::updateVotes(string text, int new_value)
{
	for (answer& a : answers) {
		if (a.getText() == text) a.updateVotes(new_value);
	}
}

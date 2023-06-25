#include "service.h"
#include <fstream>
service::service(repository repo)
	:repo(repo)
{
}

vector<user> service::getUsers()
{
	return repo.getUsers();
}

vector<question> service::getQuestions()
{
	return repo.getQuestions();
}

vector<answer> service::getAnswers()
{
	return repo.getAnswers();
}

void service::addQuestion(question q)
{
	repo.addQuestion(q);
}

void service::addAnswer(answer a)
{
	repo.addAnswer(a);
}


void service::writeToFile()
{
	ofstream file_answers("D:\\Fisiere facultate\\OOP\\Modele\\QuestionsAnswersSite\\QuestionsAnswersSite\\answers.txt");
	ofstream file_questions("D:\\Fisiere facultate\\OOP\\Modele\\QuestionsAnswersSite\\QuestionsAnswersSite\\questions.txt");


	if (file_answers.is_open()) {
		for (answer a : repo.getAnswers())
			file_answers << a.getId() << '|' << a.getIdQuestion() << '|' << a.getUsername() << '|' << a.getText() << '|' << a.getVotes() << '\n';
		file_answers.close();
	}
	if (file_questions.is_open()) {
		for (question q : repo.getQuestions())
			file_questions << q.getId() << '|' << q.getText() << '|' << q.getUsername() << '\n';
		file_questions.close();
	}
}

service::~service()
{
	writeToFile();
}

void service::updateVotes(string text, int new_value)
{
	repo.updateVotes(text, new_value);
}

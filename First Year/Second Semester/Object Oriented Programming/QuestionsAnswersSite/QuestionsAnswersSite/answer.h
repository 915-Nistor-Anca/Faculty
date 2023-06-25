#pragma once
using namespace std;
#include <string>
class answer
{
private:
	int id;
	int id_question;
	string username;
	string text;
	int votes;

public:
	answer(int id, int id_question, string username, string text, int votes);
	int getId();
	int getIdQuestion();
	string getUsername();
	string getText();
	int getVotes();
	void updateVotes(int value);
};


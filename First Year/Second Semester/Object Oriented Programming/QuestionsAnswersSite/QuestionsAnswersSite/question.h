#pragma once
using namespace std;
#include <string>

class question
{
private:
	int id;
	string text;
	string username;
public:
	question(int id, string text, string username);
	int getId();
	string getText();
	string getUsername();
};


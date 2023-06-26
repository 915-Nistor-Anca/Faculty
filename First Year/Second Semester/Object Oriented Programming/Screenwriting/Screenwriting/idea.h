#pragma once
#include <string>
using namespace std;

class idea
{
private:
	string description;
	string status;
	string creator;
	int act;
public:
	idea(string description, string status, string creator, int act);
	string getDescription();
	string getStatus();
	string getCreator();
	int getAct();
	void updateStatus(string new_status);
	void updateDescription(string new_description);
};


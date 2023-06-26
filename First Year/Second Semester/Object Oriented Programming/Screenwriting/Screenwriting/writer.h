#pragma once
#include <string>
using namespace std;

class writer
{
private:
	string name;
	string expertise;
public:
	writer(string name, string expertise);
	string getName();
	string getExpertise();
};


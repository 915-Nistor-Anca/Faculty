#pragma once
#include <string>
using namespace std;
class courier
{
private:
	string name;
	string streets;
	string zone;
public:
	courier(string name, string streets, string zone);
	string getName();
	string getStreets();
	string getZone();
};


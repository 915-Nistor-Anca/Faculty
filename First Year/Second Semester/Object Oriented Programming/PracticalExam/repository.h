#pragma once
#include <vector>
#include <fstream>
#include <sstream>

#include "package.h"
#include "courier.h"
using namespace std;

class repository
{
private:
	vector<courier> couriers;
	vector<package> packages;
public:
	repository();
	void readFromFile();
	vector<courier> getCouriers();
	vector<package> getPackages();
	void addPackage(package p);
	void deliverPackage(string recipient);
};


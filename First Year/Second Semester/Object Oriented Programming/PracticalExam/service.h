#pragma once
#include "repository.h"
#include "observer.h"

class service :public Subject
{
private:
	repository repo;
public:
	service(repository repo);
	vector<package> getPackages();
	vector<courier> getCouriers();
	void writeToFile();
	~service();
	void addPackage(package p);
	void deliverPackage(string recipient);
};


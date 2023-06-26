#pragma once
#include "repository.h"

class service
{
private:
	repository repo;
public:
	service(repository repo);
	vector<writer> getWriters();
	vector<idea> getIdeas();
	void changeIdeaStatus(string description, string new_status);
	void writeToFile();
	~service();
	void addIdea(idea i);
	void changeDescription(string description, string new_description);
};


#pragma once
#include "writer.h"
#include "idea.h"
#include <vector>

class repository
{
private:
	vector<writer> writers;
	vector<idea> ideas;
public:
	repository();
	void readFromFile();
	vector<writer> getWriters();
	vector<idea> getIdeas();
	void addIdea(idea i);
	void changeIdeaStatus(string description, string new_status);
	void changeDescription(string description, string new_description);
};


#include "repository.h"
#include <fstream>
#include <sstream>

repository::repository()
{
	readFromFile();
}

void repository::readFromFile()
{
	ifstream file_writers("D:\\Fisiere facultate\\OOP\\Modele\\Screenwriting\\Screenwriting\\writers.txt");
	ifstream file_ideas("D:\\Fisiere facultate\\OOP\\Modele\\Screenwriting\\Screenwriting\\ideas.txt");

	string line;
	while (getline(file_writers, line)) {
		vector<string> fields;
		istringstream iss(line);
		string field;
		while (getline(iss, field, '|')) {
			fields.push_back(field);
		}
		string name = fields[0];
		string expertise = fields[1];
		writer w(name, expertise);
		writers.push_back(w);

		field.clear();
	}

	while (getline(file_ideas, line)) {
		vector<string> fields;
		istringstream iss(line);
		string field;
		while (getline(iss, field, '|')) {
			fields.push_back(field);
		}
		string descr = fields[0];
		string status = fields[1];
		string creator = fields[2];
		int act = stoi(fields[3]);
		idea i(descr, status, creator, act);
		ideas.push_back(i);

		field.clear();
	}

}

vector<writer> repository::getWriters()
{
	return writers;
}

vector<idea> repository::getIdeas()
{
	return ideas;
}

void repository::addIdea(idea i)
{
	ideas.push_back(i);
}

void repository::changeIdeaStatus(string description, string new_status)
{
	for (idea& i : ideas) {
		if (i.getDescription() == description) i.updateStatus(new_status);
	}
}

void repository::changeDescription(string description, string new_description)
{
	for (idea& i : ideas)
		if (i.getDescription() == description) i.updateDescription(new_description);
}

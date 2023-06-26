#include "service.h"
#include <fstream>

service::service(repository repo)
	:repo(repo)
{
}

vector<writer> service::getWriters()
{
	return repo.getWriters();
}

vector<idea> service::getIdeas()
{
	return repo.getIdeas();
}

void service::changeIdeaStatus(string description, string new_status)
{
	repo.changeIdeaStatus(description, new_status);
}

void service::writeToFile()
{
	ofstream file_writers("D:\\Fisiere facultate\\OOP\\Modele\\Screenwriting\\Screenwriting\\writers.txt");
	ofstream file_ideas("D:\\Fisiere facultate\\OOP\\Modele\\Screenwriting\\Screenwriting\\ideas.txt");

	if (file_writers.is_open())
		for (writer w : repo.getWriters())
			file_writers << w.getName() << '|' << w.getExpertise() << '\n';

	if (file_ideas.is_open())
		for (idea i : repo.getIdeas())
			file_ideas << i.getDescription() << '|' << i.getStatus() << '|' << i.getCreator() << '|' << i.getAct() << '\n';

	file_writers.close();
	file_ideas.close();
}

service::~service()
{
	writeToFile();
}

void service::addIdea(idea i)
{
	repo.addIdea(i);
}

void service::changeDescription(string description, string new_description)
{
	repo.changeDescription(description, new_description);
}

#include "idea.h"

idea::idea(string description, string status, string creator, int act)
	:description(description), status(status), creator(creator), act(act)
{
}

string idea::getDescription()
{
	return description;
}

string idea::getStatus()
{
	return status;
}

string idea::getCreator()
{
	return creator;
}

int idea::getAct()
{
	return act;
}

void idea::updateStatus(string new_status)
{
	status = new_status;
}

void idea::updateDescription(string new_description)
{
	description = new_description;
}

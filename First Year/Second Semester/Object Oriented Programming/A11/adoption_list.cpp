#pragma once
#include "adoption_list.h"
#include "domain.h"

AdoptionList::AdoptionList()
{
}

AdoptionList::~AdoptionList()
{
}

void AdoptionList::add_dog(const Dog& d)
{
	dogs.push_back(d);
}

void AdoptionList::save_file()
{
}

void AdoptionList::delete_dog(const std::string& name) {
	for (int i = 0; i < dogs.size(); i++)
	{
		if (dogs[i].get_name() == name)
			dogs.erase(dogs.begin() + i);
		break;
	}
}


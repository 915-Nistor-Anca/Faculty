#pragma once
#include <vector>
#include <string>
#include "domain.h"
//using namespace std;

class AdoptionList {
protected:
	std::vector<Dog> dogs;
public:
	AdoptionList();
	~AdoptionList();
	virtual void add_dog(const Dog& d);
	virtual void delete_dog(const std::string& name);
	virtual void save_file();
	virtual std::string get_file_name() = 0;
};
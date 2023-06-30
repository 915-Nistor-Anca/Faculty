#include "repository.h"

repository::repository()
{
	readFromFile();
}

void repository::readFromFile()
{
	ifstream file1("D:\\Fisiere facultate\\OOP\\PracticalExam\\PracticalExam\\couriers.txt");
	string line;
	while (getline(file1, line)) {
		vector<string> fields;
		istringstream iss(line);
		string field;
		while (getline(iss, field, '|')) {
			fields.push_back(field);
		}
		string name = fields[0];
		string streets = fields[1];
		string zone = fields[2];
		courier c(name, streets, zone);
		couriers.push_back(c);

		field.clear();
	}

	ifstream file2("D:\\Fisiere facultate\\OOP\\PracticalExam\\PracticalExam\\packages.txt");
	string line2;
	while (getline(file2, line2)) {
		vector<string> fields;
		istringstream iss(line2);
		string field;
		while (getline(iss, field, '|')) {
			fields.push_back(field);
		}
		string recipient = fields[0];
		string address = fields[1];
		string location = fields[2];
		bool delivery_status = stoi(fields[3]);
		
		package p(recipient, address, location, delivery_status);
		packages.push_back(p);

		field.clear();
	}
}

vector<courier> repository::getCouriers()
{
	return couriers;
}

vector<package> repository::getPackages()
{
	return packages;
}

void repository::addPackage(package p)
{
	packages.push_back(p);
}

void repository::deliverPackage(string recipient)
{
	for (package& p : packages) {
		if (p.getRecipient() == recipient) p.updateDeliveryStatus();
	}
}

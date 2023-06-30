#include "service.h"

service::service(repository repo)
	:repo(repo)
{
}

vector<package> service::getPackages()
{
	return repo.getPackages();
}

vector<courier> service::getCouriers()
{
	return repo.getCouriers();
}

void service::writeToFile()
{
	ofstream f1("D:\\Fisiere facultate\\OOP\\PracticalExam\\PracticalExam\\packages.txt");
	if (f1.is_open()) {
		for (package p : repo.getPackages())
			f1 << p.getRecipient() << '|' << p.getAddress() << '|' << p.getLocation() << '|' << p.getDeliveryStatus() << '\n';
	}

	ofstream f2("D:\\Fisiere facultate\\OOP\\PracticalExam\\PracticalExam\\couriers.txt");
	if (f2.is_open()) {
		for (courier c : repo.getCouriers()) {
			f2 << c.getName() << '|' << c.getStreets() << '|' << c.getZone() << '\n';
		}
		}

	f1.close();
	f2.close();
}

service::~service()
{
	writeToFile();
}

void service::addPackage(package p)
{
	repo.addPackage(p);
	this->notify();
}

void service::deliverPackage(string recipient)
{
	repo.deliverPackage(recipient);
	this->notify();
}

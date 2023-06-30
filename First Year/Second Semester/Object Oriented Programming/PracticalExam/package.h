#pragma once
#include <string>
using namespace std;

class package
{
private:
	string recipient;
	string address;
	string location;
	bool delivery_status;
public:
	package(string recipient, string address, string location, bool delivery_status);
	string getRecipient();
	string getAddress();
	string getLocation();
	bool getDeliveryStatus();
	void updateDeliveryStatus();
};


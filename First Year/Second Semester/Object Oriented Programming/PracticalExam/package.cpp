#include "package.h"

package::package(string recipient, string address, string location, bool delivery_status)
	:recipient(recipient), address(address), location(location), delivery_status(delivery_status)
{
}

string package::getRecipient()
{
	return recipient;
}

string package::getAddress()
{
	return address;
}

string package::getLocation()
{
	return location;
}

bool package::getDeliveryStatus()
{
	return delivery_status;
}

void package::updateDeliveryStatus()
{
	delivery_status = 1;
}

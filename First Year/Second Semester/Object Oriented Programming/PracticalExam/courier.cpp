#include "courier.h"

courier::courier(string name, string streets, string zone)
	:name(name), streets(streets), zone(zone)
{
}

string courier::getName()
{
	return name;
}

string courier::getStreets()
{
	return streets;
}

string courier::getZone()
{
	return zone;
}

#include "writer.h"

writer::writer(string name, string expertise)
	:name(name), expertise(expertise)
{
}

string writer::getName()
{
	return name;
}

string writer::getExpertise()
{
	return expertise;
}

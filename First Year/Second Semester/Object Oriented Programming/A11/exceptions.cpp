#include "exceptions.h"

const char* DogAlreadyExists::what() const throw()
{
	return "There is already a dog with the given name.";
}

DogAlreadyExists::DogAlreadyExists()
{
}

DogAlreadyExists::~DogAlreadyExists()
{
}


const char* LengthIsZero::what() const throw() {
	return "The length is zero.";
}

LengthIsZero::~LengthIsZero() {}

LengthIsZero::LengthIsZero() {}

DogValidator::DogValidator()
{
}

bool DogValidator::validate_age(int age)
{
	if (age < 0 || age > 25) return false;
	return true;
}

bool DogValidator::validate_name(const std::string& name)
{
	for (char d : name)
		if (isdigit(d) != false) return false;
	return true;
}

DogValidator::~DogValidator()
{
}

const char* InvalidAge::what() const throw()
{
	return "The age is invalid.";
}

InvalidAge::InvalidAge()
{
}

InvalidAge::~InvalidAge()
{
}

const char* InvalidName::what() const throw()
{
	return "The name is invalid.";
}

InvalidName::InvalidName()
{
}

InvalidName::~InvalidName()
{
}

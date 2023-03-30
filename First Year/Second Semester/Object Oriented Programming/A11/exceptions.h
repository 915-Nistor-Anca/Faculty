#pragma once
#include <exception>
#include <string>
//using namespace std;

class DogAlreadyExists : public std::exception {
public:
	const char* what() const throw() override;
	DogAlreadyExists();
	~DogAlreadyExists() override;

};

class LengthIsZero : public std::exception {
public:
	const char* what() const throw() override;
	LengthIsZero();
	~LengthIsZero() override;
};

class InvalidAge : public std::exception {
public:
	const char* what() const throw() override;
	InvalidAge();
	~InvalidAge() override;
};

class InvalidName : public std::exception {
public:
	const char* what() const throw() override;
	InvalidName();
	~InvalidName() override;
};

class DogValidator {
public:
	DogValidator();
	bool validate_age(int age);
	bool validate_name(const std::string& name);
	~DogValidator();
};
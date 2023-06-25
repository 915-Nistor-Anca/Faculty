#include "question.h"

question::question(int id, string text, string username)
	:id(id), text(text), username(username)
{
}

int question::getId()
{
	return id;
}

string question::getText()
{
	return text;
}

string question::getUsername()
{
	return username;
}

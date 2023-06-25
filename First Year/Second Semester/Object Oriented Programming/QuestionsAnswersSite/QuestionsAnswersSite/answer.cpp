#include "answer.h"

answer::answer(int id, int id_question, string username, string text, int votes)
	:id(id), id_question(id_question), username(username), text(text), votes(votes)
{
}

int answer::getId()
{
	return id;
}
int answer::getIdQuestion()
{
	return id_question;
}

string answer::getUsername()
{
	return username;
}

string answer::getText()
{
	return text;
}

int answer::getVotes()
{
	return votes;
}

void answer::updateVotes(int value)
{
	votes = value;
}

#include "ListIterator.h"
#include "SortedIteratedList.h"
#include <exception>
#include <iostream>

using namespace std;

//theta(1)
ListIterator::ListIterator(const SortedIteratedList& list) : list(list) {
	//TODO - Implementation
	this->current = list.head;
}

//theta(1)
void ListIterator::first() {
	//TODO - Implementation
	this->current = this->list.head;
}

//theta(1)
void ListIterator::next() {
	//TODO - Implementation
	if (!this->valid()) throw std::exception();
	this->current = this->list.elems[this->current].next;
}

//theta(1)
bool ListIterator::valid() const {
	//TODO - Implementation
	return this->current != -1;
}

//theta(1)
TComp ListIterator::getCurrent() const {
	//TODO - Implementation
	if (!this->valid()) throw std::exception();
	return this->list.elems[this->current].info;
}

void ListIterator::jumpForward(int k)
{
	if (k <= 0 || !this->valid())
		throw std::exception();

	int steps = 0, pos = this->current;
	while (pos != -1) {
		pos = this->list.elems[pos].next;
		steps++;
	}

	if (steps < k) {
		this->current = -1;
	}
	else while (k) {
		this->next();
		k--;
	}
}



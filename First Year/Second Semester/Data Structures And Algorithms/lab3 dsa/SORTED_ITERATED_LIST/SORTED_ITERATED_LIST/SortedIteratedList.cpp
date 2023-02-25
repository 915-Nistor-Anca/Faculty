#include "ListIterator.h"
#include "SortedIteratedList.h"
#include <iostream>
using namespace std;
#include <exception>

//theta(1)
int SortedIteratedList::allocate()
{
	if (this->firstEmpty == -1)
		return -1;

	int newFreePos = this->firstEmpty;
	this->firstEmpty = this->elems[this->firstEmpty].next;
	return newFreePos;
}

//theta(1)
void SortedIteratedList::free(int pos)
{
	this->elems[pos].next = this->firstEmpty;
	this->firstEmpty = pos;
}


//theta(n)
SortedIteratedList::SortedIteratedList(Relation r) {
	//TODO - Implementation
	this->relation = r;
	this->nr_elements = 0;

	this->head = -1;
	this->tail = -1;
	this->firstEmpty = 0;

	for (int i = 0; i < this->cap-1; i++) {
		this->elems[i].next = i + 1;
	}
	this->elems[this->cap - 1].next = -1;

}

//theta(1)
int SortedIteratedList::size() const {
	//TODO - Implementation
	return this->nr_elements;
}


//theta(1)
bool SortedIteratedList::isEmpty() const {
	//TODO - Implementation
	return (this->nr_elements == 0);
}

//theta(1)
ListIterator SortedIteratedList::first() const {
	//TODO - Implementation
	return ListIterator(*this);
}


//theta(1)
TComp SortedIteratedList::getElement(ListIterator poz) const {
	//TODO - Implementation
	return poz.getCurrent();
}


// BC = theta(1), WC = AC = theta(n)
TComp SortedIteratedList::remove(ListIterator& poz) {
	//TODO - Implementation

	int i = poz.current;
	if (i < 0 || i >= this->nr_elements)
		throw exception();

	int k = 0, current = this->head, prev = -1;
	while (k < i && current != -1)
	{
		prev = current;
		current = this->elems[current].next;
		k++;
	}

	if (current != -1)
	{
		if (current == this->head)
		{
			this->head = this->elems[this->head].next;
		}
		else if (current == this->tail)
		{
			this->elems[prev].next = -1;
			this->tail = prev;
		}
		else
			this->elems[prev].next = this->elems[current].next;
		free(current);
		this->nr_elements--;
		return this->elems[current].info;
	}
	else
		throw exception();

}

// BC = theta(1), WC = AC = theta(n)
ListIterator SortedIteratedList::search(TComp e) const {
	//TODO - Implementation
	ListIterator node(*this);
	for (; node.valid(); node.next()) {
		if (node.getCurrent() == e) {
			return node;
		}
	}
	return node;
}


// BC = theta(1), WC = AC = theta(n)
void SortedIteratedList::add(TComp e) {
	//TODO - Implementation
	
	int pos = this->allocate();
	int current = this->head, prev = -1;
	while (current != -1 && this->relation(this->elems[current].info, e) == false) {
		prev = current;
		current = this->elems[current].next;
	}
	if (current == -1) {
		if (prev == -1) this->head = pos;
		else this->elems[this->tail].next = pos;
		this->tail = pos;
		this->elems[pos].next = -1;
	}
	else {
		if (prev == -1) {
			this->elems[pos].next = this->head;
			this->head = pos;
		}
		else {
			this->elems[prev].next = pos;
			this->elems[pos].next = current;
		}
	}
	this->elems[pos].info = e;
	this->nr_elements++;

}

SortedIteratedList::~SortedIteratedList() = default;
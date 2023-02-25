#include "SetIterator.h"
#include "Set.h"
#include <exception>

//BC: Theta(1), WC: Theta(capacity) -> Total complexity: O(capacity)
SetIterator::SetIterator(const Set& m) : set(m)
{
	//TODO - Implementation
	this->current_e = 0;
	while (this->current_e < this->set.m && (this->set.elems[this->current_e] == NULL_TELEM))
		this->current_e++;
	this->first_e = this->current_e;
}

//BC: Theta(1), WC: Theta(capacity) -> Total complexity: O(capacity)
void SetIterator::first() {
	//TODO - Implementation
	this->current_e = 0;
	while (this->current_e < this->set.m && (this->set.elems[this->current_e] == NULL_TELEM))
		this->current_e++;
	this->first_e = current_e;
}

//BC: Theta(1), WC: Theta(capacity) -> Total complexity: O(capacity)
void SetIterator::next() {
	//TODO - Implementation
	if (this->current_e >= this->set.m)
		throw std::exception();
	this->current_e++;
	while (this->current_e < this->set.m && (this->set.elems[this->current_e] == NULL_TELEM))
		this->current_e++;
}

//Theta(1)
TElem SetIterator::getCurrent()
{
	//TODO - Implementation
	if (this->current_e >= this->set.m)
		throw std::exception();
	return this->set.elems[this->current_e];
}

//Theta(1)
bool SetIterator::valid() const {
	//TODO - Implementation
	if (this->current_e < this->set.m)
		return true;
	return false;
}




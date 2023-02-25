#include "Set.h"
#include "SetITerator.h"
#include <cstdlib>



int Set::hash(TElem value) const
{
	return abs(value) % this->m;
}


//BC: Theta(newCapacity), WC: Theta(newCapacity * nrElems) -> Total complexity: O(newCapacity * nrElems)
void Set::resize_and_rehash()
{
	int currentLength = this->length;
	int currentM = this->m;
	//the new capacity will be double as much as the previous one
	this->m = this->m * 2;
	int index;
	//saving the old elements
	auto oldElements = new TElem[currentM];
	for (index = 0; index < currentM; index++) {
		oldElements[index] = this->elems[index];
	}

	//deleting the old ones
	delete[] this->elems;
	this->elems = new TElem[this->m];
	delete[] this->next;
	this->next = new int[this->m];

	//initialising the list
	for (index = 0; index < this->m; index++) {
		this->elems[index] = NULL_TELEM;
		this->next[index] = -1;
	}
	//changing the initial list, but now the capacity is bigger
	this->first_empty = 0;
	for (index = 0; index < currentM; index++) {
		if (oldElements[index] != NULL_TELEM)
			add(oldElements[index]);
	}
	this->length = currentLength;

	delete[] oldElements;
}

//BC: Theta(1), WC: Theta(capacity) -> Total complexity: O(capacity)
void Set::change_first_empty()
{
	this->first_empty = this->first_empty + 1;
	while (this->first_empty < this->m && this->elems[this->first_empty] != NULL_TELEM)
		this->first_empty = this->first_empty + 1;
}

//Theta(capacity)
Set::Set() {
	//TODO - Implementation
	this->m = 13;
	this->length = 0;
	this->elems = new TElem[this->m];
	this->next = new int[this->m];
	int index;
	for (index = 0; index < this->m; index++) {
		this->elems[index] = NULL_TELEM;
		this->next[index] = -1;
	}
	this->first_empty = 0;
}

//BC: Theta(1), WC: Theta(nrElements) amortized-> Total complexity: O(nrElements)
bool Set::add(TElem elem) {
	//TODO - Implementation
	if (this->search(elem) == true) return false;

	bool returnValue = false;
	TElem element = elem;
	int hashValue = this->hash(elem);
	if (this->elems[hashValue] == NULL_TELEM) { //it means the set is empty
		if (hashValue == first_empty)
			this->change_first_empty();
		this->elems[hashValue] = element;
		this->next[hashValue] = -1;
		this->length++;
		returnValue = true;
	}
	else {
		if (this->first_empty == this->m)
			this->resize_and_rehash();
		int currentPosition = hashValue;
		while (this->next[currentPosition] != -1 && this->elems[currentPosition] != elem) {
			currentPosition = this->next[currentPosition];
		}
		if (this->elems[currentPosition] == elem) { //it means the element already exists
			returnValue = false;
		}
		else if (this->next[currentPosition] == -1) { //it is put on the last position
			this->elems[this->first_empty] = element;
			this->next[this->first_empty] = -1;
			this->next[currentPosition] = this->first_empty;
			this->change_first_empty();
			this->length++;
			returnValue = true;
		}
	}
	return returnValue;
}

//BC: Theta(capacity), WC: Theta(NrElems^2)-> Total Complexity: O(nrElems^2)
bool Set::remove(TElem elem) {
	//TODO - Implementation
	int current = this->hash(elem);
	int prev = -1;
	while (current != -1 && this->elems[current] != elem) { //searching for the pos of the el
		prev = current;
		current = this->next[current];
	}

	if (current == -1) { //it means the element doesn't exist
		return false;
	}
	else {
		bool over = false;
		do { //moving all the elements after the el which has to be removed to their prev position
			int position = this->next[current];
			int prevPosition = current;
			while (position != -1 && this->hash(this->elems[position]) != current) {
				prevPosition = position;
				position = this->next[position];
			}
			if (position == -1)
				over = true;
			else {
				this->elems[current] = this->elems[position];
				prev = prevPosition;
				current = position;
			}
		} while (!over);
		if (prev == -1) { // it means is the first element
			int idx = 0;
			while (idx < this->m && prev == -1)
				if (this->next[idx] == current) {
					prev = idx;
				}
				else {
					idx = idx + 1;
				}
		}
		if (prev != -1)
			this->next[prev] = this->next[current];
		this->length--;
		this->elems[current] = NULL_TELEM;
		this->next[current] = -1;
	}
	return true;
}


//BC: Theta(1), WC: Theta(nrElements) -> Total complexity: O(nrElements)
bool Set::search(TElem elem) const {
	//TODO - Implementation
	int current_pos = this->hash(elem);
	while (this->next[current_pos] != -1 && this->elems[current_pos] != elem)
		current_pos = this->next[current_pos];
	if (this->elems[current_pos] == elem) return true;
	return false;
}

//Theta(1)
int Set::size() const {
	//TODO - Implementation
	return this->length;
}

//Theta(1)
bool Set::isEmpty() const {
	//TODO - Implementation
	return (this->length == 0);
}

//Theta(1)
Set::~Set() {
	//TODO - Implementation
	delete[] this->next;
	delete[] this->elems;
}


SetIterator Set::iterator() const {
	return SetIterator(*this);
}

int Set::getRange() const {
	if (this->isEmpty()) return -1;
	TElem max = -99999, min = 99999;
	SetIterator it = this->iterator();
	while (it.valid()) {
		if (it.getCurrent() > max) max = it.getCurrent();
		if (it.getCurrent() < min) min = it.getCurrent();
		it.next();
	}
	return max-min;
}

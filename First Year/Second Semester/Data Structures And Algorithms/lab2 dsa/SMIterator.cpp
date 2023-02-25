#include "SMIterator.h"
#include "SortedMap.h"
#include <exception>
#include <iostream>

using namespace std;

//theta(1)
SMIterator::SMIterator(const SortedMap& m) : map(m){
	//TODO - Implementation
	this->head = m.head;
	this->current_node = m.head;
}

//theta(1)
void SMIterator::first(){
	//TODO - Implementation
	this->current_node = this->head;
}

//theta(1)
void SMIterator::next(){
	//TODO - Implementation
	if (this->current_node == NULL) throw exception();
	this->current_node = this->current_node->next;
}

//theta(1)
bool SMIterator::valid() const{
	//TODO - Implementation
	return (this->current_node != NULL);
}

//theta(1)
TElem SMIterator::getCurrent() const{
	//TODO - Implementation
	if (this->current_node == NULL) throw exception();
	return this->current_node->info;

}
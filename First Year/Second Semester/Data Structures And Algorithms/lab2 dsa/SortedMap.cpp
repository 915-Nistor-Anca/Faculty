#include "SMIterator.h"
#include "SortedMap.h"
#include <exception>
#include <iostream>
using namespace std;

SortedMap::SortedMap(Relation r) {
	//TODO - Implementation
	this->nr_pairs = 0;
	this->relation = r;
	this->head = nullptr;
}


// best case = theta(1), worst case = theta(number of pairs), total = omega(nr of pairs)
TValue SortedMap::add(TKey k, TValue v) {
	//TODO - Implementation

	//if the map is empty
	if (this->nr_pairs == 0)
	{
		Node* new_node = new Node;
		new_node->info.first = k;
		new_node->info.second = v;
		new_node->next = nullptr;
		this->head = new_node;
		this->nr_pairs++;
		return NULL_TVALUE;
	}
	

	//if it has to be placed in the first position
	if (this->relation(this->head->info.first, k) == false)
	{
		Node* new_node = new Node;
		new_node->next = this->head;
		new_node->info.first = k;
		new_node->info.second = v;
		this->head = new_node;
		this->nr_pairs++;
		return NULL_TVALUE;
	}



	Node* current = this->head;
	Node* prev = NULL;

	while (current != NULL && this->relation(current->info.first, k) == true)
	{
		if (current->info.first == k) {
			TValue value = current->info.second;
			current->info.second = v;
			return value;
		}
		prev = current;
		current = current->next;
	}

	// if the place of the element is somewhere in the map, not in front and not at the end
	if (current != NULL)
	{
		Node* node = new Node;
		node->info.first = k;
		node->info.second = v;

		node->next = current;
		prev->next = node;
		this->nr_pairs++;
		return NULL_TVALUE;
	}

	// if the place of the element is in the end of the map
	Node* node = new Node;
	node->info.first = k;
	node->info.second = v;

	node->next = NULL;
	prev->next = node;
	this->nr_pairs++;
	return NULL_TVALUE;

}

// best case = theta(1), worst case = theta(number of pairs), total = omega(nr of pairs)
TValue SortedMap::search(TKey k) const {
	//TODO - Implementation
	Node* current = this->head;
	while (current != NULL)
	{
		if (current->info.first == k) return current->info.second;
		current = current->next;
	}
	return NULL_TVALUE;
}

// best case = theta(1), worst case = theta(number of pairs), total = omega(nr of pairs)
TValue SortedMap::remove(TKey k) {
	//TODO - Implementation
	if (this->search(k) == NULL_TVALUE) return NULL_TVALUE;
	Node* current = this->head;
	Node* prev = NULL;
	while (current != NULL && current->info.first != k) {
		prev = current;
		current = current->next;
	}
	if (prev == NULL) {
		TValue to_return = this->head->info.second;
		this->head = current->next;
		delete current;
		this->nr_pairs--;
		return to_return;
	}
	else
	{
		TValue to_return = current->info.second;
		prev->next = current->next;
		current->next = NULL;
		delete current;
		this->nr_pairs--;
		return to_return;
	}
}

//theta(1)
int SortedMap::size() const {
	//TODO - Implementation
	return this->nr_pairs;
}

//theta(1)
bool SortedMap::isEmpty() const {
	//TODO - Implementation
	if (this->head != nullptr) return false;
	return true;
}

SMIterator SortedMap::iterator() const {
	return SMIterator(*this);
}

//theta(number of pairs)
SortedMap::~SortedMap() {
	//TODO - Implementation

	if (this->head != NULL) {

		Node* current = this->head->next;
		Node* prev = this->head;

		while (current != NULL) {
			delete prev;
			prev = current;
			current = current->next;
		}

		delete prev;

	}

}

//theta(number of pairs)
void SortedMap::empty() {
	while (this->size() != 0) {
		Node* current = this->head;
		this->remove(current->info.first);
	}
}
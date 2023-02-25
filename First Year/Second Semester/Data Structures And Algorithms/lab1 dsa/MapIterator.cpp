#include "Map.h"
#include "MapIterator.h"
#include <exception>
using namespace std;


MapIterator::MapIterator(const Map& d) : map(d)
{
    this->current_element = 0;
    while (this->current_element < this->map.capacity && (this->map.elements[this->current_element] == NULL_TELEM))
        this->current_element++;
    this->first_element = this->current_element;
}

void MapIterator::first() {
    this->current_element = 0;
    while (this->current_element < this->map.capacity && (this->map.elements[this->current_element] == NULL_TELEM))
        this->current_element++;
    this->first_element = current_element;
}

void MapIterator::next() {
    if (this->current_element >= this->map.capacity)
        throw exception();
    this->current_element++;
    while (this->current_element < this->map.capacity && (this->map.elements[this->current_element] == NULL_TELEM))
        this->current_element++;
}

TElem MapIterator::getCurrent(){
    if (this->current_element >= this->map.capacity)
        throw exception();
    return this->map.elements[this->current_element];
}

bool MapIterator::valid() const {
    if(this->current_element < this->map.capacity)
        return true;
    return false;
}
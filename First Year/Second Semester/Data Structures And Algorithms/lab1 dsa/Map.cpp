#include <cmath>
#include "Map.h"
#include "MapIterator.h"

int Map::hash(TKey c) const {
    return abs(c) % this->capacity;
}

Map::Map() {
    this->capacity = 13;
    this->length = 0;
    this->elements = new TElem[this->capacity];
    this->next = new int[this->capacity];
    for(int i = 0; i < this->capacity; i++) {
        this->elements[i] = NULL_TELEM;
        this->next[i] = -1;
    }
    this->first_empty = 0;

}

Map::~Map() {
    delete[] this->elements;
    delete[] this->next;
}

void Map::changeFirstEmpty() {
    this->first_empty = this->first_empty + 1;
    while(this->first_empty < this->capacity && this->elements[this->first_empty] != NULL_TELEM)
        this->first_empty = this->first_empty + 1;
}

TValue Map::add(TKey c, TValue v){
    TValue return_value = NULL_TVALUE;
    TElem element;
    element.first = c;
    element.second = v;
    int hash_value = this->hash(c);
    if (this->elements[hash_value] == NULL_TELEM) { //the key does not exist, so it's created
        if(hash_value == first_empty)
            this->changeFirstEmpty();
        this->elements[hash_value] = element;
        this->next[hash_value] = -1;
        this->length++;
    } else { // the key exists
        if(this->first_empty == this->capacity)
            this->resize_and_rehash();
        int current_position = hash_value;
        while (this->next[current_position] != -1 && this->elements[current_position].first != c) {
            current_position = this->next[current_position];
        }
        if (this->elements[current_position].first == c) { // the old value is replaced and the function will return the old value
            return_value = this->elements[current_position].second;
            this->elements[current_position].second = v;
        } else if (this->next[current_position] == -1) {
            this->elements[this->first_empty] = element;
            this->next[this->first_empty] = -1;
            this->next[current_position] = this->first_empty;
            this->changeFirstEmpty();
            this->length++;
        }
    }
    return return_value;
}
//Total complexity: O(length)


TValue Map::search(TKey c) const {
    TValue return_value = NULL_TVALUE;
    int currentPosition = this->hash(c);
    while (this->next[currentPosition] != -1 && this->elements[currentPosition].first != c) {
        currentPosition = this->next[currentPosition];
    }
    if (this->elements[currentPosition].first == c) {
        return_value = this->elements[currentPosition].second;
    }
    return return_value;
}

//Total complexity: O(length)

TValue Map::remove(TKey c){
    TValue returnValue = NULL_TVALUE;
    int current = this->hash(c);
    int previous = -1;
    while (current != -1 && this->elements[current].first != c) {
        previous = current;
        current = this->next[current]; // searches for the key
    }

    if (current == -1) { // the key doesn't exist
        returnValue = NULL_TVALUE;
    } else{ // the key was found
        returnValue = this->elements[current].second;
        bool over = false;
        do {
            int position = this->next[current];
            int prevPosition = current;
            while (position != -1 && this->hash(this->elements[position].first) != current) {
                prevPosition = position;
                position = this->next[position];
            }
            if (position == -1) // it means we went over all the elements and the given key was deleted
                over = true;
            else {
                this->elements[current] = this->elements[position];
                previous = prevPosition;
                current = position;
            }
        } while (!over);
        if (previous == -1) {
            int idx = 0;
            while (idx < this->capacity && previous == -1)
                if (this->next[idx] == current) {
                    previous = idx;
                }else {
                    idx = idx + 1;
                }
        }
        if (previous != -1) //we handle the last element
            this->next[previous] = this->next[current];
        this->length--;
        this->elements[current] = NULL_TELEM;
        this->next[current] = -1;
        if (this->first_empty > current)
            this->first_empty = current;
    }
    return returnValue;
}

//Total Complexity: O(length^2)

void Map::resize_and_rehash() {
    int current_length = this->length;
    int current_m = this->capacity;
    this->capacity = this->capacity * 2;
    auto old_elements = new TElem[current_m];
    for(int i = 0; i < current_m; i++) {
        old_elements[i] = this->elements[i];
    }

    delete[] this->elements; // we give the new values
    this->elements = new TElem[this->capacity];
    delete[] this->next;
    this->next = new int[this->capacity];

    for(int i = 0; i < this->capacity; i++) {
        this->elements[i] = NULL_TELEM;
        this->next[i] = -1;
    }
    this->first_empty = 0;
    for(int i = 0; i < current_m; i++) {
        if (old_elements[i] != NULL_TELEM)
            add(old_elements[i].first, old_elements[i].second);
    }
    this->length = current_length;

    delete[] old_elements;
}


int Map::size() const {
    return this->length;
}

bool Map::isEmpty() const{
    if (this->length == 0) return true;
    return false;
}

MapIterator Map::iterator() const {
    return MapIterator(*this);
}

void Map::replace(TKey k, TValue oldValue, TValue newValue) {
    TValue result = search(k);
    if (result != NULL_TVALUE) //if k is in the map
    {
        int current_position = this->hash(k);
        while (this->next[current_position] != -1 && this->elements[current_position].first != k)
            current_position = this->next[current_position];
        if (this->elements[current_position].second == oldValue) //replace the value
            this->elements[current_position].second = newValue;
    }
}
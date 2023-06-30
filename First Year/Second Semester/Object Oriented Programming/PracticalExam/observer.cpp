#include "observer.h"

void Subject::addObserver(observer* o)
{
	this->observers.push_back(o);
}

void Subject::removeObserver(observer* o)
{
	auto it = std::find(observers.begin(), observers.end(), o);
	if (it != observers.end()) {
		observers.erase(it);
	}
}

void Subject::notify()
{
	for (auto o : observers) {
		o->update();
	}
}

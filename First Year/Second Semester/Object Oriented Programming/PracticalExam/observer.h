#pragma once
#include <vector>

class observer {
public:
	virtual void update() = 0;
	virtual ~observer() {}
};

class Subject {
private:
	std::vector<observer*> observers;

public:
	void addObserver(observer* o);
	void removeObserver(observer* o);
	void notify();

};
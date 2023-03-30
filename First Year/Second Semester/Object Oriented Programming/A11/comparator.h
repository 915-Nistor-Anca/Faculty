#pragma once
#include "domain.h"

template <typename Type>
class Comparator {
public:
	virtual bool operator()(Type& a, Type& b) = 0;

};

template <typename Type>
class CompAscendingByAge : public Comparator<Type> {
public:
	bool operator()(Type& a, Type& b) override;
};

template <typename Type>
class CompDescendingByName : public Comparator<Type> {
public:
	bool operator()(Type& a, Type& b) override;
};

template<typename Type>
bool CompAscendingByAge<Type>::operator()(Type& a, Type& b) {
	return (a.get_age() < b.get_age());
}

template<typename Type>
bool CompDescendingByName<Type>::operator()(Type& a, Type& b) {
	return a.get_name() > b.get_name();
}
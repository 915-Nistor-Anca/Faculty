#include "tests.h"
#include <assert.h>

#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
Tests::Tests()
{
}

Tests::~Tests()
{
}

void Tests::test_comparator()
{
	CompAscendingByAge<Dog> aba;
	vector<Dog> v;
	v.push_back(Dog("Golden Retriever", "Terry", 8, "photo"));
	v.push_back(Dog("Bulldog", "Aky", 2, "photo"));
	v.push_back(Dog("Husky", "Lucky", 4, "photo"));
	sort(v.begin(), v.end(), aba);
	assert(v[0].get_name() == "Aky");
	CompDescendingByName<Dog> dbn;
	sort(v.begin(), v.end(), dbn);
	assert(v[1].get_name() == "Lucky");
	//cout << "Comparator tested!\n";
}

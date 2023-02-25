#include "ExtendedTest.h"
#include "ShortTest.h"

#include "SortedMap.h"


#include <iostream>
using namespace std;


int main() {
	testAll();
	testAllExtended();
	test_new_functionality();

	cout << "That's all!" << endl;
	system("pause");
	return 0;
}



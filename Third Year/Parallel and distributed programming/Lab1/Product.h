#pragma once
#include <iostream>
using namespace std;

class Product
{
private:
	string name;
	int price;
	int quantity;
	int initial_quantity;
public:
	Product(string name, int price, int quantity);
	void setName(string new_name);
	void setPrice(int new_price);
	void setQuantity(int new_quantity);
	string getName();
	int getPrice();
	int getQuantity();
	int getInitialQuantity();

};


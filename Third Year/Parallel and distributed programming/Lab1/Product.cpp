#include "Product.h"

Product::Product(string name, int price, int quantity): name(name), price(price), quantity(quantity), initial_quantity(quantity)
{
}

void Product::setName(string new_name)
{
	this->name = new_name;
}

void Product::setPrice(int new_price)
{
	this->price = new_price;
}

void Product::setQuantity(int new_quantity)
{
	this->quantity = new_quantity;
}

string Product::getName()
{
	return this->name;
}

int Product::getPrice()
{
	return this->price;
}

int Product::getQuantity()
{
	return this->quantity;
}

int Product::getInitialQuantity()
{
	return initial_quantity;
}

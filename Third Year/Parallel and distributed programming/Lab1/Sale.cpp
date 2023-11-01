#include "Sale.h"

Sale::Sale(vector<pair<Product, int>> products): products(products) //, total_price(0)
{
}

vector<pair<Product, int>> Sale::getProductsAndQuantities()
{
	return this->products;
}

/*int Sale::getTotalPrice()
{
	return this->total_price;
}*/

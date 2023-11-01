#pragma once
#include <iostream>
#include "Product.h"
#include <vector>

using namespace std;

class Sale
{
private:
	vector<pair<Product, int>> products; //(product, quantity)
	//int total_price;
public:
	Sale(vector<pair<Product, int>> products);
	vector<pair<Product, int>> getProductsAndQuantities();
	//int getTotalPrice();
};


#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>
using namespace std;
#include "Product.h"
#include "Sale.h"
#include <random>
#include <mutex>
#include <thread>

mutex* products_mutexes;
mutex sale_mutex;
mutex money_mutex;
int money = 0;

vector<Product> products;
vector<Sale> sales;

void readProducts() {
	ifstream file("D:\\Facultate\\Programare paralela si distribuita\\Lab1\\Lab1\\products.txt");
	
	string line;
	while (getline(file, line)) {
		vector<string> fields;
		istringstream iss(line);
		string field;
		while (getline(iss, field, ' ')) {
			fields.push_back(field);
		}
		string name = fields[0];
		int price = stoi(fields[1]);
		int quantity = stoi(fields[2]);
		
		Product p(name, price, quantity);
		products.push_back(p);

		field.clear();
	}
}

void printAllProducts() {
	cout << "The products are:\n";
	cout << "Name  Price  Quantity  InitialQuantity\n";
	for (Product p : products) {
		cout << p.getName() << "  " << p.getPrice() << "       " << p.getQuantity() << "           " << p.getInitialQuantity() << '\n';
	}
	cout << '\n';
}

bool containsProduct(vector<Product> products, Product p) {
	for (Product pr : products) {
		if (pr.getName() == p.getName() && pr.getPrice() == p.getPrice() && pr.getQuantity() == p.getQuantity())
			return 1;
	}
	return 0;
}

Sale createOneSale() {
	random_device rand;
	mt19937 gen(rand());
	uniform_int_distribution<>dis(1, products.size());

	vector<Product> sale_products;
	int number_products = dis(gen);
	while (number_products > 0) {
		random_device rand2;
		mt19937 gen(rand());
		uniform_int_distribution<>dis2(0, products.size() - 1);
		int product_position = dis2(gen);

		while (containsProduct(sale_products, products[product_position])) {
			product_position = dis2(gen);
		}
		sale_products.push_back(products[product_position]);
		number_products--;
	}

	vector<pair<Product, int>> products_quantities;
	for (Product p : sale_products) {
		random_device rand3;
		mt19937 gen(rand());
		uniform_int_distribution<>dis3(1, 30);
		int quantity = dis3(gen);
		pair<Product, int> pairr = make_pair(p, quantity);
		products_quantities.push_back(pairr);
	}

	/*for (pair<Product, int> pair1 : products_quantities) {
		cout << pair1.first.getName() << ' ' << pair1.second << '\n';
	}*/

	Sale s(products_quantities);

	return s;
}

void processSale(Sale s) {
	for (pair<Product, int> p : s.getProductsAndQuantities()) {
		for (Product& prod : products) {
			int i = 0;
			if (prod.getName() == p.first.getName()) {
				products_mutexes[i].lock();
				money_mutex.lock();
				money += p.second * p.first.getPrice();
				money_mutex.unlock();
				//cout << prod.getQuantity() << ' ';
				prod.setQuantity(prod.getQuantity() - p.second);
				//cout << prod.getQuantity() << '\n';
				products_mutexes[i].unlock();
			}
			i++;
		}
	}
	sale_mutex.lock();
	sales.push_back(s);
	sale_mutex.unlock();
	cout << "A new sale is added.\n";
}

void createRandomSale() {
	random_device rand;
	mt19937 gen(rand());
	uniform_int_distribution<>dis(1, products.size());

	vector<Product> sale_products;
	int number_products = dis(gen);
	while (number_products > 0) {
		random_device rand2;
		mt19937 gen(rand());
		uniform_int_distribution<>dis2(0, products.size() - 1);
		int product_position = dis2(gen);

		while (containsProduct(sale_products, products[product_position])) {
			product_position = dis2(gen);
		}
		sale_products.push_back(products[product_position]);
		number_products--;
	}

	vector<pair<Product, int>> products_quantities;
	for (Product p : sale_products) {
		random_device rand3;
		mt19937 gen(rand());
		uniform_int_distribution<>dis3(1, 30);
		int quantity = dis3(gen);
		pair<Product, int> pairr = make_pair(p, quantity);
		products_quantities.push_back(pairr);
	}

	/*for (pair<Product, int> pair1 : products_quantities) {
		cout << pair1.first.getName() << ' ' << pair1.second << '\n';
	}*/

	Sale s(products_quantities);

	for (pair<Product, int> p : s.getProductsAndQuantities()) {
		for (Product& prod : products) {
			int i = 0;
			if (prod.getName() == p.first.getName()) {
				products_mutexes[i].lock();
				money_mutex.lock();
				money += p.second * p.first.getPrice();
				money_mutex.unlock();
				//cout << prod.getQuantity() << ' ';
				prod.setQuantity(prod.getQuantity() - p.second);
				//cout << prod.getQuantity() << '\n';
				products_mutexes[i].unlock();
			}
			i++;
		}
	}

	sale_mutex.lock();
	sales.push_back(s);
	sale_mutex.unlock();
	cout << "A new sale is added.\n";
}

void consistencyCheck() {
	cout << "Consistency Check\n";
	cout << "\n\n\n";
	money_mutex.lock();
	//cout << "The number of sales is: " << sales.size() << '\n';
	bool ok = 1;
	int expected_money = 0;
	int i = 0;
	for (Product& p : products) {
		products_mutexes[i].lock();
		int sold_quantity = 0;
		sale_mutex.lock();
		for (Sale s : sales) {
			for (pair<Product, int> pairr : s.getProductsAndQuantities()) {
				if (pairr.first.getName() == p.getName()) {
					sold_quantity += pairr.second;
					expected_money += pairr.second * p.getPrice();
				}
			}
		}
		sale_mutex.unlock();
		if (sold_quantity != p.getInitialQuantity() - p.getQuantity()) {
			cout << "Consistency check: Something is wrong at the quantity for product with name: " << p.getName() << ".\n";
			cout << "Sold quantity: " << sold_quantity << '\n';
			cout << "Initial quantity " << p.getInitialQuantity() << '\n';
			cout << "Remaining quantity: " << p.getQuantity() << '\n' << '\n';
			ok = 0;
		}
		products_mutexes[i].unlock();
		i++;
	}
	if (expected_money != money) {
		cout << "Consistency check: Money should be " << expected_money << ", but it is " << money << ".\n";
		ok = 0;
	}
	money_mutex.unlock();
	if (ok == 1) {
		cout << "Consistency check: everything is alright!\n";
		cout << "Money: " << money << '\n';
	}
}

void printAllSales() {
	sale_mutex.lock();
	for (Sale s : sales) {
		cout << "Sale:\n";
		for (pair<Product, int> p : s.getProductsAndQuantities()) {
			cout << "Pair: " << p.first.getName() << ' ' << p.first.getPrice() << ' ' << p.second << '\n';
		}
		cout << '\n';
	}
	sale_mutex.unlock();
}

int main() {
	auto start = std::chrono::high_resolution_clock::now();

	readProducts();
	printAllProducts();

	//vector<pair<Product, int>> products_quantities = createRandomSale(products);
	/*for (pair<Product, int> pair1 : products_quantities) {
		cout << pair1.first.getName() << ' ' << pair1.second << '\n';
	}*/

	const int number_of_threads = 2;
	thread threads[number_of_threads];
	products_mutexes = new mutex[products.size()];
	thread check_threads[number_of_threads];
	int nb_check_threads = 0;

	/*for (int i = 0; i < number_of_threads; i++) {
		threads[i] = thread(createRandomSale);
		threads[i].join();
		if (i % 3 == 0) {
			consistencyCheck();
		}
	}*/

	for (int i = 0; i < number_of_threads; i++) {
		threads[i] = thread(createRandomSale);
		if (i % 3 == 0) {
			consistencyCheck();
		}
	}

	for (int i = 0; i < number_of_threads; i++) {
		threads[i].join();
	}


	thread last_check(consistencyCheck);
	last_check.join();

	thread print_sales(printAllSales);
	print_sales.join();

	printAllProducts();
	cout << "Money: " << money;

	delete[] products_mutexes;

	auto end = std::chrono::high_resolution_clock::now();

	std::chrono::duration<double> duration = end - start;
	double seconds = duration.count();

	std::cout << "Time elapsed: " << seconds << " seconds" << std::endl;

}
#include <iostream>
#include <vector>
#include <thread>
#include <mutex>
#include <condition_variable>
using namespace std;

vector<int> v1;
vector<int> v2;
vector<int> pairs_product;
int scalar_product = 0;

mutex m;
condition_variable cv;
bool ready = false;

void producer_activity() {
    for (int i = 0; i < v1.size(); i++) {
        int product = v1[i] * v2[i];
        pairs_product.push_back(product);
    }

    unique_lock<mutex> lock(m);
    ready = true;
    cv.notify_one();
}

void consumer_activity() {
    unique_lock<mutex> lock(m);
    cv.wait(lock, [] { return ready; });

    for (int product : pairs_product) {
        scalar_product += product;
        cout << product << ' ';
    }
}

int main() {
    v1.push_back(3);
    v1.push_back(5);
    v1.push_back(1);
    v1.push_back(7);

    v2.push_back(5);
    v2.push_back(8);
    v2.push_back(4);
    v2.push_back(9);

    thread producer(producer_activity);
    thread consumer(consumer_activity);

    producer.join();
    consumer.join();

    cout << "\nThe scalar product is " << scalar_product <<'.';
}

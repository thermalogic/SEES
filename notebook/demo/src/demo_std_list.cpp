#include <algorithm>
#include <iostream>
#include <list>

using namespace std;

int main() {
	list<int> my_list = { };
	my_list.push_front(8);
	my_list.push_back(88);
    my_list.push_front(9);
    my_list.push_back(99);
    
    for (int x : my_list) {
		cout << x << ' ';
	}
   cout <<endl;
    
	auto it =find(my_list.begin(), my_list.end(), 88);
	if (it != my_list.end()) {
		my_list.insert(it, 21);
	}
    
	for (int x : my_list) {
		cout << x << ' ';
	}
    cout <<endl;
    
}

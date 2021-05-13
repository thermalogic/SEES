#include <iostream> 
#include <stack> 
using namespace std;

int main() {
	stack<int> st;
	st.push(8);
	st.push(88);

    while (!st.empty()) {
		cout << ' ' << st.top();
		st.pop();
	}
}

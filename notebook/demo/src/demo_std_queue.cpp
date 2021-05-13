#include <iostream>
#include <queue> 
using namespace std;
int main()
{
    queue<int> queue_sample;
    for (int x = 0; x < 5; x++)
        queue_sample.push(x);
    
     while (!queue_sample.empty()) {
        cout << ' ' << queue_sample.front();
        queue_sample.pop();
    }
    return 0;
}

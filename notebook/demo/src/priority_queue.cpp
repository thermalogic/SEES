
#include <iostream>
#include <queue>
using namespace std; 

int main()
{
    priority_queue<float> q;  // 默认的是大顶堆 
    // insert three elements into the priority queue
    q.push(47);
    q.push(70);
    q.push(86); 
    // print the elements
    while (!q.empty())
    {
        cout << q.top() << ' ';
        q.pop();
    }
    cout << endl;
}

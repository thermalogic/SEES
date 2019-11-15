#include <iostream>
#include <vector>

using namespace std;

int main()
{
    std::vector<int> myList;
    for(int i = 0; i < 10; i++)
        myList.push_back(i);
    cout <<myList[2]<<endl; 
}

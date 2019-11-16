#include <iostream>
#include <vector>

using namespace std;

int main()
{
    vector<int> myList;
    for(int i = 0; i < 10; i++)
        myList.push_back(i);
    cout <<myList[2]<<endl; 
    
    for (const int& item : myList)
    {
        cout << item << " ";
    }
    cout << endl;
}

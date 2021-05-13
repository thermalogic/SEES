
/*
Test Driver for List class (TestList.cpp) 
*/
#include <iostream>
#include "List.h"
using namespace std;
 
int main() {
 
   List<int> lst1;
   cout << lst1 << endl;
   lst1.pushFront(8);
   lst1.pushBack(88);
   lst1.pushFront(9);
   lst1.pushBack(99);
   cout << lst1 << endl;
 
   int result;
   lst1.popBack(result)
      ? cout << "value is " << result << ", list is " << lst1 << endl
      : cout << "empty list" << endl;
   lst1.popBack(result)
      ? cout << "value is " << result << ", list is " << lst1 << endl
      : cout << "empty list" << endl;
  
   lst1.popFront(result)
      ? cout << "value is " << result << ", list is " << lst1 << endl
      : cout << "empty list" << endl;
   lst1.popFront(result)
      ? cout << "value is " << result << ", list is " << lst1 << endl
      : cout << "empty list" << endl;
   
    lst1.popBack(result)
      ? cout << "value is " << result << ", list is " << lst1 << endl
      : cout << "empty list" << endl;
}

/* 
  Test Driver for Stack class (TestStack.cpp)
    
*/
#include <iostream>
#include "Stack.h"
using namespace std;
 
int main() {
 
   Stack<int> s1;
   cout << s1 << endl;
   s1.push(8);
   s1.push(88);
   cout << s1 << endl;
 
   int result;
   s1.pop(result)
      ? cout << "value is " << result << ", stack is " << s1 << endl
      : cout << "empty stack" << endl;
 
   s1.push(9);
   s1.push(99);
   cout << s1 << endl;
 
   s1.pop(result)
      ? cout << "value is " << result << ", stack is " << s1 << endl
      : cout << "empty stack" << endl;
 
   s1.pop(result)
      ? cout << "value is " << result << ", stack is " << s1 << endl
      : cout << "empty stack" << endl;
   s1.pop(result)
      ? cout << "value is " << result << ", stack is " << s1 << endl
      : cout << "empty stack" << endl;
   s1.pop(result)
      ? cout << "value is " << result << ", stack is " << s1 << endl
      : cout << "empty stack" << endl;
}

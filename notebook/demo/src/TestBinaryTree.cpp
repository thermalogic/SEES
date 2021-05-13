/* 

Test Driver for BinaryTree class (TestBinaryTree.cpp) 
    
*/
#include <iostream>
#include "BinaryTree.h"
using namespace std;

int main()
{
   BinaryTree<int> t1;
   t1.insert(6);
   t1.insert(10);
   t1.insert(5);
   t1.insert(15);
   t1.insert(7);
   t1.insert(4);
   t1.insert(9);

   cout << "pre-order depth-first search" << endl;
   t1.preOrderTraversal();
   cout << "in-order depth-first search (ascending order)" << endl;
   t1.inOrderTraversal();
   cout << "post-order depth-first search" << endl;
   t1.postOrderTraversal();
   cout << "in-order depth-first search" << endl;
   cout << t1;
}

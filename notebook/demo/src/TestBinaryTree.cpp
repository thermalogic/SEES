/* 

Test Driver for BinaryTree class (TestBinaryTree.cpp) 
    
*/
#include <iostream>
#include "BinaryTree.h"
using namespace std;
 
int main() {
   BinaryTree<int> t1;
   t1.insert(6);
   t1.insert(10);
   t1.insert(5);
   t1.insert(15);
   t1.insert(7);
   t1.insert(4);
   t1.insert(9);
 
   t1.preOrderTraversal();
   t1.inOrderTraversal();
   t1.postOrderTraversal();
   cout << t1;
   t1.breadthFirstTraversal();
}

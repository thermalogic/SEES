/* 
   Node template class for binary tree (Node.h)
*/
#ifndef NODE_H
#define NODE_H
 
template <typename T> class BinaryTree; // Forward reference
 
template <typename T>
class Node {
private:
   T data;
   Node * rightPtr;
   Node * leftPtr;
public:
   Node (T d) : data(d), rightPtr(0), leftPtr(0) { };
   T getData() const { return data; };
   Node * getRightPtr() const { return rightPtr; }
   Node * getLeftPtr() const  { return leftPtr;  }
 
friend class BinaryTree<T>;
   // Make BinaryTree class a friend to access private data
};
 
#endif

/* 
   BinaryTree template class for binary tree (BinaryTree.h)
*/
#ifndef BINARY_TREE_H
#define BINARY_TREE_H

#include <iostream>
#include <queue>
#include "Node.h"

// Forward Reference
template <typename T>
std::ostream &operator<<(std::ostream &os, const BinaryTree<T> &lst);

template <typename T>
class BinaryTree
{
private:
   Node<T> *rootPtr;

   // private helper functions
   void insertNode(Node<T> *&ptr, const T &value);
   void preOrderSubTree(const Node<T> *ptr, std::ostream &os = std::cout) const;
   void inOrderSubTree(const Node<T> *ptr, std::ostream &os = std::cout) const;
   void postOrderSubTree(const Node<T> *ptr, std::ostream &os = std::cout) const;
   void removeSubTree(Node<T> *&ptr);

public:
   BinaryTree();  // Constructor
   ~BinaryTree(); // Destructor
   void insert(const T &value);
   bool isEmpty() const;
   void preOrderTraversal(std::ostream &os = std::cout) const;
   void inOrderTraversal(std::ostream &os = std::cout) const;
   void postOrderTraversal(std::ostream &os = std::cout) const;

   friend std::ostream &operator<<<>(std::ostream &os, const BinaryTree<T> &lst);
   // Overload the stream insertion operator to print the list
};

// Constructor - Create an empty list with no node
template <typename T>
BinaryTree<T>::BinaryTree() : rootPtr(0) {}

// Destructor - Remove all the dynamically allocated nodes
template <typename T>
BinaryTree<T>::~BinaryTree()
{
   removeSubTree(rootPtr);
   // std::cout << "Destructor completed..." << std::endl;
}

template <typename T>
void BinaryTree<T>::removeSubTree(Node<T> *&ptr)
{
   if (ptr)
   {
      removeSubTree(ptr->leftPtr);  // remove left subtree
      removeSubTree(ptr->rightPtr); // remove right subtree
      delete ptr;
   }
}

// Is list empty? Check if rootPtr is null
template <typename T>
bool BinaryTree<T>::isEmpty() const { return rootPtr == 0; }

// Push the data in front by dynamically allocate a new node
template <typename T>
void BinaryTree<T>::insert(const T &value)
{
   insertNode(rootPtr, value);
}

// Need to pass the pointer by reference so as to modify the caller's copy
template <typename T>
void BinaryTree<T>::insertNode(Node<T> *&ptr, const T &value)
{
   if (ptr == 0)
   {
      ptr = new Node<T>(value);
   }
   else
   {
      if (value < ptr->data)
         insertNode(ptr->leftPtr, value);
      else if (value > ptr->data)
         insertNode(ptr->rightPtr, value);
      else
         std::cout << "duplicate value" << std::endl;
   }
}

template <typename T>
void BinaryTree<T>::preOrderTraversal(std::ostream &os) const
{
   os << "{ ";
   preOrderSubTree(rootPtr);
   os << '}' << std::endl;
}

template <typename T>
void BinaryTree<T>::preOrderSubTree(const Node<T> *ptr, std::ostream &os) const
{
   if (ptr)
   {
      os << ptr->data << ' ';
      preOrderSubTree(ptr->leftPtr);
      preOrderSubTree(ptr->rightPtr);
   }
}

template <typename T>
void BinaryTree<T>::inOrderTraversal(std::ostream &os) const
{
   os << "{ ";
   inOrderSubTree(rootPtr);
   os << '}' << std::endl;
}

template <typename T>
void BinaryTree<T>::inOrderSubTree(const Node<T> *ptr, std::ostream &os) const
{
   if (ptr)
   {
      inOrderSubTree(ptr->leftPtr);
      os << ptr->data << ' ';
      inOrderSubTree(ptr->rightPtr);
   }
}

template <typename T>
void BinaryTree<T>::postOrderTraversal(std::ostream &os) const
{
   os << "{ ";
   postOrderSubTree(rootPtr);
   os << '}' << std::endl;
}

template <typename T>
void BinaryTree<T>::postOrderSubTree(const Node<T> *ptr, std::ostream &os) const
{
   if (ptr)
   {
      postOrderSubTree(ptr->leftPtr);
      postOrderSubTree(ptr->rightPtr);
      os << ptr->data << ' ';
   }
}

// Overload the stream insertion operator to print the list in in-order traversal
template <typename T>
std::ostream &operator<<(std::ostream &os, const BinaryTree<T> &lst)
{
   lst.inOrderTraversal(os);
   return os;
}

#endif

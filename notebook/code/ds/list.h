#ifndef LIST_H
#define LIST_H
 
#include <iostream>
#include "Node.h"
 
// Forward Reference
template <typename T>
std::ostream & operator<<(std::ostream & os, const List<T> & lst);
 
template <typename T>
class List {
private:
   Node<T> * frontPtr;  // First node
   Node<T> * backPtr;   // Last node
public:
   List();   // Constructor
   ~List();  // Destructor
   void pushFront(const T & value);
   void pushBack(const T & value);
   bool popFront(T & value);
   bool popBack(T & value);
   bool isEmpty() const;
 
friend std::ostream & operator<< <>(std::ostream & os, const List<T> & lst);
      // Overload the stream insertion operator to print the list
};
 
// Constructor - Create an empty list without any node
template <typename T>
List<T>::List() : frontPtr(0), backPtr(0) { }
 
// Destructor - Remove all the dynamically allocated nodes
template <typename T>
List<T>::~List() {
   while (frontPtr) {
      Node<T> * tempPtr = frontPtr;
      frontPtr = frontPtr->nextPtr;
      delete tempPtr;
   }
   // std::cout << "Destructor completed..." << std::endl;
}
 
// Is list empty? Check if frontPtr is null
template <typename T>
bool List<T>::isEmpty() const { return frontPtr == 0; }
 
// Push the data in front by dynamically allocate a new node
template <typename T>
void List<T>::pushFront(const T & value) {
   Node<T> * newNodePtr = new Node<T>(value);
   if (isEmpty()) {
      frontPtr = backPtr = newNodePtr;
   } else {
      newNodePtr->nextPtr = frontPtr;
      frontPtr = newNodePtr;
   }
}
 
// Push the data at the end by dynamically allocate a new node
template <typename T>
void List<T>::pushBack(const T & value) {
   Node<T> * newNodePtr = new Node<T>(value);
   if (isEmpty()) {
      frontPtr = backPtr = newNodePtr;
   } else {
      backPtr->nextPtr = newNodePtr;
      backPtr = newNodePtr;
   }
}
 
// Pop and the data in front to value and remove the node
template <typename T>
bool List<T>::popFront(T & value) {
   if (isEmpty()) {
      return false;
   } else if (frontPtr == backPtr) {  // only one node
      value = frontPtr->data;
      delete frontPtr;         // remove node
      frontPtr = backPtr = 0;  // empty
   } else {
      value = frontPtr->data;
      Node<T> * tempPtr = frontPtr;
      frontPtr = frontPtr->nextPtr;
      delete tempPtr;
   }
   return true;
}
 
// Pop and the data at the end to value and remove the node
template <typename T>
bool List<T>::popBack(T & value) {
   if (isEmpty()) {
      return false;
   } else if (frontPtr == backPtr) {  // only one node
      value = backPtr->data;
      delete backPtr;          // remove node
      frontPtr = backPtr = 0;  // empty
   } else {
      // Locate second to last node
      Node<T> * currentPtr = frontPtr;
      while (currentPtr->nextPtr != backPtr) {
         currentPtr = currentPtr->nextPtr;
      }
      value = backPtr->data;
      delete backPtr;          // remove last node
      backPtr = currentPtr;
      currentPtr->nextPtr = 0;
   }
   return true;
}
 
// Overload the stream insertion operator to print the list
template <typename T>
std::ostream & operator<< (std::ostream & os, const List<T> & lst) {
   os << '{';
   if (!lst.isEmpty()) {
      Node<T> * currentPtr = lst.frontPtr;
      while (currentPtr) {
         os << currentPtr->getData();
         if (currentPtr != lst.backPtr) os << ',';
         currentPtr = currentPtr->getNextPtr();
      }
   }
   os << '}';
}
 
#endif

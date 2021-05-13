/* 
    DoubleLinkedList template class for double linked list
   (DoubleLinkedList.h)
*/
#ifndef DOUBLE_LINKED_LIST_H
#define DOUBLE_LINKED_LIST_H

#include <iostream>
#include "DoubleLinkedNode.h"

// Forward Reference
template <typename T>
std::ostream &operator<<(std::ostream &os,
                         const DoubleLinkedList<T> &lst);

template <typename T>
class DoubleLinkedList
{
private:
   DoubleLinkedNode<T> *frontPtr;
   DoubleLinkedNode<T> *backPtr;

public:
   DoubleLinkedList();  // Constructor
   ~DoubleLinkedList(); // Destructor
   void pushFront(const T &value);
   void pushBack(const T &value);
   bool popFront(T &value);
   bool popBack(T &value);
   bool isEmpty() const;

   friend std::ostream &operator<<<>(std::ostream &os,
                                     const DoubleLinkedList<T> &lst);
   // Overload the stream insertion operator to print the list
};

// Constructor - Create an empty list with no node
template <typename T>
DoubleLinkedList<T>::DoubleLinkedList() : frontPtr(0), backPtr(0) {}

// Destructor - Remove all the dynamically allocated nodes
template <typename T>
DoubleLinkedList<T>::~DoubleLinkedList()
{
   while (frontPtr)
   {
      DoubleLinkedNode<T> *tempPtr = frontPtr;
      frontPtr = frontPtr->nextPtr;
      delete tempPtr;
   }
   // std::cout << "Destructor completed..." << std::endl;
}

// Is list empty? Check if frontPtr is null
template <typename T>
bool DoubleLinkedList<T>::isEmpty() const { return frontPtr == 0; }

// Push the data in front by dynamically allocate a new node
template <typename T>
void DoubleLinkedList<T>::pushFront(const T &value)
{
   DoubleLinkedNode<T> *newPtr = new DoubleLinkedNode<T>(value);
   if (isEmpty())
   {
      frontPtr = backPtr = newPtr;
   }
   else
   {
      frontPtr->prevPtr = newPtr;
      newPtr->nextPtr = frontPtr;
      frontPtr = newPtr;
   }
}

// Push the data at the end by dynamically allocate a new node
template <typename T>
void DoubleLinkedList<T>::pushBack(const T &value)
{
   DoubleLinkedNode<T> *newPtr = new DoubleLinkedNode<T>(value);
   if (isEmpty())
   {
      frontPtr = backPtr = newPtr;
   }
   else
   {
      backPtr->nextPtr = newPtr;
      newPtr->prevPtr = backPtr;
      backPtr = newPtr;
   }
}

// Pop and the data in front to value and remove the node
template <typename T>
bool DoubleLinkedList<T>::popFront(T &value)
{
   if (isEmpty())
   {
      return false;
   }
   else if (frontPtr == backPtr)
   { // only one node
      value = frontPtr->data;
      delete frontPtr;        // remove node
      frontPtr = backPtr = 0; // empty
   }
   else
   {
      value = frontPtr->data;
      DoubleLinkedNode<T> *tempPtr = frontPtr;
      frontPtr = frontPtr->nextPtr;
      frontPtr->prevPtr = 0;
      delete tempPtr;
   }
   return true;
}

// Pop and the data at the end to value and remove the node
template <typename T>
bool DoubleLinkedList<T>::popBack(T &value)
{
   if (isEmpty())
   {
      return false;
   }
   else if (frontPtr == backPtr)
   { // only one node
      value = backPtr->data;
      delete backPtr;         // remove node
      frontPtr = backPtr = 0; // empty
   }
   else
   {
      value = backPtr->data;
      DoubleLinkedNode<T> *tempPtr = backPtr;
      backPtr = backPtr->prevPtr; // 2nd last node
      backPtr->nextPtr = 0;
      delete tempPtr;
   }
   return true;
}

// Overload the stream insertion operator to print the list
template <typename T>
std::ostream &operator<<(std::ostream &os, const DoubleLinkedList<T> &lst)
{
   os << '{';
   if (!lst.isEmpty())
   {
      DoubleLinkedNode<T> *currentPtr = lst.frontPtr;
      while (currentPtr)
      {
         os << currentPtr->getData();
         if (currentPtr != lst.backPtr)
            os << ',';
         currentPtr = currentPtr->getNextPtr();
      }
   }
   os << '}';
}

#endif

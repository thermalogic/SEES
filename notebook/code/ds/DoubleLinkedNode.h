/* DoubleLinkedNode template class for double linked list (DoubleLinkedNode.h) */
#ifndef DOUBLE_LINKED_NODE_H
#define DOUBLE_LINKED_NODE_H
 
template <typename T> class DoubleLinkedList; // Forward reference
 
template <typename T>
class DoubleLinkedNode {
private:
   T data;
   DoubleLinkedNode * nextPtr;
   DoubleLinkedNode * prevPtr;
public:
   DoubleLinkedNode (T d) : data(d), nextPtr(0), prevPtr(0) { };
   T getData() const { return data; };
   DoubleLinkedNode * getNextPtr() const { return nextPtr; }
   DoubleLinkedNode * getPrevPtr() const { return prevPtr; }
 
friend class DoubleLinkedList<T>;
   // Make DoubleLinkedList class a friend to access private data
};
 
#endif

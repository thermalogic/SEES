#ifndef NODE_H
#define NODE_H

template <typename T>
class List; // Forward reference

template <typename T>
class Node
{
private:
   T data;
   Node *nextPtr;

public:
   Node(T d) : data(d), nextPtr(0){};           // Constructor
   T getData() const { return data; };          // Public getter for data
   Node *getNextPtr() const { return nextPtr; } // Public getter for nextPtr

   friend class List<T>; // Make List class a friend to access private data
};

#endif

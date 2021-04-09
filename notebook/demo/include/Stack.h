
#ifndef STACK_H
#define STACK_H

#include <iostream>

// Forward Reference
template <typename T>
class Stack;
template <typename T>
std::ostream &operator<<(std::ostream &os, const Stack<T> &s);

template <typename T>
class Stack
{
private:
   T *data;       // Array
   int tos;       // Top of stack, start at index -1
   int capacity;  // capacity of the array
   int increment; // each subsequent increment size
public:
   explicit Stack(int capacity = 10, int increment = 10);
   ~Stack(); // Destructor
   void push(const T &value);
   bool pop(T &value);
   bool isEmpty() const;

   friend std::ostream &operator<<<>(std::ostream &os, const Stack<T> &s);
   // Overload the stream insertion operator to print the list
};

// Constructor - Create an empty list without any node
template <typename T>
Stack<T>::Stack(int cap, int inc) : capacity(cap), increment(inc)
{
   data = new T[capacity];
   tos = -1;
}

// Destructor - Remove all the dynamically allocated nodes
template <typename T>
Stack<T>::~Stack()
{
   delete[] data; // remove the dynamically allocate storage
   // std::cout << "Destructor completed..." << std::endl;
}

// Is list empty? Check if frontPtr is null
template <typename T>
bool Stack<T>::isEmpty() const { return tos < 0; }

// Push the data on top of the stack
template <typename T>
void Stack<T>::push(const T &value)
{
   if (tos < capacity - 1)
   {
      // Have space, simply add in the value
      data[++tos] = value;
   }
   else
   {
      // No more space. Allocate a bigger array
      T *newDataPtr = new T[capacity + increment];
      for (int i = 0; i <= tos; ++i)
      {
         newDataPtr[i] = data[i]; // copy over
      }
      delete[] data;
      data = newDataPtr;
   }
}

// Pop the data from the TOS
template <typename T>
bool Stack<T>::pop(T &value)
{
   if (isEmpty())
   {
      return false;
   }
   else
   {
      value = data[tos--];
   }
   return true;
}

// Overload the stream insertion operator to print the list
template <typename T>
std::ostream &operator<<(std::ostream &os, const Stack<T> &stack)
{
   os << '{';
   for (int i = stack.tos; i >= 0; --i)
   {
      os << stack.data[i];
      if (i > 0)
         os << ',';
   }
   os << '}';
}

#endif

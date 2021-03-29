#include <iostream>
#include "queue.h"

using namespace std;

Queue::Queue(int size) 
{
	values = new double[size];
	maxSize = size;
	front = 0;
	rear = -1;
	counter = 0;
}

Queue::~Queue() 
{ 
	delete [] values; 
}

bool Queue::IsEmpty() 
{
	if (counter)
		return false;
	else 
		return true;
}

bool Queue::IsFull() 
{
	if (counter < maxSize)
		return false;
	else 
		return true;
}

bool Queue::Enqueue(double x) 
{
	if (IsFull()) 
	{
		cout<< "Error: the queue is full." << endl;
		return false;
	}
	else 
	{
		// calculate the new rear position (circular)
		rear= (rear + 1) % maxSize; 
		// insert new item
		values[rear]= x;
		// update counter
		counter++;
		return true;
	}
}

bool Queue::Dequeue(double &x) 
{
	if (IsEmpty()) 
	{
		cout<< "Error: the queue is empty." << endl;
		return false;
	}
	else 
	{
		// retrieve the front item
		x= values[front];
		// move front 
		front= (front + 1) % maxSize;
		// update counter
		counter--;
		return true;
	}
}

void Queue::DisplayQueue()
{
	cout<< "front -->";
	for (int i = 0; i < counter; i++) 
	{
		if (i == 0) 
			cout << "\t";
		else 
			cout << "\t\t"; 
		cout<< values[(front + i) % maxSize];
		if (i != counter - 1)
			cout << endl;
		else
			cout << "\t<--rear" << endl;
	}
}

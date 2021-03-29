class Queue 
{
	public:
		Queue(int size);// constructor
		~Queue();// destructor
		bool IsEmpty(void);
		bool IsFull(void);
		bool Enqueue(double x);
		bool Dequeue(double &x);
		void DisplayQueue(void);
	private:
		int front;// front index
		int rear;// rear index
		int counter;// number of elements
		int maxSize;// size of array queue
		double* values;// element array
};

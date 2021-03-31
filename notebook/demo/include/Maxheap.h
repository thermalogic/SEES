
#ifndef MAXHEAP_H
#define MAXHEAP_H

#include<iostream>
using namespace std;
//enum bool{true, false};
#define defaultSize 100
template<class T>
class MaxHeap {
public:
	MaxHeap(int sz = defaultSize);         //最大堆的默认构造函数
	MaxHeap(T arr[], int sz);             //通过一个数组创建构造函数
	~MaxHeap();                            //析构函数
	bool insert(const T& x);              //将x插入到最大堆中
	bool removeMax(T& x);                //删除最大堆中最大的元素，保存至x中
	bool isEmpty();                       //判断最大堆是否为空
	bool isFull();                       //判断最大堆是否满
	void makeEmpty();                     //将最大堆置空
	void display();                      //输出最小堆
private:
	T* _heap;                              //存放堆中元素的数组
	int _currentSize;                       //最最大堆中当前元素的个数
	int _maxHeapSize;                       //最最大堆最多允许的个数
	void shifDown(int start, int end);      //从start 到end下滑调整为最大堆
	void shifUp(int start);                //从start 到0上滑调整为最大堆
};
 
 
//最大堆的默认构造函数
template<class T>
MaxHeap<T>::MaxHeap(int sz /*= defaultSize*/) {
	_maxHeapSize = (sz > defaultSize) ? sz : defaultSize;    //_maxHeapSize为参数sz与defaultSize中的较大者
	_heap = new T[_maxHeapSize];                             //为堆数组分配内存
	if (_heap == nullptr) {                                  //内存分配错误
		cerr << "内存分配错误！" << endl;
		exit(-1);
	}
	_currentSize = 0;                                       //当前堆元素个数为0
}
 
//通过一个数组创建构造函数
template<class T>
MaxHeap<T>::MaxHeap(T arr[], int sz) {
	_maxHeapSize = (sz > defaultSize) ? sz : defaultSize;    //_maxHeapSize为参数sz与defaultSize中的较大者
	_heap = new T[_maxHeapSize];                                       //为堆数组分配内存，大小为参数数组个数
	if (_heap == nullptr) {                                  //内存分配错误
		cerr << "内存分配错误！" << endl;
		exit(-1);
	}
 
	for (int i = 0; i < sz; i++)                             //将参数数组赋值给堆元素数组
		_heap[i] = arr[i];
	_currentSize = sz;                                       //建立当前堆数组大小
 
	int currentPos = (_currentSize - 1) / 2;                 //当前位置指向最后一个有子结点的父节点
	while (currentPos >= 0) {                                //还未达到根节点，就继续循环
		shifDown(currentPos, _currentSize - 1);              //自底向上(对于整个堆而言)-自上而下(对于局部堆而言)调整为最大堆
		currentPos--;
	}
}
 
//从start 到end下滑调整为最小堆
//这个的前提是在值之前子堆已经是最大堆
template<class T>
void MaxHeap<T>::shifDown(int start, int end) {
	int i = start;
	int j = 2 * i + 1;                                      //j指向当前结点的左子结点
	T tempValue = _heap[i];                                 //tempValue暂存当前父节点的值
	while (j <= end) {                                      //当未达到end时，就一直循环下去
		if (j < end && _heap[j] < _heap[j + 1])             //如果有右子结点并且右结点较大，j就指向右结点
			j++;
		if (tempValue >= _heap[j])                          //如果当前父节点的值大于子结点就直接进行下一轮循环
			break;
		else {                                              //否则就将子结点的值赋值给父节点
			_heap[i] = _heap[j];
			i = j;                                          //父节点指向当前子节点
			j = 2 * i + 1;                                  //子节点指向当前父节点的左子结点
		}
	}
	_heap[i] = tempValue;                                  //回返
}
 
//从start 到0上滑调整为最大堆
//这个的前提是在值之前堆已经是最大堆
template<class T>
void MaxHeap<T>::shifUp(int start) {
	int j = start;
	int i = (j - 1) / 2;                                    //i当前结点的父节点
	T tempValue = _heap[j];                                 //tempValue暂存当前节点的值
	while (j > 0) {                                         //达到父节点之前一直循环
		if (_heap[i] >= tempValue)                          //如果父节点大于等于子节点的值就进行下一层循环
			break;
		else {
			_heap[j] = _heap[i];                           //将父节点的值赋值给子节点
			j = i;                                         //子结点指向当前父节点
			i = (j - 1) / 2;                               //父节点指向当前子节点的父节点
		}
	}
	_heap[j] = tempValue;                                  //回反
}
 
//析构函数
template<class T>
MaxHeap<T>::~MaxHeap() {
	if (_heap != nullptr)
		delete _heap;
}
 
//公共函数将x插入到最小堆中
template<class T>
bool MaxHeap<T>::insert(const T& x) {
	if (isFull())                                           //如果已满，就不能进行插入
		return false;
	_heap[_currentSize] = x;                               //将参数赋值给新的堆元素
	shifUp(_currentSize);                                  //调用shifUp函数进行最大堆调整
	_currentSize++;                                        //参数个数自增加一
	return true;
}
 
//删除最小堆中最小的元素，保存至x中
template<class T>
bool MaxHeap<T>::removeMax(T& x) {
	if (isEmpty())                                         //如果已空,就不能进行删除
		return false;
	x = _heap[0];                                         //堆顶元素赋值给返回参数x
	_heap[0] = _heap[_currentSize - 1];                   //将最后一个元素赋值给堆顶元素
	_currentSize--;                                       //参数个数自减减一
	shifDown(0, _currentSize - 1);                        //调用shifDown函数进行最大堆调整  
	return true;
}
 
//判断最小堆是否为空
template<class T>
bool  MaxHeap<T>::isEmpty() {
	return _currentSize == 0;
}
 
//判断最小堆是否满 
template<class T>
bool  MaxHeap<T>::isFull() {
	return _currentSize == _maxHeapSize;
}
 
//将最小堆置空
template<class T>
void  MaxHeap<T>::makeEmpty() {
	if (!isEmpty()) {                             //如果不为空
		delete _heap;
		_currentSize = 0;
	}
}
 
//输出最小堆
template<class T>
void MaxHeap<T>::display() {
	for (int i = 0; i < _currentSize; i++)
		cout << _heap[i] << " ";
	cout << endl;
}
#endif

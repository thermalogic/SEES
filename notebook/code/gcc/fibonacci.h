
#ifndef FIBONACCI_H
#define FIBONACCI_H

/*
  Up to 93rd Fibonacci number, starting from 0th  can be computed. 
  
  Anything larger will overflow.
*/

#define CACHE_SIZE 94 

unsigned long fibonacci(int n, unsigned long *fib_cache);

#endif

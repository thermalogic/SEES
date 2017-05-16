
#include "fibonacci.h"

/*
* Function to compute nth Fibonacci number.
*
*   It uses a cache to avoid repetitive computation. 
*       1）Reference to the cache must be passed to the function. 
*       2）The cache should contain 0 for uncomputed values.
*   Returns -1 on negative input.
*/

unsigned long fibonacci(int n, unsigned long *fib_cache) {
 
  if (n< 0)
      return -1;
  
  // base case 0 or 1
  if (n == 0||n==1)
      return 1;
  
  // check if nth value is available in cache
  if (fib_cache[n] != 0)
     return fib_cache[n];

  // recursive case : compute and store in cache
  fib_cache[n] = fibonacci(n - 1, fib_cache) + fibonacci(n - 2, fib_cache);

  return fib_cache[n];
}
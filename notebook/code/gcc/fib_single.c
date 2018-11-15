
#include <stdio.h>  /* printf, NULL */
#include <stdlib.h> /* calloc, exit, free */

#define CACHE_SIZE 94 

/*
  Function to compute nth Fibonacci number.

   Up to 93rd Fibonacci number, starting from 0th  can be computed. 
   Anything larger will overflow.

   It uses a cache to avoid repetitive computation. 
       1）Reference to the cache must be passed to the function. 
       2）The cache should contain 0 for uncomputed values.
    Returns -1 on negative input.
*/

unsigned long fibonacci(int n, unsigned long *fib_cache)
{
 
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

int main() {

    unsigned long *fib_cache;   // cache to store fibonacci numbers
    
    // cache initialization
    fib_cache=(unsigned long *)calloc(CACHE_SIZE, sizeof(unsigned long));
    
    if(fib_cache==NULL) exit (1);
   
    int n=20;
    printf("fib of %d = %lu\n", n,fibonacci(n, fib_cache));
    free(fib_cache);
   
    return 0;
}

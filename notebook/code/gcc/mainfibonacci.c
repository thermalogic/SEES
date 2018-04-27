
#include <stdio.h>  /* printf, NULL */
#include <stdlib.h> /* calloc, exit, free */
#include "fibonacci.h"

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
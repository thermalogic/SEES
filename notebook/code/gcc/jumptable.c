#include <stdio.h>
#include <stdlib.h>

typedef void (*Handler)(void);    /* A pointer to a handler function */

/* The functions */
void func3 (void) { printf( "3\n" ); }
void func2 (void) { printf( "2\n" ); }
void func1 (void) { printf( "1\n" ); }
void func0 (void) { printf( "0\n" ); }

Handler jump_table[4] = {func0, func1, func2, func3};

int main (void)
{
    int value;
    for(int i=0;i<10;i++)
    {
      /* Convert i to 0-3 integer (modulus) */
       value = ((i % 4) + 4) % 4;
      /* Call appropriate function (func0 thru func3) */
      jump_table[value]();
    };    

    return 0;
}

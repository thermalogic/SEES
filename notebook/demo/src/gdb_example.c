// -------------------------------------------------------------
// A program to be debugged in a GDB session
//     gdb_example.c:
// Test the swap() function, which exchanges the contents of two int variables.
// -------------------------------------------------------------

#include <stdio.h>
void swap( int *p1, int *p2 ); // Exchange *p1 and *p2

int main()
{
    int a = 10, b = 20;
    /* ... */
    printf( "The old values: a = %d; b = %d.\n", a, b );
    swap( &a, &b );
    printf( "The new values: a = %d; b = %d.\n", a, b );
    /* ... */
    return 0;
}

void swap( int *p1, int *p2 ) // Exchange *p1 and *p2
{
    int *p = p1;
    p1 = p2;
    p2 = p;
}
